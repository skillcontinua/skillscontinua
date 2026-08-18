from django.apps import AppConfig
import os

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
    path = os.path.dirname(__file__)