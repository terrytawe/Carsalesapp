from . import views
from .views import ServiceRecordUpdateView, TestDriveBookingUpdateView
from django.urls import path

urlpatterns = [
    path('create-booking', views.booking_create, name="create-booking"),
    path('create-service', views.service_create, name="create-service"),
    path('list-booking', views.booking_list, name="list-booking"),
    path('list-service', views.service_list, name="list-service"),
    path('display-booking/<int:pk>', TestDriveBookingUpdateView.as_view(), name="display-booking"),
    path('display-service/<int:pk>', ServiceRecordUpdateView.as_view(), name="display-service"),
    path('manage-booking/<int:pk>', TestDriveBookingUpdateView.as_view(), name="manage-booking"),
    path('manage-service/<int:pk>', ServiceRecordUpdateView.as_view(), name="manage-service")
]
