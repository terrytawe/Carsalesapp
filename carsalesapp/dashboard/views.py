from django.shortcuts import render

# ────────────────────────────────────────────────────────────────────────────────────────────────
# Create your views here.
# ────────────────────────────────────────────────────────────────────────────────────────────────
def customer_view(request):
    return render(request, 'dashboard/dashboard-customer.html')

# ────────────────────────────────────────────────────────────────────────────────────────────────
#
# ────────────────────────────────────────────────────────────────────────────────────────────────
def admin_view(request):
    return render(request, 'dashboard/dashboard-employee.html')
