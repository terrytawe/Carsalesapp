from django.shortcuts import render

# Create your views here.
def bookings_create(request):
    return render(request, 'servicebookings/booking-create.html')

def service_create(request):
    return render(request, 'servicebookings/service-create.html')

def service_manage(request):
    return render(request, 'servicebookings/service-manage.html', {})