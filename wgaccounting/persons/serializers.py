from rest_framework import serializers
from . import models

class InhabitantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Inhabitant
        fields = ('id', 'username', 'picture', 'balance')
