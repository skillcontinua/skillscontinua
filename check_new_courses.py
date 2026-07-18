import os
import sys
import django

project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from courses.models import Course

print("="*60)
print("🔍 CHECKING NEW COURSES")
print("="*60)

new_titles = [
    'Windows OS Complete - Installation and Configuration',
    'macOS Fundamentals - Complete Guide',
    'Linux for Beginners - Ubuntu and Beyond',
    'GIMP - Professional Image Editing (Open Source)',
    'Inkscape - Vector Graphics Design (Open Source)',
    'Music Theory Fundamentals - Complete Guide',
    'African Music and Traditional Instruments',
    'Digital Photography Fundamentals',
    'Video Production and Filming Techniques',
]

found = 0
not_found = 0

for title in new_titles:
    try:
        course = Course.objects.get(title=title)
        print(f"✅ Found: {title} (Category: {course.category.name})")
        found += 1
    except Course.DoesNotExist:
        print(f"❌ Not found: {title}")
        not_found += 1

print("\n" + "="*60)
print(f"Found: {found}")
print(f"Not Found: {not_found}")
print("="*60)