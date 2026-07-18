import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from courses.models import Course, Lesson

print("Checking for courses with no lessons...")
empty_courses = []

for course in Course.objects.filter(is_active=True):
    if course.lessons.count() == 0:
        empty_courses.append(course.title)

if empty_courses:
    print(f"\n⚠️ Courses with NO lessons ({len(empty_courses)}):")
    for title in empty_courses:
        print(f"  - {title}")
else:
    print("\n✅ All courses have lessons!")

print(f"\n📚 Total Courses: {Course.objects.filter(is_active=True).count()}")
print(f"📖 Total Lessons: {Lesson.objects.count()}")