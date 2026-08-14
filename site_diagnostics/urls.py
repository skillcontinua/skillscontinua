from django.urls import path
from . import views

app_name = 'site_diagnostics'

urlpatterns = [
    path('', views.diagnostic_dashboard, name='diagnostic'),
    path('api/check-template/', views.check_template, name='check_template'),
    path('api/check-url/', views.check_url, name='check_url'),
    path('api/check-database/', views.check_database, name='check_database'),
]