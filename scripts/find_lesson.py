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
print("🔍 FINDING OFFSET PRINTING LESSONS")
print("="*70)

# Find all lessons related to Offset Printing
lessons = Lesson.objects.filter(title__icontains="Offset")
print(f"\nFound {len(lessons)} lessons:")
for lesson in lessons:
    print(f"  ID: {lesson.id}, Title: {lesson.title}")
    print(f"  Course: {lesson.course.title}")
    print(f"  Content preview: {lesson.content[:100] if lesson.content else 'EMPTY'}...")
    print()

# Also check the specific lesson you're viewing
print("\n" + "="*70)
print("📖 CHECKING LESSON CONTENT")
print("="*70)

# Get the lesson you're trying to view (the one with "Offset Printing Press Types")
try:
    lesson = Lesson.objects.get(title="Offset Printing Press Types")
    print(f"Found lesson: {lesson.id} - {lesson.title}")
    print(f"Content length: {len(lesson.content) if lesson.content else 0}")
    print(f"Content starts with: {lesson.content[:200] if lesson.content else 'EMPTY'}...")
except Lesson.DoesNotExist:
    print("Lesson 'Offset Printing Press Types' not found")
    
print("\n" + "="*70)