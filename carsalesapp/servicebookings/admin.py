from django.contrib import admin
from .models import CustomerVehicle, ServiceRecord, TestDriveRecord, Review

# Register your models here.

admin.site.register(CustomerVehicle)
admin.site.register(ServiceRecord)
admin.site.register(TestDriveRecord)
admin.site.register(Review)
