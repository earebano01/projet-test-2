from rest_framework import viewsets
from .models import TemperatureData
from .serializers import TemperatureDataSerializer

class TemperatureDataViewSet(viewsets.ModelViewSet):
    queryset = TemperatureData.objects.all()
    serializer_class = TemperatureDataSerializer
