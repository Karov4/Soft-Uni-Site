from django.db import models

from Soft_Uni_Site.apartments.models import Apartment
from Soft_Uni_Site.users.models import CustomUser


class Review(models.Model):
    reviewer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reviews_written')
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField(default=5)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reviewer.username} - {self.apartment.address}"