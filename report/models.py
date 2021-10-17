from django.db import models

from django.conf import settings

from register.models import Organisation

class Report(models.Model):
    RELATIONSHIP_CHOICES = [
        ('customer', 'Customer'),
        ('employee', 'Employee'),
        ('client', 'Client'),
        ('boss', 'Boss'),
        ('other', 'Other'),
    ]
    
    date = models.DateField()
    time = models.TimeField(blank=True, null=True)
    accused_description = models.CharField(max_length=1000, blank=True)
    location = models.ForeignKey(Organisation, on_delete=models.SET_NULL, null=True, blank=False)
    repeat = models.BooleanField(default=False)
    name = models.CharField(blank=True, max_length=100)
    event_description = models.CharField(max_length=4000, blank=False)
    accused_relationship = models.CharField(choices=RELATIONSHIP_CHOICES, blank=False, max_length=100)
    submitter_relationship = models.CharField(choices=RELATIONSHIP_CHOICES, blank=False, max_length=100)
