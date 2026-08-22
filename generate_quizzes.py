import os, django, random
os.environ.setdefault('DJANGO_SETTINGS_MODULE','core.settings')
django.setup()
from courses.models import Course, Lesson
from quizzes.models import Quiz, Question, Choice  # adjust if different app name

for course in Course.objects.all():
    print(f"Course {course.id} {course.title}")
    for lesson in course.lessons.all().order_by('order'):
        if hasattr(lesson, 'quizzes') and lesson.quizzes.exists():
            continue
        quiz = Quiz.objects.create(
            lesson=lesson,
            title=f"Quiz: {lesson.title}",
            passing_score=60
        )
        # 5 questions per lesson
        for q in range(1,6):
            question = Question.objects.create(
                quiz=quiz,
                text=f"Question {q} about {lesson.title} - what is the correct step for {course.title} in Nigeria?",
                order=q
            )
            # 1 correct, 3 wrong
            Choice.objects.create(question=question, text="Correct practical step (use right tools, safety first)", is_correct=True)
            Choice.objects.create(question=question, text="Skip safety and use cheap tools", is_correct=False)
            Choice.objects.create(question=question, text="Only theory, no practice", is_correct=False)
            Choice.objects.create(question=question, text="Wait for government job", is_correct=False)
    # final exam per course
    if not course.exams.exists() if hasattr(course,'exams') else True:
        try:
            from exams.models import Exam
            Exam.objects.get_or_create(course=course, defaults=dict(title=f"Final Exam - {course.title}", passing_score=70))
        except:
            pass
print("QUIZZES DONE")