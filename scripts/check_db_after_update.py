import os
import sys
import django
from django.db import connection

# Add project root to path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

print("="*70)
print("🔍 CHECK DATABASE AFTER UPDATE")
print("="*70)

lesson_id = 3366

with connection.cursor() as cursor:
    cursor.execute("""
        SELECT id, title, content, content_en 
        FROM courses_lesson 
        WHERE id = %s
    """, [lesson_id])
    
    result = cursor.fetchone()
    
    if result:
        print(f"\n📖 Lesson ID: {result[0]}")
        print(f"Title: {result[1]}")
        print(f"\nContent (main):")
        print(f"{result[2][:500] if result[2] else 'EMPTY'}")
        print(f"\nContent (English translation):")
        print(f"{result[3][:500] if result[3] else 'EMPTY'}")
    else:
        print(f"Lesson {lesson_id} not found")

print("\n" + "="*70)