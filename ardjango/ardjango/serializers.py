from rest_framework import serializers
from .models import TemperatureData 

class TemperatureDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperatureData
        # fields = '__all__'
        fields = ['id', 'temperature', 'date', 'time']
