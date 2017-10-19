from rest_framework import serializers
from . import models

class RosterSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Roster
		fields = ('id', 'kitchen_lord','shift')

class ShiftPeriodSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.ShiftPeriod
		fields = ('start', 'end')

