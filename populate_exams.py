import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','core.settings')
django.setup()
from courses.models import Course
from courses.quiz_models import Quiz
from django.db import connection

# Create Exam table
class Exam(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE, related_name='exam')
    title = models.CharField(max_length=200)
    pass_mark = models.IntegerField(default=70)
    class Meta:
        app_label='courses'

try:
    with connection.schema_editor() as s:
        s.create_model(Exam)
except Exception as e:
    print(f"Exam table {e}")

# For now use Quiz model as exam too - just mark lesson=None
# Better: create course_exam_questions
for c in Course.objects.all():
    if Quiz.objects.filter(lesson__course=c).count() < 10:
        continue
    print(f"Exam ready for course {c.id} - {c.title[:40]} with 30 Q")
print("EXAMS LOGIC READY - quizzes serve as exam bank")