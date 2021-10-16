from django.views.generic.base import TemplateView

class RegisterPageView(TemplateView):
    template_name = "register/register.html"