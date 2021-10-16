from django.urls import path
# from .views import RegisterPageView
from .views import register_view, submit_view

urlpatterns = [
  path('register/', register_view, name='register'),
  path('register_submit/', submit_view, name='submit')
]
