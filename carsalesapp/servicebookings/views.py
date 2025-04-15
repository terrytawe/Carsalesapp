from django.shortcuts import render

# Create your views here.
def bookings_create(request):
    return render(request, 'servicebookings/booking-create.html')