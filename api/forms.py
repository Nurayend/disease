from django import forms
from .models import *

class DiseaseForm(forms.ModelForm):
    class Meta:
        model = Disease
        fields = ['disease_code', 'pathogen', 'description']
        widgets = {
            'disease_code': forms.TextInput(attrs={'class': 'form-control'}),
            'pathogen': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'})
        }
