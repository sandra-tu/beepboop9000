from django.contrib import admin
from .models import Organisation

# Register your models here.
class OrganisationAdmin(Organisation):
    list_display('name', 'country', 'city')
