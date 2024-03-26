from django.contrib.auth.models import User
from django.db import models
from Soft_Uni_Site.apartments.models import Apartment


class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    owned_apartments = models.ManyToManyField(Apartment, related_name="owners")

    def __str__(self):
        return self.user.username

