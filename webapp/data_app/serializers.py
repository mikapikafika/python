from rest_framework import serializers
from .models import DataPoint


class DataPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataPoint
        fields = ['id', 'feature1', 'feature2', 'category']