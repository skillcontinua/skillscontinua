import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skillscontinua_core.settings')
django.setup()

from courses.models import Course, Lesson

# First let us see the exact course titles in the database
print("ALL COURSES IN DATABASE:")
for c in Course.objects.all().order_by('title'):
    print(f'  "{c.title}" - {c.lessons.count()} lessons')