from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.postal_code}"


class Apartment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    description = models.TextField()
    image_url = models.URLField(null=False, blank=False, verbose_name="Image URL:")
    rent_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Apartment at {self.address}"