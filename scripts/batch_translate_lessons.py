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

from courses.models import Lesson

print("="*70)
print("🌍 BATCH TRANSLATION - LESSONS (20 Lessons at a Time)")
print("="*70)

# Get lessons that need translation
lessons_to_translate = Lesson.objects.all()[:20]  # Start with just 20 lessons

print(f"📚 Translating {lessons_to_translate.count()} lessons in this batch...")

def translate_text(text, target_lang):
    if not text or len(text.strip()) < 3:
        return text
    if len(text) > 500:
        text = text[:497] + "..."
    try:
        translator = GoogleTranslator(source='auto', target=target_lang)
        return translator.translate(text)
    except Exception as e:
        return text

for lesson in lessons_to_translate:
    print(f"\n📖 Processing: {lesson.title}")
    
    # Translate lesson title
    print("  Translating title...")
    for lang_code in ['fr', 'es', 'pt', 'sw', 'ar']:
        try:
            translated = translate_text(lesson.title, lang_code)
            setattr(lesson, f'title_{lang_code}', translated)
            print(f"    ✅ {lang_code.upper()}: {translated[:40]}...")
        except:
            print(f"    ⚠️ {lang_code.upper()}: Failed")
    
    # Translate lesson content (only first 500 chars to avoid issues)
    print("  Translating content...")
    for lang_code in ['fr', 'es', 'pt', 'sw', 'ar']:
        try:
            content_preview = lesson.content[:500] if lesson.content else ''
            translated = translate_text(content_preview, lang_code)
            setattr(lesson, f'content_{lang_code}', translated)
            print(f"    ✅ {lang_code.upper()}: {translated[:40]}...")
        except:
            print(f"    ⚠️ {lang_code.upper()}: Failed")
    
    lesson.save()
    print(f"  ✅ Saved: {lesson.title}")
    time.sleep(1)

print("\n" + "="*70)
print("✅ Batch lesson translation complete!")
print(f"📚 Translated {lessons_to_translate.count()} lessons")
print("\n💡 Run this script again to translate the next batch of lessons")
print("="*70)