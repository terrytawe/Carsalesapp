from . import views
from django.urls import path

urlpatterns = [
    path('create-booking', views.bookings_create, name="create-booking"),
    path('create-service', views.service_create, name="create-service"),
    path('manage-service', views.service_manage, name="manage-service")
]
