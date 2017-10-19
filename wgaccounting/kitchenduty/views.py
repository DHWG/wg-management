from rest_framework import viewsets
from . import models, serializers

class RosterViewSet(viewsets.ModelViewSet):
	queryset = models.Roster.objects.all()
	serializer_class = serializers.RosterSerializer


class ShiftPeriodViewSet(viewsets.ModelViewSet):
	queryset = models.ShiftPeriod.objects.all()
	serializer_class = serializers.ShiftPeriodSerializer
