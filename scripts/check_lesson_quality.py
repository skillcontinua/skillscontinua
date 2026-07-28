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
print("🔍 CHECKING LESSON CONTENT QUALITY")
print("="*70)

# Get all lessons
all_lessons = Lesson.objects.all()
print(f"📚 Total Lessons: {all_lessons.count()}")

# Check for generic content
generic_content = []
for lesson in all_lessons:
    content = lesson.content or ""
    # Check if content is generic template
    if "This comprehensive lesson covers the essential concepts" in content:
        generic_content.append(lesson)

print(f"📚 Lessons with generic content: {len(generic_content)}")

if generic_content:
    print("\n📖 Sample of generic lessons:")
    for lesson in generic_content[:10]:
        print(f"  - {lesson.title} (Course: {lesson.course.title})")

print("\n" + "="*70)