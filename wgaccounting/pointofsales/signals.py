from .models import Purchase
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Purchase)
def deduct_from_balance(sender, instance: Purchase, **kwargs):
    buyer = instance.buyer
    product = instance.product
    buyer.balance -= product.unit_price
    buyer.save()