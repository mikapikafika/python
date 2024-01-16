from rest_framework import serializers
from .models import DataPoint


# To render the DataPoint model as JSON
class DataPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataPoint
        fields = '__all__'
