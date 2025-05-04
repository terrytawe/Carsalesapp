from django.contrib import admin
from .models import (
    CustomerVehicle,
    ServiceRecord,
    TestDriveRecord,
    Review,
    ServiceType,
)

@admin.register(CustomerVehicle)
class CustomerVehicleAdmin(admin.ModelAdmin):
    pass

@admin.register(TestDriveRecord)
class TestDriveRecordAdmin(admin.ModelAdmin):
    readonly_fields = ('requested_by',)

@admin.register(ServiceRecord)
class ServiceRecordAdmin(admin.ModelAdmin):
    readonly_fields = ('created_by',)

@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass