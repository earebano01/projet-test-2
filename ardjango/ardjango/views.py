from django.shortcuts import render

from rest_framework import viewsets
from .models import TemperatureData
from .serializers import TemperatureDataSerializer

def home(request):
    return render(request, 'ardjango/intro.html')

class TemperatureDataViewSet(viewsets.ModelViewSet):
    queryset = TemperatureData.objects.all()
    serializer_class = TemperatureDataSerializer

def temperature_data_view(request):
    temperature_data = TemperatureData.objects.all()
    return render(request, 'ardjango/temperature_data_table.html', {'temperature_data': temperature_data})