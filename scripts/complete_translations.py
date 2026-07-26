import os
import sys
import django
import time
from deep_translator import GoogleTranslator

# Add project root to path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from courses.models import Course, Lesson

print("="*70)
print("🌍 COMPLETE TRANSLATIONS - ALL COURSES & LESSONS")
print("="*70)

# Languages to translate to
TARGET_LANGUAGES = {
    'fr': 'french',
    'es': 'spanish',
    'pt': 'portuguese',
    'sw': 'swahili',
    'ar': 'arabic',
}

def translate_text(text, target_lang):
    """Translate text with error handling"""
    if not text or len(text.strip()) < 3:
        return text
    
    if len(text) > 1000:
        text = text[:997] + "..."
    
    try:
        translator = GoogleTranslator(source='auto', target=target_lang)
        return translator.translate(text)
    except Exception as e:
        print(f"    ⚠️ Error: {e}")
        return text

def translate_field(obj, field_name, target_lang, obj_type):
    """Translate a field with progress tracking"""
    original_text = getattr(obj, field_name)
    if not original_text or len(original_text.strip()) < 3:
        return
    
    translated_field = f"{field_name}_{target_lang}"
    existing = getattr(obj, translated_field, None)
    if existing and len(existing) > 10:
        return
    
    print(f"    Translating {field_name} to {target_lang.upper()}...")
    translated = translate_text(original_text, TARGET_LANGUAGES[target_lang])
    
    if translated:
        setattr(obj, translated_field, translated)
        print(f"    ✅ {target_lang.upper()}: {translated[:50]}...")
    else:
        print(f"    ⚠️ {target_lang.upper()}: Translation failed")

# ============================================================
# TRANSLATE ALL COURSES
# ============================================================
print("\n📚 TRANSLATING COURSES...")
print("="*70)

courses = Course.objects.filter(is_active=True)
print(f"Found {courses.count()} courses")

translated_courses = 0
for course in courses:
    print(f"\n📖 {course.title}")
    translated = False
    
    for lang_code in TARGET_LANGUAGES.keys():
        translate_field(course, 'title', lang_code, 'course')
        translate_field(course, 'description', lang_code, 'course')
        translate_field(course, 'learning_objectives', lang_code, 'course')
        translate_field(course, 'prerequisites', lang_code, 'course')
        translate_field(course, 'target_audience', lang_code, 'course')
    
    course.save()
    translated_courses += 1
    time.sleep(0.5)  # Prevent rate limiting

# ============================================================
# TRANSLATE ALL LESSONS
# ============================================================
print("\n\n📖 TRANSLATING LESSONS...")
print("="*70)

lessons = Lesson.objects.all()
print(f"Found {lessons.count()} lessons")

translated_lessons = 0
for lesson in lessons:
    print(f"\n📖 {lesson.title}")
    translated = False
    
    for lang_code in TARGET_LANGUAGES.keys():
        translate_field(lesson, 'title', lang_code, 'lesson')
        translate_field(lesson, 'content', lang_code, 'lesson')
    
    lesson.save()
    translated_lessons += 1
    time.sleep(0.3)  # Prevent rate limiting

# ============================================================
# SUMMARY
# ============================================================
print("\n" + "="*70)
print("📊 TRANSLATION SUMMARY")
print("="*70)
print(f"✅ Courses Translated: {translated_courses}")
print(f"✅ Lessons Translated: {translated_lessons}")
print("🎉 Translation complete!")
print("="*70)