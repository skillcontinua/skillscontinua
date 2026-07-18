import os
import sys
import django

project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from courses.models import Category, Course

print("="*60)
print("📊 CATEGORIES AND COURSE COUNTS")
print("="*60)

for cat in Category.objects.all():
    count = Course.objects.filter(category=cat, is_active=True).count()
    print(f"  {cat.name}: {count} courses")

print("\n" + "="*60)
active = Course.objects.filter(is_active=True).count()
total = Course.objects.count()
print(f"Active Courses: {active}")
print(f"Total Courses: {total}")
print("="*60)