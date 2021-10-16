# from django.views.generic.base import TemplateView
# from .models import Organisation
from django.shortcuts import render
from django.http import Http404
from register.models import Organisation
#
# class ViewPageView(TemplateView):
#     model = Organisation
#     template_name = "view/view.html"

def view_view(request):
    orgs = Organisation.objects.all()
    return render(request, 'view/view.html', {
        'orgs': orgs,
    })
