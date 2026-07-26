import os
import sys
import django

# Add project root to path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from courses.models import Lesson

print("="*70)
print("🔍 CHECKING LESSONS WITH MISSING CONTENT")
print("="*70)

# Get all lessons
all_lessons = Lesson.objects.all()
print(f"📚 Total Lessons: {all_lessons.count()}")

# Find lessons with minimal content
missing_content = []
for lesson in all_lessons:
    content = lesson.content or ""
    # Check if content is too short or just a template
    if len(content) < 200 or "Learning Objectives" in content:
        missing_content.append(lesson)

print(f"📚 Lessons with missing content: {len(missing_content)}")

# Show first 20 missing lessons
print("\n📖 Sample of lessons needing content:")
for lesson in missing_content[:20]:
    print(f"  - {lesson.title} (Course: {lesson.course.title})")

print("\n" + "="*70)