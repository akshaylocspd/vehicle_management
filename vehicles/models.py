from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User

class Vehicle(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    owner_name = models.CharField(max_length=100,default=None,null=True)
    address = models.TextField(default=None,null=True)
    mobile_number = models.CharField(max_length=15,default=None,null=True)
    email = models.EmailField(default=None,null=True)
    registration_number = models.CharField(max_length=100, unique=True)
    model = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    registered_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.registration_number


class Chalan(models.Model):
    VEHICLE_CLASSES = [
        ('motorcycle/scooter', 'Motorcycle/Scooter'),
        ('car', 'Car'),
    ]
    
    VIOLATOR_TYPES = [
        ('owner', 'Owner'),
    ]

    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    issued_on = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    location = models.CharField(max_length=100,default=None,null=True)
    vehicle_class = models.CharField(max_length=20, choices=VEHICLE_CLASSES,default=None,null=True)
    violator_type = models.CharField(max_length=20, choices=VIOLATOR_TYPES,default=None,null=True)
    offence_committed = models.TextField(default=None,null=True)

    def __str__(self):
        return f"{self.vehicle.registration_number} - {self.amount}"