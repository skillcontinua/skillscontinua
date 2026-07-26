import os
import sys
import django

# Add project root to path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from courses.models import Course, Lesson

print("="*70)
print("🌍 TRANSLATION STATUS CHECK")
print("="*70)

# Check courses
total_courses = Course.objects.filter(is_active=True).count()
translated_courses = 0

for course in Course.objects.filter(is_active=True):
    if course.title_fr and len(course.title_fr) > 10:
        translated_courses += 1

print(f"\n📚 COURSES:")
print(f"  Total: {total_courses}")
print(f"  Translated: {translated_courses}")
print(f"  Remaining: {total_courses - translated_courses}")

# Check lessons
total_lessons = Lesson.objects.count()
translated_lessons = 0

for lesson in Lesson.objects.all():
    if lesson.title_fr and len(lesson.title_fr) > 10:
        translated_lessons += 1

print(f"\n📖 LESSONS:")
print(f"  Total: {total_lessons}")
print(f"  Translated: {translated_lessons}")
print(f"  Remaining: {total_lessons - translated_lessons}")

print("\n" + "="*70)