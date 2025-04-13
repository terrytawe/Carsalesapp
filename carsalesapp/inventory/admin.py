from django.contrib import admin
from .models import Category, VehicleBrand,VehicleModel, Booking

# Register your models here.

admin.site.register(Category)
admin.site.register(VehicleBrand)
admin.site.register(VehicleModel)
admin.site.register(Booking)
