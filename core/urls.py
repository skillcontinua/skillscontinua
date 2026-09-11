from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('en/', views.home, name='home_en'),
    path('en/pillars/', views.pillars_overview, name='pillars_overview'),
    path('en/pillars/<slug:slug>/', views.pillar_detail, name='pillar_detail'),
    path('en/courses/', include('courses.urls')),
    path('en/community/', views.community, name='community'),
    path('en/dashboard/', views.dashboard, name='dashboard'),
]