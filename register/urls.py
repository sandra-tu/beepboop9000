from django.urls import path
# from .views import RegisterPageView
from .views import register_view

urlpatterns = [
  path('register', register_view, name='register'),
]
