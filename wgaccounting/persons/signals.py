from .models import Expense
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Expense)
def add_from_balance(sender, instance: Expense, **kwargs):
    subject = instance.subject
    subject.balance += instance.amount
    subject.save()