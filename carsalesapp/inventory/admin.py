from django.contrib import admin
from .models import Category, Brand, Model, Booking

# Register your models here.

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Booking)
