from django.urls import path
from . import views

urlpatterns = [
    path('subscribe/', views.subscribe_page, name='village_subscribe'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]