from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.core.validators import MinValueValidator, MaxValueValidator
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
# Vehicle for Test Drive or Service
# ────────────────────────────────────────────────────────────────────────────────────────────────
class CustomerVehicle(models.Model):
    make            = models.CharField(max_length=100)
    model           = models.CharField(max_length=100)
    year            = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(datetime.datetime.now().year)]
    )
    license_plate   = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.license_plate} - {self.make} {self.model}"


# ────────────────────────────────────────────────────────────────────────────────────────────────
# Customer Service 
# ────────────────────────────────────────────────────────────────────────────────────────────────
class ServiceRecord(models.Model):
    vehicle          = models.ForeignKey(CustomerVehicle, on_delete=models.CASCADE, related_name='services_received')
    service_type     = models.CharField(max_length=50)
    description      = models.TextField(blank=True, null=True)
    status           = models.CharField(
                        max_length=20,
                        choices=Status.choices,
                        default=Status.PENDING,
    )
    created_by       = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='services_created')
    created_on       = models.DateTimeField(default=now)
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='services_managed')
    last_modified_on = models.DateTimeField(auto_now=True)
    completed_on     = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.vehicle.license_plate} - {self.service_type} ({self.status})"