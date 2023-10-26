from django.shortcuts import render

from rest_framework import viewsets
from .models import TemperatureData
from .serializers import TemperatureDataSerializer

class TemperatureDataViewSet(viewsets.ModelViewSet):
    queryset = TemperatureData.objects.all()
    serializer_class = TemperatureDataSerializer

def temperature(request):
    return render(request, 'ardjango/temperature_data_table.html')