from django.urls import path
# from .views import ReportPageView
from .views import report_view, report_submit_view

urlpatterns = [
    path('report', report_view, name='report'),
    path('report_submit', report_submit_view, name='report_submit'),
]
