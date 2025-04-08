from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#
#--------------------------------------------------------------------------------------------------
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20, default='', blank=True, null=True)
    address = models.CharField(max_length=255, default='', blank=True, null=True)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{ self.first_name } { self.last_name }'