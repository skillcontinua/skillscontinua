import os
import sys
import django
import time
from google.cloud import translate_v2 as translate

# Add project root to path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from courses.models import Category, Course, Lesson

print("="*70)
print("🌍 PROFESSIONAL TRANSLATION USING GOOGLE CLOUD API")
print("="*70)

# ============================================================
# CONFIGURATION - SET YOUR API KEY HERE
# ============================================================
API_KEY = "YOUR_GOOGLE_API_KEY_HERE"  # <-- REPLACE WITH YOUR API KEY

if API_KEY == "YOUR_GOOGLE_API_KEY_HERE":
    print("⚠️ PLEASE SET YOUR GOOGLE API KEY IN THE SCRIPT!")
    print("1. Go to: https://console.cloud.google.com/apis/credentials")
    print("2. Create an API Key")
    print("3. Copy the key and replace 'YOUR_GOOGLE_API_KEY_HERE'")
    exit()

# Initialize translation client
translate_client = translate.Client(api_key=API_KEY)

# Languages to translate to
TARGET_LANGUAGES = {
    'fr': 'French',
    'es': 'Spanish',
    'pt': 'Portuguese',
    'sw': 'Swahili',
    'ar': 'Arabic',
}

# ============================================================
# TRANSLATION FUNCTIONS
# ============================================================

def translate_text(text, target_language):
    """Translate text using Google Cloud API"""
    if not text or len(text.strip()) == 0:
        return text
    
    try:
        result = translate_client.translate(text, target_language=target_language)
        return result['translatedText']
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
    
    if existing_translation:
        # Skip if already translated (with more than 10 chars)
        if len(existing_translation) > 10:
            return
    
    # Translate
    translated = translate_text(original_text, target_lang)
    
    # Save translation (truncate if too long)
    if len(translated) > 5000:
        translated = translated[:4997] + "..."
    
    setattr(obj, translated_field, translated)
    print(f"    ✅ {target_lang.upper()}: {translated[:50]}...")

# ============================================================
# TRANSLATE CATEGORIES
# ============================================================
print("\n📚 TRANSLATING CATEGORIES...")
print("="*70)

categories = Category.objects.all()
print(f"Found {categories.count()} categories")

for category in categories:
    print(f"\n📖 {category.name}")
    for lang_code, lang_name in TARGET_LANGUAGES.items():
        translate_field(category, 'name', lang_code)
        translate_field(category, 'description', lang_code)
    category.save()

# ============================================================
# TRANSLATE COURSES
# ============================================================
print("\n\n📚 TRANSLATING COURSES...")
print("="*70)

courses = Course.objects.filter(is_active=True)
print(f"Found {courses.count()} courses")

for course in courses:
    print(f"\n📖 {course.title}")
    for lang_code, lang_name in TARGET_LANGUAGES.items():
        translate_field(course, 'title', lang_code)
        translate_field(course, 'description', lang_code)
        translate_field(course, 'learning_objectives', lang_code)
        translate_field(course, 'prerequisites', lang_code)
        translate_field(course, 'target_audience', lang_code)
    course.save()
    
    # Small delay to avoid rate limiting
    time.sleep(0.2)

# ============================================================
# TRANSLATE LESSONS
# ============================================================
print("\n\n📚 TRANSLATING LESSONS...")
print("="*70)

lessons = Lesson.objects.all()
print(f"Found {lessons.count()} lessons")

for lesson in lessons:
    print(f"\n📖 {lesson.title}")
    for lang_code, lang_name in TARGET_LANGUAGES.items():
        translate_field(lesson, 'title', lang_code)
        translate_field(lesson, 'content', lang_code)
    lesson.save()
    
    # Small delay to avoid rate limiting
    time.sleep(0.2)

# ============================================================
# SUMMARY
# ============================================================
print("\n\n" + "="*70)
print("📊 TRANSLATION SUMMARY")
print("="*70)
print(f"✅ Categories Translated: {categories.count()}")
print(f"✅ Courses Translated: {courses.count()}")
print(f"✅ Lessons Translated: {lessons.count()}")
print(f"✅ Languages: {', '.join(TARGET_LANGUAGES.values())}")

# Show estimated character usage
total_chars = 0
for course in courses:
    total_chars += len(course.title) + len(course.description)
for lesson in lessons:
    total_chars += len(lesson.title) + len(lesson.content)

print(f"\n📊 Estimated Characters Translated: {total_chars:,}")
print(f"📊 Estimated Cost: ${total_chars * 0.00002:.2f} (approx)")
print("\n💡 Google Cloud Translation Free Tier: 500,000 characters/month")
print(f"💡 Your usage: {total_chars:,} characters across 5 languages")

print("\n🎉 Translation complete!")
print("="*70)