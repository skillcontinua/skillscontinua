import pathlib, re
urls_path = pathlib.Path("certifications/urls.py")
views_path = pathlib.Path("certifications/views.py")

print("=== certifications/views.py available functions ===")
if views_path.exists():
    txt = views_path.read_text(encoding='utf-8', errors='ignore')
    funcs = re.findall(r'def (\w+)\(', txt)
    print(funcs)
else:
    print("views.py not found")
    funcs = []

print("\n=== certifications/urls.py current ===")
if urls_path.exists():
    print(urls_path.read_text(encoding='utf-8', errors='ignore')[:1000])

# Create safe urls.py using only what exists
safe_urls = '''from django.urls import path
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
'''

# Write safe version
if urls_path.exists():
    backup = urls_path.with_suffix('.bak.py')
    backup.write_text(urls_path.read_text(encoding='utf-8', errors='ignore'), encoding='utf-8')
    print(f"\nBacked up to {backup}")

urls_path.write_text(safe_urls, encoding='utf-8')
print(f"\nWrote safe {urls_path}")

print("\nNow try: python manage.py migrate --run-syncdb")