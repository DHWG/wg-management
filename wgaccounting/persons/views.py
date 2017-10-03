from rest_framework import viewsets
from . import models, serializers

class InhabitantViewSet(viewsets.ModelViewSet):
    queryset = models.Inhabitant.objects.filter(system_user=False)
    serializer_class = serializers.InhabitantSerializer