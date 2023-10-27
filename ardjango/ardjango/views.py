from django.shortcuts import render

from rest_framework import viewsets
from .models import TemperatureData
from .serializers import TemperatureDataSerializer

def home(request):
    return render(request, 'ardjango/intro.html')

class TemperatureDataViewSet(viewsets.ModelViewSet):
    queryset = TemperatureData.objects.all()
    serializer_class = TemperatureDataSerializer

def temperatureView(request):
    temperature_data = TemperatureData.objects.all()
    return render(request, 'ardjango/temperature.html', {'temperature_data': temperature_data})

def humidityView(request):
    temperature_data = TemperatureData.objects.all()
    return render(request, 'ardjango/humidity.html', {'temperature_data': temperature_data})

def heat_indexView(request):
    temperature_data = TemperatureData.objects.all()
    return render(request, 'ardjango/heat_index.html', {'temperature_data': temperature_data})

def statisticsView(request):
    temperature_data = TemperatureData.objects.all()
    return render(request, 'ardjango/statistics.html', {'temperature_data': temperature_data})