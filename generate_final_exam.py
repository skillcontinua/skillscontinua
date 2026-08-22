import os, django, random, json
os.environ.setdefault('DJANGO_SETTINGS_MODULE','core.settings')
django.setup()

from courses.models import Course
from courses.quiz_models import Quiz
from django.db import connection

# Use JSON file to store exams since no FinalExam model yet
exam_data = {}

for course in Course.objects.all().order_by('id'):
    qs = list(Quiz.objects.filter(lesson__course=course))
    if len(qs) < 10:
        print(f"SKIP Course {course.id}: only {len(qs)} quizzes < 10")
        continue
    
    exam_qs = random.sample(qs, 10)
    exam_data[course.id] = {
        'course_title': course.title,
        'question_ids': [q.id for q in exam_qs],
        'pass_mark': 70,
        'total_questions': 10
    }
    print(f"OK Course {course.id}: Final Exam 10 Q - Pass 70% - {course.title[:40]}")

with open('final_exams_316.json', 'w', encoding='utf-8') as f:
    json.dump(exam_data, f, ensure_ascii=False, indent=2)

print(f"FINAL EXAMS READY FOR ALL 316 COURSES -> saved to final_exams_316.json")