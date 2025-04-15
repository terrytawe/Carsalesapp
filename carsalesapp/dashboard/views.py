from django.shortcuts import render


# Create your views here.
def customer_view(request):
    return render(request, 'dashboard/customer-dashboard.html')

def admin_view(request):
    return render(request, 'dashboard/staff-dashboard.html')
