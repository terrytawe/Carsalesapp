
import datetime
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
# ────────────────────────────────────────────────────────────────────────────────────────────────
# Vehicle Category
# ────────────────────────────────────────────────────────────────────────────────────────────────
class Category(models.Model):
    name        = models.CharField(max_length=100)
    image       = models.ImageField(upload_to='uploads/Category/')
    description = models.CharField(max_length=255, default='', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
  
# ────────────────────────────────────────────────────────────────────────────────────────────────
# Features
# ────────────────────────────────────────────────────────────────────────────────────────────────

class Feature(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
# ────────────────────────────────────────────────────────────────────────────────────────────────
# Vehicle Brand
# ────────────────────────────────────────────────────────────────────────────────────────────────  
class VehicleBrand(models.Model):
    name        = models.CharField(max_length=255)
    description = models.CharField(max_length=255, default='', blank=True, null=True)

    def __str__(self):
        return self.name
 
    
# ────────────────────────────────────────────────────────────────────────────────────────────────
# Vehicle Model
# ────────────────────────────────────────────────────────────────────────────────────────────────
class VehicleModel(models.Model):
    name        = models.CharField(max_length=50, blank=False, null=False)
    brand       = models.ForeignKey(to=VehicleBrand, on_delete=models.CASCADE, related_name='vehicle_brand')
    category    = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name='vehicle_category')
    price       = models.DecimalField(default=0, decimal_places=2, max_digits=12)
    image       = models.ImageField(upload_to='uploads/Models/')
    createdon   = models.DateField(default=now)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    is_sale     = models.BooleanField(default=False)
    sale_price  = models.DecimalField(default=0, decimal_places=2, max_digits=12)
    features    = models.ManyToManyField(Feature, related_name="vehicle_features", blank=True)

    def __str__(self):
        return self.name
 