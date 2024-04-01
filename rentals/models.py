# models.py
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    USER_TYPE_CHOICES = (
        ('landlord', 'Landlord'),
        ('tenant', 'Tenant'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)


class Landlord(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # add additional fields here


class Tenant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # add additional fields here


class Apartment(models.Model):
    landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    rent = models.DecimalField(max_digits=7, decimal_places=2)
    # add additional fields here


class Lease(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    # add additional fields here


class Payment(models.Model):
    lease = models.ForeignKey(Lease, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    # add additional fields here

