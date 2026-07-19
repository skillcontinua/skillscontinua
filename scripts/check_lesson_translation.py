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
print("📊 LESSON TRANSLATION STATUS CHECK")
print("="*70)

total_lessons = Lesson.objects.count()
translated_lessons = 0

for lesson in Lesson.objects.all():
    # Check if French translation exists (as a proxy for all translations)
    if lesson.title_fr and len(lesson.title_fr) > 10:
        translated_lessons += 1

print(f"📚 Total Lessons: {total_lessons}")
print(f"✅ Translated: {translated_lessons}")
print(f"⏳ Remaining: {total_lessons - translated_lessons}")

if translated_lessons < total_lessons:
    print("\n💡 Run batch_translate_lessons.py again!")
else:
    print("\n🎉 ALL LESSONS ARE TRANSLATED!")

print("="*70)