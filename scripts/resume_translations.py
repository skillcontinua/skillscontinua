import os
import sys
import django
import time
import json

# Add project root to path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from courses.models import Course, Lesson  # Add this import

# Try to import translator, handle if not installed
try:
    from deep_translator import GoogleTranslator
    TRANSLATOR_AVAILABLE = True
except ImportError:
    TRANSLATOR_AVAILABLE = False
    print("⚠️ deep_translator not installed. Install with: pip install deep-translator")

print("="*70)
print("🌍 RESUMING TRANSLATIONS - SAVING PROGRESS")
print("="*70)

if not TRANSLATOR_AVAILABLE:
    print("❌ Translation library not available. Exiting.")
    sys.exit(1)

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
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, 'r') as f:
            return json.load(f)
    return {'courses': [], 'lessons': []}

def save_progress(progress):
    with open(PROGRESS_FILE, 'w') as f:
        json.dump(progress, f)

def translate_text(text, target_lang):
    if not text or len(text.strip()) < 3:
        return text
    if len(text) > 1000:
        text = text[:997] + "..."
    try:
        translator = GoogleTranslator(source='auto', target=target_lang)
        return translator.translate(text)
    except Exception as e:
        print(f"    ⚠️ Translation error: {e}")
        return text

progress = load_progress()

# Translate Courses
print("\n📚 Translating Courses...")
courses = Course.objects.filter(is_active=True)
course_count = 0

for course in courses:
    if str(course.id) in progress['courses']:
        print(f"⏭️ Skipping: {course.title}")
        continue
    
    print(f"📖 Translating: {course.title}")
    for lang_code, lang_name in TARGET_LANGUAGES.items():
        # Translate title
        translated = translate_text(course.title, lang_name)
        setattr(course, f'title_{lang_code}', translated)
        # Translate description
        if course.description:
            translated = translate_text(course.description, lang_name)
            setattr(course, f'description_{lang_code}', translated)
    
    course.save()
    progress['courses'].append(str(course.id))
    save_progress(progress)
    course_count += 1
    print(f"✅ Saved: {course.title}")
    time.sleep(0.5)

print(f"\n✅ Translated {course_count} courses")

# Translate Lessons
print("\n📖 Translating Lessons...")
lessons = Lesson.objects.all()
lesson_count = 0

for lesson in lessons:
    if str(lesson.id) in progress['lessons']:
        continue
    
    print(f"📖 Translating: {lesson.title}")
    for lang_code, lang_name in TARGET_LANGUAGES.items():
        if lesson.title:
            translated = translate_text(lesson.title, lang_name)
            setattr(lesson, f'title_{lang_code}', translated)
        if lesson.content:
            translated = translate_text(lesson.content[:500], lang_name)
            setattr(lesson, f'content_{lang_code}', translated)
    
    lesson.save()
    progress['lessons'].append(str(lesson.id))
    save_progress(progress)
    lesson_count += 1
    print(f"✅ Saved: {lesson.title}")
    time.sleep(0.3)

print(f"\n✅ Translated {lesson_count} lessons")
print("\n🎉 Translation completed!")