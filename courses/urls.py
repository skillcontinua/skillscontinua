from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('<int:pk>/', views.course_detail, name='course_detail'),
    path('<int:pk>/enroll/', views.enroll, name='enroll'),
    path('<int:course_pk>/lesson/<int:lesson_pk>/', views.lesson_view, name='lesson_view'),
]