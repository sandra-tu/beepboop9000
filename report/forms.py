from django import forms
from .models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report

        fields = ('date', 'time', 'event_description', 'accused_description', 'name')
        widgets = {
            'date': forms.TextInput(attrs={'type': 'date'})
        }
