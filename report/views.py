# from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import Http404
from django.core.mail import send_mail
from .forms import ReportForm

# class ReportPageView(TemplateView):
#     template_name = "report/report.html"

def report_view(request):
    form = ReportForm()
    send_mail(
        'uhhh',
        'HEY???',
        None,
        ['sandratu2000@gmail.com'],
        fail_silently=False,
    )
    return render(request, 'report/report.html', {'form': form})
