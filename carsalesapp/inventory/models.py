
import datetime
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
#--------------------------------------------------------------------------------------------------
# Vehicle Category
#--------------------------------------------------------------------------------------------------
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

#--------------------------------------------------------------------------------------------------
# Vehicle Brand
#--------------------------------------------------------------------------------------------------    
class VehicleBrand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

#--------------------------------------------------------------------------------------------------
# Vehicle Model
#--------------------------------------------------------------------------------------------------
class VehicleModel(models.Model):
    name = models.CharField(max_length=50)
    brand = models.ForeignKey(to=VehicleBrand, on_delete=models.CASCADE, verbose_name='brand name')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, verbose_name='category')
    price = models.DecimalField(default=0, decimal_places=2, max_digits=12)
    image = models.ImageField(upload_to='uploads/Models/')
    createdon = models.DateField(default=now)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=12)

    def __str__(self):
        return self.name
    
#--------------------------------------------------------------------------------------------------
# Test-drive booking
#--------------------------------------------------------------------------------------------------
class Booking(models.Model):
    model = models.ForeignKey(to=VehicleModel, on_delete=models.CASCADE)
    customer = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateField(default=now)
    status = models.BooleanField(default=False)
    createdon = models.DateField(default=now)

    def __str__(self):
        return self.model