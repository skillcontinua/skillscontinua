from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed, name='community-feed'),
    path('create/', views.create_post, name='community-create'),
]