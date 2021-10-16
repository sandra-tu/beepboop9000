from django.db import models

from django.conf import settings

class Organisation(models.Model):
    COUNTRY_CHOICES = [
        ('gb','United Kingdom'),
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
    name = models.CharField(max_length=150)
    country = models.CharField(max_length=50, choices=COUNTRY_CHOICES)
    city = models.CharField(max_length=50)
    type = models.CharField(max_length=25, choices=TYPE_CHOICES)
    email = models.EmailField()

# Create your models here.
