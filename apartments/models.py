from django.db import models
from django.contrib.auth.models import User


class Apartment(models.Model):
    name = models.TextField(default='default_name')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.TextField()
    image_url = models.URLField(null=False, blank=False, verbose_name="Image URL:", default='default_url')


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


class Favorite(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

