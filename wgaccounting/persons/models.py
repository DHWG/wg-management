from django.db import models
from django.contrib.auth.models import AbstractUser

class Inhabitant(AbstractUser):

    picture = models.ImageField(null=True, blank=True, upload_to='avatars')

    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)