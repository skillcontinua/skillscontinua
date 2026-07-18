from django.urls import path
from . import views

app_name = 'certifications'

urlpatterns = [
    path('', views.my_certificates, name='my_certificates'),
    path('<int:pk>/', views.certificate_detail, name='certificate_detail'),
    path('generate/<int:enrollment_id>/', views.generate_certificate, name='generate_certificate'),
    path('download/<int:pk>/', views.download_certificate, name='download'),
    path('share/<int:pk>/', views.share_certificate, name='share'),
    path('verify/<str:verification_code>/', views.verify_certificate, name='verify'),
    path('admin/', views.certificate_list_admin, name='admin_certificates'),
]