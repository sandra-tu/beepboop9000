from django.db import models

from django.conf import settings

class Organisation(models.Model):
    COUNTRY_CHOICES = [
        ('great_britain','Great Britain'),
        ('ireland', 'Ireland'),
    ]
    TYPE_CHOICES = [
        ('pubbar', 'Pub/Bar'),
        ('club', 'Nightclub'),
        ('society', 'University Society'),
        ('school', 'School'),
        ('office', 'Office'),
        ('store', 'Store'),
        ('other', 'Other'),
    ]
    CITY_CHOICES = [
        ('edinburgh', 'Edinburgh'),
        ('dublin', 'Dublin'),
    ]
    name = models.CharField(max_length=150)
    country = models.CharField(max_length=50, choices=COUNTRY_CHOICES)
    city = models.CharField(max_length=50, choices=CITY_CHOICES)
    type = models.CharField(max_length=25, choices=TYPE_CHOICES)
    email = models.EmailField()
    report_count = models.IntegerField(blank=False, null=False, default=0)

    # to prevent spam - allows admin to manually allow an orgnaisation to show
    # verified = models.BooleanField(default=False) 

    class Meta:
        # sort results by name by default when querying DB
        ordering = ['name']
