from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('<int:pk>/', views.course_detail, name='course_detail'),
    path('<int:pk>/enroll/', views.enroll, name='enroll'),
    path('pillar/<slug:pillar_slug>/', views.pillar_courses, name='pillar_courses'),
    path('<int:course_pk>/lesson/<int:pk>/', views.lesson_view, name='lesson_view'),
    path('<int:course_pk>/lesson/<int:pk>/complete/', views.complete_lesson, name='complete_lesson'),
]