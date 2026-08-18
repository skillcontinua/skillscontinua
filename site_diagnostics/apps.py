from django.apps import AppConfig
import os
class SiteDiagnosticsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'site_diagnostics'
    path = os.path.dirname(__file__)
