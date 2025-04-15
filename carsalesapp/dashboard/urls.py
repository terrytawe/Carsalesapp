from . import views
from django.urls import path

urlpatterns = [
     path('customer-main', views.customer_view, name="customer-dashboard"), 
     path('dashboard-staff', views.admin_view, name="admin-dashboard")
]
