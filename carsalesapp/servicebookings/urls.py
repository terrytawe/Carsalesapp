from . import views
from .views import ServiceRecordUpdateView
from django.urls import path

urlpatterns = [
    path('create-booking', views.booking_create, name="create-booking"),
    path('list-booking', views.booking_list, name="list-booking"),
    path('display-booking/<int:id>', views.booking_details, name="display-booking"),
    path('manage-booking/<int:id>', views.booking_manage, name="manage-booking"),
    path('create-service', views.service_create, name="create-service"),
    path('list-service', views.service_list, name="list-service"),
    path('display-service/<int:pk>', ServiceRecordUpdateView.as_view(), name="display-service"),
    path('manage-service/<int:id>', views.service_manage, name="manage-service")
]
