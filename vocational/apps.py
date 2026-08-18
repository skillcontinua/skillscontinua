from django.apps import AppConfig
import os
class VocationalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vocational'
    path = os.path.dirname(__file__)
