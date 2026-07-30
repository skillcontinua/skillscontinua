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
print("🔍 SEEING WHAT'S REALLY IN THE DATABASE")
print("="*70)

# Let's find the actual lesson ID for "Offset Printing Press Types"
with connection.cursor() as cursor:
    cursor.execute("""
        SELECT id, title, course_id 
        FROM courses_lesson 
        WHERE title LIKE '%Offset Printing Press Types%'
    """)
    lessons = cursor.fetchall()
    
    print("\n📖 Found lessons:")
    for lesson in lessons:
        print(f"  ID: {lesson[0]}, Title: {lesson[1]}, Course ID: {lesson[2]}")
        
        # Get the content for this lesson
        cursor2 = connection.cursor()
        cursor2.execute("SELECT content FROM courses_lesson WHERE id = %s", [lesson[0]])
        content = cursor2.fetchone()
        
        print(f"  Content preview (first 200 chars):")
        if content and content[0]:
            print(f"  {content[0][:200]}...")
        else:
            print(f"  EMPTY!")
        print()

print("="*70)