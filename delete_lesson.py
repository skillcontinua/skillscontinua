import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skillscontinua_core.settings')
django.setup()

from courses.models import Lesson

lesson = Lesson.objects.get(pk=529)
print(f'Deleting: {lesson.title} (ID:{lesson.pk})')
lesson.delete()
print('Done')

# Confirm remaining lessons
for l in Lesson.objects.filter(course__title='Introduction to Computers').order_by('order'):
    print(f'ID:{l.pk} | Order:{l.order} | {l.title}')