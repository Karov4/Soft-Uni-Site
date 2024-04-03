from django.conf import settings
from django.db import models


class Apartment(models.Model):
    name = models.TextField(default='default_name')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    location = models.TextField()
    image_url = models.URLField(null=False, blank=False, verbose_name="Image URL:", default='default_url')


class Lease(models.Model):
    tenant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
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
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
