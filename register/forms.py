from django import forms
from .models import Organisation

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Organisation
        fields = ('name', 'country', 'city', 'type', 'email')
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'Email address to send incident reports to'}),
            
           
        }
        labels = {
            'name': 'Name of your organisation',
            'type': 'Type of organisation',
        }


