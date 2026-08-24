from django.urls import path
from . import views

urlpatterns = [
    path('verify/<str:code>/', views.verify_certificate, name='verify_certificate'),
]

# Add other routes only if view exists
try:
    if hasattr(views, 'certificate_view'):
        urlpatterns.append(path('view/<int:pk>/', views.certificate_view, name='certificate_view'))
    if hasattr(views, 'my_certificates'):
        urlpatterns.append(path('', views.my_certificates, name='my_certificates'))
    if hasattr(views, 'certificate_detail'):
        urlpatterns.append(path('<int:pk>/', views.certificate_detail, name='certificate_detail'))
    if hasattr(views, 'generate_certificate'):
        urlpatterns.append(path('generate/<int:enrollment_id>/', views.generate_certificate, name='generate_certificate'))
except Exception as e:
    print(f"Dynamic add failed: {e}")
