from django.db import models
from django.contrib.auth.models import User


class Location(models.Model):
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)


class Apartment(models.Model):
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)


class Lease(models.Model):
    tenant = models.ForeignKey(User, on_delete=models.CASCADE)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()


class Review(models.Model):
    rating = models.IntegerField()
    comment = models.TextField()
    lease = models.ForeignKey(Lease, on_delete=models.CASCADE)
    date = models.DateField()


