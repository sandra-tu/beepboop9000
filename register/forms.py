from django import forms
from .models import Organisation

COUNTRY_CHOICES = [
        ('gb','Great Britain'),
        ('ie', 'Ireland'),
    ]
TYPE_CHOICES = [
    ('pubbar', 'Pub/Bar'),
    ('club', 'Nightclub'),
    ('soc', 'University Society'),
    ('school', 'School'),
    ('office', 'Office'),
    ('store', 'Store'),
    ('other', 'Other'),
]
CITY_CHOICES = [('edi', 'Edinburgh')]

class RegisterForm(forms.Form):
    # class Meta:
    #     model = Organisation
    #     feilds = ('name', 'country', 'city', 'type', 'email')
    name = forms.CharField(max_length=255, required=False)
    country = forms.CharField(label='Country', widget=forms.Select(choices=COUNTRY_CHOICES))
    city = forms.CharField(label='Country', widget=forms.Select(choices=CITY_CHOICES))
    type = forms.CharField(label='Country', widget=forms.Select(choices=TYPE_CHOICES))
    email = forms.CharField(label='Email', max_length=255, required=True)
