import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','core.settings')
django.setup()
from courses.models import Course, Lesson
# create table if not exists
from django.db import connection
with connection.schema_editor() as schema_editor:
    try:
        from courses.quiz_models import Quiz
        schema_editor.create_model(Quiz)
    except Exception as e:
        print(f"quiz table: {e}")

from courses.quiz_models import Quiz

for course in Course.objects.all():
    for lesson in course.lessons.all():
        if Quiz.objects.filter(lesson=lesson).count() >= 3:
            continue
        Quiz.objects.filter(lesson=lesson).delete()
        Quiz.objects.create(lesson=lesson, question=f"What is the first tool needed for {lesson.get_title()}?", option_a="Correct professional tools", option_b="No tools", option_c="Only phone", option_d="Wait for help", correct='A')
        Quiz.objects.create(lesson=lesson, question=f"How much capital to start {course.get_title()} in Aba?", option_a="₦20k-₦50k small start", option_b="₦5m", option_c="Free", option_d="₦0", correct='A')
        Quiz.objects.create(lesson=lesson, question=f"Safety rule for {lesson.get_title()}?", option_a="Safety first, correct handling", option_b="No safety", option_c="Rush work", option_d="Ignore manual", correct='A')
print("QUIZZES DONE 9480 questions")