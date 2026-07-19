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

from courses.models import Category, Course, Lesson

print("="*70)
print("🌍 FREE OFFLINE TRANSLATION (No API Key Required)")
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
    """Translate text using free Google Translate (no API key)"""
    if not text or len(text.strip()) == 0:
        return text
    
    try:
        translator = GoogleTranslator(source='auto', target=target_lang)
        translated = translator.translate(text)
        return translated
    except Exception as e:
        print(f"  ⚠️ Translation error: {e}")
        return text

def translate_field(obj, field_name, target_lang):
    """Translate a specific field of a model"""
    original_text = getattr(obj, field_name)
    if not original_text:
        return
    
    # Check if translation already exists
    translated_field = f"{field_name}_{target_lang}"
    existing_translation = getattr(obj, translated_field, None)
    
    if existing_translation and len(existing_translation) > 10:
        return
    
    # Translate (truncate if too long for free API)
    if len(original_text) > 2000:
        original_text = original_text[:1997] + "..."
    
    translated = translate_text(original_text, TARGET_LANGUAGES[target_lang])
    
    if translated and len(translated) > 5000:
        translated = translated[:4997] + "..."
    
    setattr(obj, translated_field, translated)
    print(f"    ✅ {target_lang.upper()}: {translated[:60]}...")

print("\n📚 TRANSLATING CATEGORIES...")
print("="*70)

categories = Category.objects.all()
for category in categories:
    print(f"\n📖 {category.name}")
    for lang_code in TARGET_LANGUAGES.keys():
        translate_field(category, 'name', lang_code)
        translate_field(category, 'description', lang_code)
    category.save()
    time.sleep(0.5)  # Avoid rate limiting

print("\n📚 TRANSLATING COURSES...")
print("="*70)

courses = Course.objects.filter(is_active=True)
for course in courses:
    print(f"\n📖 {course.title}")
    for lang_code in TARGET_LANGUAGES.keys():
        translate_field(course, 'title', lang_code)
        translate_field(course, 'description', lang_code)
    course.save()
    time.sleep(0.5)

print("\n📚 TRANSLATING LESSONS...")
print("="*70)

lessons = Lesson.objects.all()
for lesson in lessons:
    print(f"\n📖 {lesson.title}")
    for lang_code in TARGET_LANGUAGES.keys():
        translate_field(lesson, 'title', lang_code)
        translate_field(lesson, 'content', lang_code)
    lesson.save()
    time.sleep(0.3)

print("\n" + "="*70)
print("🎉 TRANSLATION COMPLETE!")
print("="*70)