# forms.py

from django import forms
from .models import SegmentType, Service

class SegmentTypeForm(forms.ModelForm):
    class Meta:
        model = SegmentType
        fields = ['name', 'description', 'template', 'variables']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'template': forms.Textarea(attrs={'class': 'form-control'}),
            'variables': forms.Textarea(attrs={'class': 'form-control'}),
        }


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['service_date', 'speaker', 'topic', 'description', 'coordinator']
        widgets = {
            'service_date': forms.DateInput(attrs={'class': 'form-control'}),
            'speaker': forms.TextInput(attrs={'class': 'form-control'}),
            'topic': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'coordinator': forms.Select(attrs={'class': 'form-control'}),
        }
