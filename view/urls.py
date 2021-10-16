from django.urls import path
from .views import view_view

urlpatterns = [
  # path('view', ViewPageView.as_view(), name='view'),
  path('view', view_view, name='view'),
]
