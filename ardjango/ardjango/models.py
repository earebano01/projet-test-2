from django.db import models

class TemperatureData(models.Model):
    temperature = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    date = models.DateField(auto_now_add=True, null=True)
    time = models.TimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'Temperature: {self.temperature} °C at {self.timestamp}'
