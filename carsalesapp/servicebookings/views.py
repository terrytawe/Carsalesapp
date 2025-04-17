from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.timezone import now
from .models import CustomerVehicle, ServiceRecord

# ────────────────────────────────────────────────────────────────────────────────────────────────
# Test Drive Booking Views (unchanged)
# ────────────────────────────────────────────────────────────────────────────────────────────────
def bookings_create(request):
    return render(request, 'servicebookings/booking-create.html')

def bookings_manage(request):
    return render(request, 'servicebookings/booking-manage.html')


# ────────────────────────────────────────────────────────────────────────────────────────────────
# Service Request Creation View
# ────────────────────────────────────────────────────────────────────────────────────────────────
@login_required
def service_create(request):
    if request.method == 'POST':
        make = request.POST.get('make').strip()
        model = request.POST.get('model').strip()
        year = int(request.POST.get('year'))
        license_plate = request.POST.get('license_plate').strip().upper()
        service_type = request.POST.get('service_type')
        description = request.POST.get('description', '').strip()

        # Step 1: Retrieve or create the vehicle
        vehicle, created = CustomerVehicle.objects.get_or_create(
            license_plate=license_plate,
            defaults={'make': make, 'model': model, 'year': year}
        )

        # Update vehicle info if changed
        if not created and (vehicle.make != make or vehicle.model != model or vehicle.year != year):
            vehicle.make = make
            vehicle.model = model
            vehicle.year = year
            vehicle.save()

        # Step 2: Create the service request
        ServiceRecord.objects.create(
            vehicle=vehicle,
            service_type=service_type,
            description=description,
            status='PENDING',
            created_by=request.user,
            last_modified_by=request.user,
            created_on=now()
        )

        return redirect('service-manage')  # Replace with your URL name

    return render(request, 'servicebookings/service-create.html')


# ────────────────────────────────────────────────────────────────────────────────────────────────
# Service Management View (basic for now)
# ────────────────────────────────────────────────────────────────────────────────────────────────
@login_required
def service_manage(request):
    services = ServiceRecord.objects.filter(created_by=request.user).select_related('vehicle').order_by('-created_on')
    return render(request, 'servicebookings/service-manage.html', {'services': services})