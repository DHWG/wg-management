from rest_framework import serializers
from . import models

class InhabitantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Inhabitant
        fields = ('id', 'username', 'picture', 'balance')

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Expense
        fields = ('id', 'date', 'subject', 'amount')