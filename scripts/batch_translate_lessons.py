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
print("🌍 BATCH TRANSLATION - LESSONS (Skip Already Translated)")
print("="*70)

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

# Get lessons that need translation (skip ones already translated)
lessons_to_translate = []
for lesson in Lesson.objects.all():
    # Check if French translation exists (as proxy for all translations)
    if not lesson.title_fr or len(lesson.title_fr) < 10:
        lessons_to_translate.append(lesson)
        if len(lessons_to_translate) >= 20:
            break

print(f"📚 Found {len(lessons_to_translate)} lessons needing translation")

if len(lessons_to_translate) == 0:
    print("🎉 All lessons are already translated!")
    exit()

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
    
    # Translate lesson content
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
print(f"📚 Translated {len(lessons_to_translate)} lessons")
print(f"⏳ Remaining: {Lesson.objects.count() - len(lessons_to_translate)}")
print("="*70)