import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','core.settings')
django.setup()
from courses.models import Course, Lesson
from courses.quiz_models import Quiz

print(f"Lessons {Lesson.objects.count()}")

for course in Course.objects.all().order_by('id'):
    for lesson in course.lessons.all().order_by('order'):
        if Quiz.objects.filter(lesson=lesson).count() >= 3:
            continue
        # delete old if partial
        Quiz.objects.filter(lesson=lesson).delete()
        try:
            Quiz.objects.create(lesson=lesson, question=f"What is the first tool needed for {lesson.title[:80]}?", option_a="Correct professional tools with safety", option_b="No tools needed", option_c="Only phone is enough", option_d="Wait for government help", correct='A')
            Quiz.objects.create(lesson=lesson, question=f"How much capital to start {course.title[:60]} in Aba market?", option_a="₦20k-₦50k small start at Ariaria", option_b="₦5 million minimum", option_c="It is free, no capital", option_d="₦0", correct='A')
            Quiz.objects.create(lesson=lesson, question=f"What is the key safety rule for {lesson.title[:60]}?", option_a="Safety first, follow manual, correct handling", option_b="No safety needed", option_c="Rush the work to finish", option_d="Ignore instructions", correct='A')
            print(f"Quiz for Lesson {lesson.id} OK")
        except Exception as e:
            print(f"Error lesson {lesson.id}: {e}")

print("QUIZZES DONE")
total = Quiz.objects.count()
print(f"TOTAL QUIZZES: {total} - should be ~9480 for 3160 lessons x3")