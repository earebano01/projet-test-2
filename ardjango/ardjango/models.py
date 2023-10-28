from django.db import models

class TemperatureData(models.Model):
    humidity = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    celsius = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    fahrenheit = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    hic = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    hif = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    date = models.DateField(auto_now_add=True, null=True)
    time = models.TimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'humidity: {self.humidity}, celsius: {self.celsius}, fahrenheit: {self.fahrenheit}, hic: {self.hic}, hif: {self.fahrenheit}, date: {self.date}, time: {self.time}'
