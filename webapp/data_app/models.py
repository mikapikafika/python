from django.db import models


class DataPoint(models.Model):
    height = models.FloatField()
    weight = models.FloatField()
    quality = models.IntegerField()
