from django import forms
from .models import DataPoint


class DataPointForm(forms.ModelForm):
    feature1 = forms.DecimalField(max_digits=6, decimal_places=2)
    feature2 = forms.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        model = DataPoint
        fields = ['feature1', 'feature2', 'category']

