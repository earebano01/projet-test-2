from django.shortcuts import render
from rest_framework import viewsets
from .models import HumidityData, CelsiusData, FahrenheitData, HICData, HIFData
from .serializers import HumidityDataSerializer, CelsiusDataSerializer, FahrenheitDataSerializer, HICDataSerializer, HIFDataSerializer

def home(request):
    return render(request, 'ardjango/intro.html')
class HumidityDataViewSet(viewsets.ModelViewSet):
    queryset = HumidityData.objects.all()
    serializer_class = HumidityDataSerializer

def humidityView(request):
    humidity_data = HumidityData.objects.all()
    return render(request, 'ardjango/humidity.html', {'humidity_data': humidity_data})
  
class CelsiusDataViewSet(viewsets.ModelViewSet):
    queryset = CelsiusData.objects.all()
    serializer_class = CelsiusDataSerializer

def celsiusView(request):
    celsius_data = CelsiusData.objects.all()
    return render(request, 'ardjango/celsius.html', {'celsius_data': celsius_data})
  

class FahrenheitDataViewSet(viewsets.ModelViewSet):
    queryset = FahrenheitData.objects.all()
    serializer_class = FahrenheitDataSerializer

def fahrenheitView(request):
    fahrenheit_data = FahrenheitData.objects.all()
    return render(request, 'ardjango/fahrenheit.html', {'fahrenheit_data': fahrenheit_data})

class HicDataViewSet(viewsets.ModelViewSet):
    queryset = HICData.objects.all()
    serializer_class = HICDataSerializer

def HICView(request):
    hic_data = HICData.objects.all()
    return render(request, 'ardjango/hic.html', {'hic_data': hic_data})

class HifDataViewSet(viewsets.ModelViewSet):
    queryset = HIFData.objects.all()
    serializer_class = HIFDataSerializer

def HIFView(request):
    hif_data = HIFData.objects.all()
    return render(request, 'ardjango/hif.html', {'hif_data': hif_data})
    