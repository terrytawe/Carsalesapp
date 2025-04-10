from . import views
from django.urls import path

urlpatterns = [
    path('', views.bookings, name="bookings")
]
