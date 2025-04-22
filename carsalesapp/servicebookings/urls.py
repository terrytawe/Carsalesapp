from . import views
from django.urls import path

urlpatterns = [
    path('create-booking', views.booking_create, name="create-booking"),
    path('display-booking/<int:id>', views.booking_display, name="display-booking"),
    path('manage-booking', views.booking_manage, name="manage-booking"),
    path('create-service', views.service_create, name="create-service"),
    path('display-service/<int:id>', views.service_display, name="display-service"),
    path('manage-service', views.service_manage, name="manage-service")
]
