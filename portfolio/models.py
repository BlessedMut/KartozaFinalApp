from django.contrib.auth.models import AbstractUser
from django.db import models


class Profiles(AbstractUser):
    """
    This model class extends the built-in user model from django auth
    """
    address = models.TextField(blank=False, null=False)
    phone = models.CharField(blank=False, max_length=15, null=False)
    lat = models.DecimalField(max_digits=11, decimal_places=11, blank=True, null=True)
    lon = models.DecimalField(max_digits=11, decimal_places=11, blank=True, null=True)
