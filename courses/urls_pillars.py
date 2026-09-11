from django.urls import path
from. import views
urlpatterns = [
    path('', views.pillars_list, name='pillars_list'),
]