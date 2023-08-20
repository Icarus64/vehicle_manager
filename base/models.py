from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
# Create your models here.

#     Vehicle Number (Alpha numeric)
# Vehicle Type (options:- Two, There, Four wheelers)
# Vehicle Model (Text)
# Vehicle Description (Text)
class Vehicle(models.Model):
    VEHICLE_TYPE_CHOICES = [
        ('Two', 'Two Wheeler'),
        ('Three', 'Three Wheeler'),
        ('Four', 'Four Wheeler'),
    ]

    vehicle_number = models.CharField(max_length=20, unique=True)
    vehicle_type = models.CharField(max_length=10, choices=VEHICLE_TYPE_CHOICES)
    vehicle_model = models.CharField(max_length=100)
    vehicle_description = models.TextField()

    def __str__(self):
        return self.vehicle_number
    
    class Meta:
        permissions = [
            ("read_vehicle", "Can view vehicle"),
            ("create_vehicle", "Can create new vehicle"),
            ("update_vehicle", "Can update existing vehicle"),
            ("del_vehicle", "Can delete existing vehicle"),
        ]


        
