import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skillscontinua_core.settings')
django.setup()

from certifications.models import Quiz, Certificate

print('=== CURRENT QUIZZES ===')
for q in Quiz.objects.all():
    print(f'  {q.course.title} — {q.questions.count()} questions (pass: {q.pass_mark}%)')

print(f'\nTotal quizzes: {Quiz.objects.count()}')
print(f'Total certificates issued: {Certificate.objects.count()}')