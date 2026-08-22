import os, django, random
os.environ.setdefault('DJANGO_SETTINGS_MODULE','core.settings')
django.setup()

from courses.models import Course, Lesson
from courses.quiz_models import Quiz

for course in Course.objects.all():
    print(f"Course {course.id} {course.title}")
    for lesson in Lesson.objects.filter(course=course).order_by('id'):
        if Quiz.objects.filter(lesson=lesson).exists():
            continue
        
        # create 10 quizzes per lesson so final exam has 10 Q to sample
        for q in range(1, 11):
            Quiz.objects.create(
                lesson=lesson,
                question=f"Q{q}: What is the correct step for {lesson.title} in {course.title}?",
                option_a="Correct practical step - safety first",
                option_b="Skip safety and use cheap tools", 
                option_c="Only theory, no practice",
                option_d="Wait for government job",
                correct="A"
            )
        print(f"  Created 10 quizzes for Lesson {lesson.id}")

print("QUIZZES DONE")