from rest_framework import serializers
from . import models

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ('id', 'name', 'image', 'unit_price')

class PurchaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Purchase
        fields = ('id', 'date', 'buyer', 'product')