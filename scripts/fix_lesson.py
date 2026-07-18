import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skillscontinua_core.settings')
django.setup()

from courses.models import Lesson

# Find and show all lessons in Introduction to Computers
course_lessons = Lesson.objects.filter(
    course__title='Introduction to Computers'
).order_by('order')

for l in course_lessons:
    print(f'ID:{l.pk} | Order:{l.order} | {l.title} | {l.duration_minutes}min')