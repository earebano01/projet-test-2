from rest_framework import serializers
from .models import HumidityData, CelsiusData, FahrenheitData, HICData, HIFData

class HumidityDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = HumidityData
        fields = '__all__'

class CelsiusDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CelsiusData
        fields = '__all__'

class FahrenheitDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FahrenheitData
        fields = '__all__'

class HICDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = HICData
        fields = '__all__'

class HIFDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = HIFData
        fields = '__all__'
