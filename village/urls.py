from django.urls import path
from . import views

urlpatterns = [
    path('subscribe/', views.subscribe, name='village_subscribe'),
    path('subscribe/success/', views.subscribe_success, name='subscribe_success'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]