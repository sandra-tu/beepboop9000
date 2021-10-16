# from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import Http404

#
# class RegisterPageView(TemplateView):
#     template_name = "register/register.html"

def register_view(request):
    return render(request, 'register/register.html', {})
