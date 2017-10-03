from django.contrib import admin
from .models import Product, Purchase

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    pass