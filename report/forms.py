from django import forms
from .models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report

        fields = ('date', 'time',  'location', 'accused_description', 'event_description', 'name')
        widgets = {
            'date': forms.TextInput(attrs={'type': 'date'}),
            'time': forms.TextInput(attrs={'type': 'time'}),
            'location': forms.TextInput(attrs={'placeholder': 'Select the organisation this happened in'}),
            'accused_description':forms.Textarea(attrs={'rows': 3, 'cols': 25, 'placeholder':'Describe the perpetrator in any way you feel comfortable'} ),
            'event_description':forms.Textarea(attrs={'rows': 5, 'cols': 25, 'placeholder':'Describe the event as fully as possible'}),
            'name': forms.TextInput(attrs={'placeholder': 'Optional: if you would like us to know who you are'}),
        }
        labels = {
            'accused_description': 'Description of perpetrator',
            'event_description': 'Description of event',
        }
