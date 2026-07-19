import os
import sys
from google.cloud import translate_v2 as translate

# Test the translation API
API_KEY = "YOUR_GOOGLE_API_KEY_HERE"  # <-- REPLACE WITH YOUR API KEY

if API_KEY == "YOUR_GOOGLE_API_KEY_HERE":
    print("⚠️ PLEASE SET YOUR GOOGLE API KEY!")
    exit()

translate_client = translate.Client(api_key=API_KEY)

test_text = "SkillsContinua takes every person from where they are to where they want to be."

print("🌍 Testing Translation API...")
print("="*50)
print(f"Original: {test_text}")

for lang_code, lang_name in [('fr', 'French'), ('es', 'Spanish'), ('pt', 'Portuguese'), ('sw', 'Swahili'), ('ar', 'Arabic')]:
    result = translate_client.translate(test_text, target_language=lang_code)
    print(f"\n{lang_name}:")
    print(f"  {result['translatedText']}")

print("\n✅ Translation API is working!")