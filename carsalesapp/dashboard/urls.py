from . import views
from django.urls import path

urlpatterns = [
     path('customer-main', views.customer_view, name="dashboard-customer"), 
     path('dashboard-staff', views.admin_view, name="dashboard-employee")
]
