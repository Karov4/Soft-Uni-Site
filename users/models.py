from django.db import models
from django.contrib.auth.models import User, AbstractUser, Group, Permission


class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('renter', 'Renter'),
        ('leaser', 'Leaser'),
    )
    age = models.IntegerField(null=True, blank=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, null=True, blank=True)

    def save(self, *args, **kwargs):

        self.is_staff = self.is_superuser or self.user_type == 'leaser'

        super().save(*args, **kwargs)

        if self.user_type == 'renter':
            self.groups.set([Group.objects.get(name='Renters')])
        elif self.user_type == 'leaser':
            self.groups.set([Group.objects.get(name='Leasers')])