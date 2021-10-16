from django.views.generic.base import TemplateView

class ReportPageView(TemplateView):
    template_name = "report/report.html"