from django.db import models

from Soft_Uni_Site.apartments.models import Apartment
from Soft_Uni_Site.users.models import CustomUser


class Booking(models.Model):
    renter = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='bookings')
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='bookings')
    start_date = models.DateField()
    end_date = models.DateField()
