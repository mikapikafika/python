from django.db import models

class DataPoint(models.Model):
    feature1 = models.FloatField()
    feature2 = models.FloatField()
    category = models.IntegerField()
