from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('<int:pk>/', views.course_detail, name='course_detail'),
    path('<int:pk>/enroll/', views.enroll, name='enroll'),
    path('pillar/<slug:pillar_slug>/', views.pillar_courses, name='pillar_courses'),
]