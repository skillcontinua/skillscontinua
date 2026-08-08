from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_home, name='home'),
    path('post/<slug:slug>/', views.blog_detail, name='detail'),
    path('category/<slug:slug>/', views.category_view, name='category'),
    path('tag/<slug:slug>/', views.tag_view, name='tag'),
    path('create/', views.create_post, name='create'),
    path('forum/', views.forum_home, name='forum_home'),
    path('forum/topic/<slug:slug>/', views.forum_topic, name='forum_topic'),
    path('forum/create/', views.create_topic, name='create_topic'),
    path('contributors/', views.contributors_list, name='contributors'),
    path('feedback/', views.feedback_submit, name='feedback'),
]