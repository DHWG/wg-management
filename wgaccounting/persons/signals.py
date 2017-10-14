from .models import Expense, Inhabitant
from django.contrib.auth.signals import user_logged_in
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(user_logged_in)
def on_login(sender, user, request, **kwargs):
    user_model = Inhabitant.objects.get_by_natural_key(user)
    print('LOGIN', user_model, type(user_model))

@receiver(post_save, sender=Expense)
def add_from_balance(sender, instance: Expense, **kwargs):
    subject = instance.subject
    subject.balance += instance.amount
    subject.save()