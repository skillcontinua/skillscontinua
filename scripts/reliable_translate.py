import os
import sys
import django
import time
import json
from deep_translator import GoogleTranslator
from deep_translator.exceptions import TooManyRequests

# Add project root to path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from courses.models import Category, Course, Lesson

print("="*70)
print("🌍 RELIABLE TRANSLATION (With Error Handling & Resume)")
print("="*70)

# Progress tracking file
PROGRESS_FILE = 'translation_progress.json'

# Languages to translate to
TARGET_LANGUAGES = {
    'fr': 'french',
    'es': 'spanish',
    'pt': 'portuguese',
    'sw': 'swahili',
    'ar': 'arabic',
}

def load_progress():
    """Load translation progress from file"""
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, 'r') as f:
            return json.load(f)
    return {'categories': [], 'courses': [], 'lessons': []}

def save_progress(progress):
    """Save translation progress to file"""
    with open(PROGRESS_FILE, 'w') as f:
        json.dump(progress, f)

def translate_text(text, target_lang, retries=3):
    """Translate text with retry logic"""
    if not text or len(text.strip()) == 0:
        return text
    
    # Skip if text is too short
    if len(text.strip()) < 3:
        return text
    
    # For very long text, truncate
    if len(text) > 1000:
        text = text[:997] + "..."
    
    for attempt in range(retries):
        try:
            translator = GoogleTranslator(source='auto', target=target_lang)
            translated = translator.translate(text)
            return translated
        except TooManyRequests:
            print(f"    ⏳ Rate limited, waiting 5 seconds...")
            time.sleep(5)
            continue
        except Exception as e:
            if attempt < retries - 1:
                print(f"    ⚠️ Error, retrying in 3 seconds...")
                time.sleep(3)
                continue
            else:
                print(f"    ⚠️ Failed after {retries} attempts: {e}")
                return text
    
    return text

def translate_field(obj, obj_type, obj_id, field_name, target_lang, progress):
    """Translate a specific field with progress tracking"""
    original_text = getattr(obj, field_name)
    if not original_text or len(original_text.strip()) < 3:
        return
    
    # Check if already translated
    translated_field = f"{field_name}_{target_lang}"
    existing = getattr(obj, translated_field, None)
    if existing and len(existing) > 10:
        return
    
    key = f"{obj_type}_{obj_id}_{field_name}_{target_lang}"
    if key in progress.get('done', []):
        return
    
    translated = translate_text(original_text, TARGET_LANGUAGES[target_lang])
    
    if translated:
        setattr(obj, translated_field, translated)
        progress['done'].append(key)
        print(f"    ✅ {target_lang.upper()}: {translated[:50]}...")

print("\n📚 TRANSLATING CATEGORIES...")
print("="*70)

progress = load_progress()
if 'done' not in progress:
    progress['done'] = []

categories = Category.objects.all()
for category in categories:
    print(f"\n📖 {category.name}")
    for lang_code in TARGET_LANGUAGES.keys():
        translate_field(category, 'category', category.id, 'name', lang_code, progress)
        translate_field(category, 'category', category.id, 'description', lang_code, progress)
    category.save()
    save_progress(progress)
    time.sleep(1)  # Delay to avoid rate limiting

print("\n📚 TRANSLATING COURSES...")
print("="*70)

courses = Course.objects.filter(is_active=True)
for course in courses:
    print(f"\n📖 {course.title}")
    for lang_code in TARGET_LANGUAGES.keys():
        translate_field(course, 'course', course.id, 'title', lang_code, progress)
        translate_field(course, 'course', course.id, 'description', lang_code, progress)
    course.save()
    save_progress(progress)
    time.sleep(1)

print("\n📚 TRANSLATING LESSONS...")
print("="*70)

lessons = Lesson.objects.all()
for lesson in lessons:
    print(f"\n📖 {lesson.title}")
    for lang_code in TARGET_LANGUAGES.keys():
        translate_field(lesson, 'lesson', lesson.id, 'title', lang_code, progress)
        translate_field(lesson, 'lesson', lesson.id, 'content', lang_code, progress)
    lesson.save()
    save_progress(progress)
    time.sleep(0.5)

print("\n" + "="*70)
print("🎉 TRANSLATION COMPLETE!")
print("="*70)