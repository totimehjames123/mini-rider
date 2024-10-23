from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password
import re

USER_TYPES = [
    ('driver', 'Driver'),
    ('rider', 'Rider')
]

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    user_type = models.CharField(max_length=225, choices=USER_TYPES, default="driver")
    phoneNumber = models.CharField(max_length=15, unique=True)
    vehicle_make = models.CharField(max_length=50, blank=True, null=True)  # For drivers
    vehicle_model = models.CharField(max_length=50, blank=True, null=True)  # For drivers
    vehicle_year = models.PositiveIntegerField(blank=True, null=True)  
    expo_tokens = models.CharField(max_length=225, blank=False)
    createdAt = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.password:
            self.password = make_password(self.password)
            super().save(*args, **kwargs)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def clean(self):
        if not self.name:
            raise ValidationError({"name": "Name is required!"})
        if not self.email:
            raise ValidationError({"email": "Email is required!"})
        if len(self.password) < 8:
            raise ValidationError({"password": "Password cannot be less than 8!"})
        if not re.search(r'\d', self.password):
            raise ValidationError({"password": "Password must contain at least one digit!"})
        if not self.expo_tokens:
            raise ValidationError({"expo_tokens": "Device token is required"})
        
        if self.user_type == 'driver':
            if not self.vehicle_make or  not self.vehicle_model or not self.vehicle_year: 
                raise ValidationError({"vehicle", "Vehicle information is required for drivers!"})

    def __str__(self):
        return f"{self.name} {self.user_type}"


