import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skillscontinua_core.settings')
django.setup()

from courses.models import Course

c = Course.objects.get(title='Introduction to Computers')
try:
    print(c.quiz.title, c.quiz.questions.count())
except Exception as e:
    print('NO QUIZ FOUND for this course:', e)