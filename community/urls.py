from django.urls import path
from. import views

urlpatterns = [
    path('', views.feed, name='community-feed'),
    path('create/', views.create_post, name='community-create'),
    path('<int:pk>/like/', views.like_post, name='community-like'),
    path('<int:pk>/comment/', views.add_comment, name='community-comment'),
]