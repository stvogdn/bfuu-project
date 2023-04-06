# forms.py

from django import forms
from .models import Service, ScriptElements, Speaker

class SpeakerForm(forms.ModelForm):
    class Meta:
        model = Speaker
        fields = ['name', 'biography']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'biography': forms.Textarea(attrs={'class': 'form-control'}),
        }

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['service_date', 'speaker', 'topic', 'description', 'coordinator']
        widgets = {
            'service_date': forms.DateInput(attrs={'class': 'form-control'}),
            'speaker': forms.Select(attrs={'class': 'form-control'}),
            'topic': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'coordinator': forms.Select(attrs={'class': 'form-control'}),
        }

class ScriptElementsForm(forms.ModelForm):
    class Meta:
        model = ScriptElements
        fields = ['service', 'liturgist_name', 'prelude_hymn_number', 'prelude_hymn_name', 'opening_words',
                  'principle_or_source_number', 'principle_or_source', 'principle_or_source_text',
                  'first_hymn_number', 'first_hymn_name', 'meditation_reading', 'metta_singer',
                  'second_hymn_number', 'second_hymn_name', 'readers_names', 'singers_names', 'zoom_host_name',
                  'slide_manager_name', 'shared_plate_partner', 'final_hymn_number', 'final_hymn_name',
                  'circle_round_singer']
        widgets = {'service': forms.Select(attrs={'class': 'form-control'}),
                   'liturgist_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'prelude_hymn_number': forms.NumberInput(attrs={'class': 'form-control'}),
                   'prelude_hymn_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'opening_words': forms.Textarea(attrs={'class': 'form-control'}),
                   'principle_or_source_number': forms.NumberInput(attrs={'class': 'form-control'}),
                   'principle_or_source': forms.TextInput(attrs={'class': 'form-control'}),
                   'principle_or_source_text': forms.Textarea(attrs={'class': 'form-control'}),
                   'first_hymn_number': forms.NumberInput(attrs={'class': 'form-control'}),
                   'first_hymn_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'meditation_reading': forms.Textarea(attrs={'class': 'form-control'}),
                   'metta_singer': forms.TextInput(attrs={'class': 'form-control'}),
                   'second_hymn_number': forms.NumberInput(attrs={'class': 'form-control'}),
                   'second_hymn_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'readers_names': forms.TextInput(attrs={'class': 'form-control'}),
                   'singers_names': forms.TextInput(attrs={'class': 'form-control'}),
                   'zoom_host_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'slide_manager_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'shared_plate_partner': forms.TextInput(attrs={'class': 'form-control'}),
                   'final_hymn_number': forms.NumberInput(attrs={'class': 'form-control'}),
                   'final_hymn_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'circle_round_singer': forms.TextInput(attrs={'class': 'form-control'}),
                   }
        
