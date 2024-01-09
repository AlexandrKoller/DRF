from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150, blank=True)


class Measurement(models.Model):
    id_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    temperature = models.FloatField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)
