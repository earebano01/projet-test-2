from django.db import models

class HumidityData(models.Model):
    humidity = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    date = models.DateField(auto_now_add=True, null=True)
    time = models.TimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'humidity: {self.humidity}, date: {self.date}, time: {self.time}'

class CelsiusData(models.Model):
    celsius = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    date = models.DateField(auto_now_add=True, null=True)
    time = models.TimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'celsius: {self.celsius}, date: {self.date}, time: {self.time}'


class FahrenheitData(models.Model):
    fahrenheit = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    date = models.DateField(auto_now_add=True, null=True)
    time = models.TimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'fahrenheit: {self.fahrenheit}, date: {self.date}, time: {self.time}'

class HICData(models.Model):
    hic = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    date = models.DateField(auto_now_add=True, null=True)
    time = models.TimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'hic: {self.hic}, date: {self.date}, time: {self.time}'

class HIFData(models.Model):
    hif = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    date = models.DateField(auto_now_add=True, null=True)
    time = models.TimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'hif: {self.hif}, date: {self.date}, time: {self.time}'
