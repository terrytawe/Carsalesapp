from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.timezone import now
from django.contrib import messages
from .models import CustomerVehicle, ServiceRecord, TestDriveRecord, ServiceType
from inventory.models import Category, VehicleBrand


# ────────────────────────────────────────────────────────────────────────────────────────────────
# Test Drive Booking Views
# ────────────────────────────────────────────────────────────────────────────────────────────────
@login_required
def booking_create(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'servicebookings/booking-create.html', context)

# ────────────────────────────────────────────────────────────────────────────────────────────────
# Display Test Drive Views
# ────────────────────────────────────────────────────────────────────────────────────────────────
@login_required
def booking_display(request, id):
    booking = TestDriveRecord.objects.get(pk=id)
    context = {
        'booking': booking,
        'values': booking
    }
    return render(request, 'servicebookings/booking-display.html', context)


# ────────────────────────────────────────────────────────────────────────────────────────────────
# Display list
# ────────────────────────────────────────────────────────────────────────────────────────────────
@login_required
def booking_list(request):
    try:
        bookings = TestDriveRecord.objects.filter(
            requested_by=request.user
        ).select_related('vehicle').order_by('-created_on')
        return render(request, 'servicebookings/booking-list.html', {'bookings': bookings})

    except Exception as e:
        messages.error(request, f"Failed to load booking records: {str(e)}")
        return render(request, 'servicebookings/booking-list.html', {'bookings': []})

# ────────────────────────────────────────────────────────────────────────────────────────────────
# Manage test drive
# ────────────────────────────────────────────────────────────────────────────────────────────────
@login_required
def booking_manage(request, id):

    return render(request, 'servicebookings/booking-manage.html')


# ────────────────────────────────────────────────────────────────────────────────────────────────
# Service Request Creation View (with error handling)
# ────────────────────────────────────────────────────────────────────────────────────────────────
@login_required
def service_create(request):

    service_types = ServiceType.objects.all()
    context={
        'services': service_types
    }

    if request.method == 'POST':
        try:
            make            = request.POST.get('make', '').strip()
            model           = request.POST.get('model', '').strip()
            year_raw        = request.POST.get('year')
            license_plate   = request.POST.get('license_plate', '').strip().upper()
            service_type    = ServiceType.objects.get(pk=request.POST.get('service_type'))
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
                license_plate   = license_plate,
                defaults        = { 'make': make, 'model': model, 'year': year }
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
            return redirect('manage-service')

        except Exception as e:
            messages.error(request, f"An unexpected error occurred: {str(e)}")
            return render(request, 'servicebookings/service-create.html')

    return render(request, 'servicebookings/service-create.html', context)


# ────────────────────────────────────────────────────────────────────────────────────────────────
# Display Service View
# ────────────────────────────────────────────────────────────────────────────────────────────────
@login_required
def service_display(request, id):
    service_record = ServiceRecord.objects.get(pk=id)
    service_types = ServiceType.objects.all()
    context = {
        'service': service_record,
        'values': service_record,
        'services': service_types
    }
    return render(request, 'servicebookings/service-display.html', context)


# ────────────────────────────────────────────────────────────────────────────────────────────────
# Service Management View (safe and stable)
# ────────────────────────────────────────────────────────────────────────────────────────────────
@login_required
def service_manage(request, id):
    service_record = ServiceRecord.objects.get(pk=id)
    service_types = ServiceType.objects.all()
    context = {
        'service': service_record,
        'values': service_record,
        'services': service_types
    }
    return render(request, 'servicebookings/service-manage.html', context)
    

# ────────────────────────────────────────────────────────────────────────────────────────────────
# Service Management View (safe and stable)
# ────────────────────────────────────────────────────────────────────────────────────────────────
@login_required
def service_list(request):
    try:
        services = ServiceRecord.objects.filter(
            created_by=request.user
        ).select_related('vehicle').order_by('-created_on')
        return render(request, 'servicebookings/service-list.html', {'services': services})

    except Exception as e:
        messages.error(request, f"Failed to load service records: {str(e)}")
        return render(request, 'servicebookings/service-list.html', {'services': []})
    