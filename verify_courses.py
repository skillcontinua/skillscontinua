"""
VERIFICATION SCRIPT - Check courses in Category 11
Run with: python verify_courses.py
"""

import os
import sys
import django

# Set up Django environment
sys.path.append('C:\\skillscontinua')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')  # Change 'core.settings' to your actual settings module if different
django.setup()

from courses.models import Course, Category

print("=" * 60)
print("VERIFYING COURSES IN CATEGORY 11")
print("=" * 60)

try:
    category = Category.objects.get(id=11)
    print(f"\nCategory: {category.name}")
    print(f"Category ID: {category.id}")
    print(f"Total courses in this category: {category.courses.count()}")
    
    if category.courses.count() > 0:
        print("\n📚 Courses in this category:")
        print("-" * 60)
        for course in category.courses.all().order_by('id'):
            lesson_count = course.lessons.count()
            print(f"  ✅ ID {course.id}: {course.title}")
            print(f"     Lessons: {lesson_count}")
            print(f"     Active: {course.is_active}")
            print(f"     Level: {course.level}")
            print("-" * 60)
    else:
        print("\n❌ No courses found in this category!")
        
except Category.DoesNotExist:
    print("\n❌ Category with ID 11 does not exist!")
except Exception as e:
    print(f"\n❌ Error: {e}")

print("\n" + "=" * 60)
print("VERIFICATION COMPLETE!")
print("=" * 60)