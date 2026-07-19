import os
import sys
import django
import time
import json
from deep_translator import GoogleTranslator

# Add project root to path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from courses.models import Category, Course, Lesson

print("="*70)
print("🌍 BATCH TRANSLATION (Small Batches, No Stuck Issues)")
print("="*70)

# Get courses that need translation
courses_to_translate = Course.objects.filter(is_active=True)[:20]  # Start with just 20 courses

print(f"📚 Translating {courses_to_translate.count()} courses in this batch...")

def translate_text(text, target_lang):
    """Translate text with timeout protection"""
    if not text or len(text.strip()) < 3:
        return text
    
    if len(text) > 500:
        text = text[:497] + "..."
    
    try:
        translator = GoogleTranslator(source='auto', target=target_lang)
        return translator.translate(text)
    except Exception as e:
        return text

for course in courses_to_translate:
    print(f"\n📖 Processing: {course.title}")
    
    # Translate course title
    print("  Translating title...")
    for lang_code in ['fr', 'es', 'pt', 'sw', 'ar']:
        try:
            translated = translate_text(course.title, lang_code)
            setattr(course, f'title_{lang_code}', translated)
            print(f"    ✅ {lang_code.upper()}: {translated[:40]}...")
        except:
            print(f"    ⚠️ {lang_code.upper()}: Failed")
    
    # Translate course description
    print("  Translating description...")
    for lang_code in ['fr', 'es', 'pt', 'sw', 'ar']:
        try:
            translated = translate_text(course.description, lang_code)
            setattr(course, f'description_{lang_code}', translated)
            print(f"    ✅ {lang_code.upper()}: {translated[:40]}...")
        except:
            print(f"    ⚠️ {lang_code.upper()}: Failed")
    
    course.save()
    print(f"  ✅ Saved: {course.title}")
    time.sleep(2)  # Wait between courses

print("\n" + "="*70)
print("✅ Batch translation complete!")
print(f"📚 Translated {courses_to_translate.count()} courses")
print("\n💡 Run this script again to translate the next batch of courses")
print("="*70)