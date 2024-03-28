from django.db import models
from django.contrib.auth.models import User
from Soft_Uni_Site.users.models import CustomUser


class Apartment(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='owned_apartments')
    address = models.CharField(max_length=255)
    description = models.TextField()
    rent = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    image_url = models.URLField(null=False, blank=False, verbose_name="Image URL:")
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
