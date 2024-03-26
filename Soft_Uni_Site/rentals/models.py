from django.contrib.auth.models import User
from django.db import models

from Soft_Uni_Site.apartments.models import Apartment


class Rental(models.Model):
    renter = models.ForeignKey(User, on_delete=models.CASCADE)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Rental for {self.apartment} by {self.renter}"


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(default=5)
    comment = models.TextField()

    def __str__(self):
        return f"Review for {self.apartment} by {self.user}"