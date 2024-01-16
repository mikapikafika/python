from django import forms
from .models import DataPoint


class DataPointForm(forms.ModelForm):
    class Meta:
        model = DataPoint
        fields = ['feature1', 'feature2', 'category']
        # Added so that features will be visibly floats
        widgets = {
            'feature1': forms.NumberInput(attrs={'step': '0.01'}),
            'feature2': forms.NumberInput(attrs={'step': '0.01'}),
        }
