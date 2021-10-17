# from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import Http404
from django.core.mail import send_mail
from .forms import ReportForm
from .models import Report

# class ReportPageView(TemplateView):
#     template_name = "report/report.html"

def report_view(request):
    form = ReportForm()
    # send_mail(
    #     'uhhh',
    #     'HEY???',
    #     None,
    #     ['sandratu2000@gmail.com'],
    #     fail_silently=False,
    # )
    return render(request, 'report/report.html', {'form': form})

def report_submit_view(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        new_report = Report.objects.create(
            date = request.POST.get('date'),
            time = request.POST.get('time'),
            accused_description = request.POST.get('accused_description'),
            event_description = request.POST.get('event_description'),
            name = request.POST.get('name'),
        )

    return render(request, 'report/submitted.html', {})
