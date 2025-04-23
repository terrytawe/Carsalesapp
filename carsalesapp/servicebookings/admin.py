from django.contrib import admin
from .models import CustomerVehicle, ServiceRecord, TestDriveRecord, Review, ServiceType

# Register your models here.

admin.site.register(CustomerVehicle)
admin.site.register(TestDriveRecord)
admin.site.register(ServiceRecord)
admin.site.register(ServiceType)
admin.site.register(Review)
