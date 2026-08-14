from django.urls import path
from . import views

app_name = 'skills_health'

urlpatterns = [
    path('', views.diagnostic_dashboard, name='diagnostic'),
]