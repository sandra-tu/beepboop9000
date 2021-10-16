from django.urls import path
from .views import ViewPageView

urlpatterns = [
  path('view', ViewPageView.as_view(), name='view'),
]
