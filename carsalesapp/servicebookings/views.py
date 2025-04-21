from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.timezone import now
from django.contrib import messages
from .models import CustomerVehicle, ServiceRecord
from inventory.models import Category, VehicleBrand


# ────────────────────────────────────────────────────────────────────────────────────────────────
# Test Drive Booking Views
# ────────────────────────────────────────────────────────────────────────────────────────────────
@login_required
def bookings_create(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'servicebookings/booking-create.html', context)

# ────────────────────────────────────────────────────────────────────────────────────────────────
# Test Drive Management Views
# ────────────────────────────────────────────────────────────────────────────────────────────────
@login_required
def bookings_manage(request):
    return render(request, 'servicebookings/booking-manage.html')


# ────────────────────────────────────────────────────────────────────────────────────────────────
# Service Request Creation View (with error handling)
# ────────────────────────────────────────────────────────────────────────────────────────────────
@login_required
def service_create(request):
    if request.method == 'POST':
        try:
            make            = request.POST.get('make', '').strip()
            model           = request.POST.get('model', '').strip()
            year_raw        = request.POST.get('year')
            license_plate   = request.POST.get('license_plate', '').strip().upper()
            service_type    = request.POST.get('service_type', '').strip()
            description     = request.POST.get('description', '').strip()

            # Check required fields
            if not all([make, model, year_raw, license_plate, service_type]):
                messages.error(request, "All fields except notes are required.")
                return render(request, 'servicebookings/service-create.html')

            try:
                year = int(year_raw)
            except ValueError:
                messages.error(request, "Year must be a valid number.")
                return render(request, 'servicebookings/service-create.html')

            # Step 1: Retrieve or create the vehicle
            vehicle, created    = CustomerVehicle.objects.get_or_create(
                license_plate   =license_plate,
                defaults={'make': make, 'model': model, 'year': year}
            )

            # Step 2: Update vehicle info if it differs
            if not created and (vehicle.make != make or vehicle.model != model or vehicle.year != year):
                vehicle.make    = make
                vehicle.model   = model
                vehicle.year    = year
                vehicle.save()

            # Step 3: Create the service request
            ServiceRecord.objects.create(
                vehicle         = vehicle,
                service_type    = service_type,
                description     = description,
                status          = 'PENDING',
                created_by      = request.user,
                created_on      = now()
            )

            messages.success(request, "Service request created successfully.")
            return redirect('service-manage')

        except Exception as e:
            messages.error(request, f"An unexpected error occurred: {str(e)}")
            return render(request, 'servicebookings/service-create.html')

    return render(request, 'servicebookings/service-create.html')


# ────────────────────────────────────────────────────────────────────────────────────────────────
# Service Management View (safe and stable)
# ────────────────────────────────────────────────────────────────────────────────────────────────
@login_required
def service_manage(request):
    try:
        services = ServiceRecord.objects.filter(
            created_by=request.user
        ).select_related('vehicle').order_by('-created_on')
        return render(request, 'servicebookings/service-manage.html', {'services': services})

    except Exception as e:
        messages.error(request, f"Failed to load service records: {str(e)}")
        return render(request, 'servicebookings/service-manage.html', {'services': []})