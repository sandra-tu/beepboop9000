from django.contrib import admin
from .models import Organisation

@admin.register(Organisation)
class OrganisationAdmin(Organisation):
    list_display = ['name', 'country', 'city']
