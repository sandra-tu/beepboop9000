# from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.db.models import F
from django.http import Http404
from django.core.mail import send_mail
from .forms import ReportForm
from .models import Report
from register.models import Organisation

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
        loc = Organisation.objects.get(id=request.POST.get('location'))
        t = request.POST.get('time')
        if not t:
            t = None
        new_report = Report.objects.create(
            date = request.POST.get('date'),
            time = t,
            accused_description = request.POST.get('accused_description'),
            event_description = request.POST.get('event_description'),
            name = request.POST.get('name'),
            location = loc
        )
        new_report.save()
        loc.report_count = F('report_count') + 1
        loc.save(update_fields=['report_count'])

    return render(request, 'report/submitted.html', {})
