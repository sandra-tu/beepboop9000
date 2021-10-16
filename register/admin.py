from django.contrib import admin
from .models import Organisation

@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'city', 'type', 'email']
