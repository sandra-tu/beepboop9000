from django.db import models

from django.conf import settings

class Report(models.Model):
    RELATIONSHIP_CHOICES = [
        ('customer', 'Customer'),
        ('employee', 'Employee'),
        ('client', 'Client'),
        ('boss', 'Boss')
    ]
    date = models.DateField()
    time = models.TimeField(blank=True)
    accused_description = models.CharField(max_length=1000, blank=True)
    location = models.CharField(blank=True, max_length=200)
    repeat = models.BooleanField(default=False)
    name = models.CharField(blank=True, max_length=100)
    accused_relationship = models.CharField(choices=RELATIONSHIP_CHOICES, blank=False, max_length=100)
    submitter_relationship = models.CharField(choices=RELATIONSHIP_CHOICES, blank=False, max_length=100)
