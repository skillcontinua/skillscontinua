from django.apps import AppConfig
import os
class CertificationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'certifications'
    path = os.path.dirname(__file__)
