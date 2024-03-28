from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    RENTER = 'R'
    OWNER = 'O'
    USER_ROLES = [
        (RENTER, 'Renter'),
        (OWNER, 'Apartment Owner'),
    ]
    role = models.CharField(max_length=1, choices=USER_ROLES)

    # Provide unique related_name arguments for groups and user_permissions
    # to resolve clashes with the auth.User model
    groups = models.ManyToManyField('auth.Group', verbose_name=_('groups'), blank=True, related_name='customuser_set')
    user_permissions = models.ManyToManyField('auth.Permission', verbose_name=_('user permissions'), blank=True, related_name='customuser_set')