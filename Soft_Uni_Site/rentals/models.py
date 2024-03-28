from django.contrib.auth.models import User
from django.db import models

from Soft_Uni_Site.apartments.models import Apartment
from Soft_Uni_Site.users.models import CustomUser


class RentalApplication(models.Model):
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    message = models.TextField()
    applied_at = models.DateTimeField(auto_now_add=True)
