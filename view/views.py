from django.views.generic.base import TemplateView
from .models import Organisation

class ViewPageView(TemplateView):
    model = Organisation
    template_name = "view/view.html"