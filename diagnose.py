import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skillscontinua_core.settings')
django.setup()

# Check URL configuration
print('Checking URL patterns...')
from django.urls import reverse
try:
    url = reverse('courses:lesson_detail', kwargs={'pk': 1})
    print(f'lesson_detail URL resolves: {url}')
except Exception as e:
    print(f'lesson_detail URL ERROR: {e}')

try:
    url = reverse('courses:course_detail', kwargs={'pk': 1})
    print(f'course_detail URL resolves: {url}')
except Exception as e:
    print(f'course_detail URL ERROR: {e}')

# Check views
print('\nChecking views...')
import courses.views as v
print(dir(v))

# Check urls
print('\nChecking courses/urls.py...')
import courses.urls as u
for pattern in u.urlpatterns:
    print(f'  {pattern}')