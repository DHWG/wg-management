from django.db import models
from django.contrib.auth.models import AbstractUser

class Inhabitant(AbstractUser):

    system_user = models.BooleanField(default=False)

    picture = models.ImageField(null=True, blank=True, upload_to='avatars')

    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

class Expense(models.Model):
    '''An expense is a amount of money somebody disbursed for the sake of the WG.'''

    date = models.DateTimeField(auto_now_add=True)

    subject = models.ForeignKey(Inhabitant, on_delete=models.CASCADE, related_name='subject')

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'[Expense of {self.amount}€ from {self.subject.username} @ {self.date}]'