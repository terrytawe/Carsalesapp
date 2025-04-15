from . import views
from django.urls import path

urlpatterns = [
    path('create-booking', views.bookings_create, name="create-booking")
]
