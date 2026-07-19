import os
import sys
import django

# Add project root to path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from courses.models import Course

print("="*70)
print("📊 TRANSLATION STATUS CHECK")
print("="*70)

total_courses = Course.objects.filter(is_active=True).count()
translated_courses = 0

for course in Course.objects.filter(is_active=True):
    # Check if French translation exists (as a proxy for all translations)
    if course.title_fr and len(course.title_fr) > 10:
        translated_courses += 1

print(f"📚 Total Courses: {total_courses}")
print(f"✅ Translated: {translated_courses}")
print(f"⏳ Remaining: {total_courses - translated_courses}")

if translated_courses < total_courses:
    print("\n💡 Run batch_translate.py again to translate the next batch!")
else:
    print("\n🎉 ALL COURSES ARE TRANSLATED!")

print("="*70)