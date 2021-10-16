from django.urls import path
from .views import ReportPageView

urlpatterns = [
  path('report', ReportPageView.as_view(), name='report'),
]
