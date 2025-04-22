from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from inventory.models import VehicleModel
import datetime

# ────────────────────────────────────────────────────────────────────────────────────────────────
# Service & Booking Status Model
# ────────────────────────────────────────────────────────────────────────────────────────────────
class Status(models.TextChoices):
    PENDING         = 'PENDING', 'Pending'
    IN_PROGRESS     = 'IN_PROGRESS', 'In Progress'
    COMPLETED       = 'COMPLETED', 'Completed'
    CANCELLED       = 'CANCELLED', 'Cancelled'

# ────────────────────────────────────────────────────────────────────────────────────────────────
# Service types
# ────────────────────────────────────────────────────────────────────────────────────────────────
class ServiceType(models.Model):
    name            = models.CharField(max_length=100, null=False, blank=False)
    description     = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"
    

# ────────────────────────────────────────────────────────────────────────────────────────────────
# Vehicle for Test Drive or Service
# ────────────────────────────────────────────────────────────────────────────────────────────────
class CustomerVehicle(models.Model):
    make            = models.CharField(max_length=100)
    model           = models.CharField(max_length=100)
    year            = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(datetime.datetime.now().year)]
    )
    license_plate   = models.CharField(max_length=10, unique=True)
    owner           = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='owned_by')

    def __str__(self):
        return f"{self.license_plate} - {self.make} {self.model}"


# ────────────────────────────────────────────────────────────────────────────────────────────────
# Customer Service 
# ────────────────────────────────────────────────────────────────────────────────────────────────
class ServiceRecord(models.Model):
    vehicle          = models.ForeignKey(CustomerVehicle, on_delete=models.CASCADE, related_name='services_received')
    service_type     = models.ForeignKey(ServiceType, on_delete=models.CASCADE, related_name='service_type')
    description      = models.TextField(blank=True, null=True)
    status           = models.CharField(
                        max_length=20,
                        choices=Status.choices,
                        default=Status.PENDING,
    )
    service_date     = models.DateField(blank=True, null=True)
    created_by       = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='services_created')
    created_on       = models.DateTimeField(default=now)
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='services_managed')
    last_modified_on = models.DateTimeField(auto_now=True)
    service_notes    = models.TextField(blank=True, null=True)
    completed_on     = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.vehicle.license_plate} - {self.service_type.name} ({self.status})"
    


# ────────────────────────────────────────────────────────────────────────────────────────────────
# Test Drive Service 
# ────────────────────────────────────────────────────────────────────────────────────────────────
class TestDriveRecord(models.Model):
    vehicle          = models.ForeignKey(VehicleModel, on_delete=models.CASCADE, related_name='tests_driven')
    description      = models.TextField(blank=True, null=True)
    status           = models.CharField(
                        max_length=20,
                        choices=Status.choices,
                        default=Status.PENDING,
    )
    requested_by     = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='requests_created')
    requested_on     = models.DateTimeField(default=now)
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='requests_managed')
    last_modified_on = models.DateTimeField(auto_now=True)
    completed_on     = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.vehicle.vin_number} - ({self.status})"
    
# ────────────────────────────────────────────────────────────────────────────────────────────────
# Review Record
# ────────────────────────────────────────────────────────────────────────────────────────────────
class Review(models.Model):
    created_by      = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='reviews_created')
    created_on      = models.DateTimeField(auto_now_add=True)
    stars           = models.PositiveSmallIntegerField(
                        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    description     = models.TextField(blank=True, null=True)
    is_visible      = models.BooleanField(default=False)
    moderated_by    = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="reviews_moderated")

    # Generic relation to either ServiceRecord or TestDriveRecord
    content_type    = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id       = models.PositiveIntegerField()
    content_object  = GenericForeignKey('content_type', 'object_id')

    

    def __str__(self):
        return f"{self.user} - {self.stars}★ - {self.content_object}"