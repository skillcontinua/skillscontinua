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
print("📚 DIRECT DATABASE UPDATE - BYPASSING ALL CODE")
print("="*70)

# Direct SQL update for lessons
with connection.cursor() as cursor:
    # Check current content for a specific lesson
    cursor.execute("SELECT id, title, content FROM courses_lesson WHERE id = 3366")
    lesson = cursor.fetchone()
    
    if lesson:
        print(f"\n📖 Found lesson: {lesson[1]}")
        print(f"Content preview (first 200 chars): {lesson[2][:200] if lesson[2] else 'None'}")
        
        # Update with real content directly
        new_content = """
## Offset Printing Press Types - Complete Guide

Offset printing presses come in three main types. This guide explains each type in detail.

## 1. Sheet-Fed Offset Presses

Sheet-fed offset presses feed individual sheets of paper through the press. They are used for high-quality printing on various paper types.

**Key Features:**
- Handles different sheet sizes
- Excellent print quality
- Versatile paper options
- Quick job changeovers

**Applications:**
- Brochures and catalogs
- Annual reports
- Art books
- Postcards and greeting cards

**Advantages:**
- Superior print quality
- Wide paper range
- Low waste
- Custom sizes possible

**Disadvantages:**
- Slower than web presses
- Higher per-unit cost for long runs

## 2. Web Offset Presses

Web offset presses use continuous rolls of paper. They are designed for high-volume, long-run printing.

**Key Features:**
- Continuous paper feed
- Very high speed
- Integrated folding and cutting
- Cost-effective for large volumes

**Applications:**
- Newspapers
- Magazines
- Catalogs
- Direct mail

**Advantages:**
- Very fast production
- Lower per-unit cost
- Integrated finishing
- High volume capacity

**Disadvantages:**
- Limited paper options
- High setup costs
- Not for short runs

## 3. Hybrid Offset Presses

Hybrid presses combine offset and digital printing capabilities.

**Key Features:**
- Offset quality with digital flexibility
- Variable data printing
- On-demand capability
- Versatile applications

**Applications:**
- Personalized direct mail
- Variable data catalogs
- Targeted marketing materials

**Advantages:**
- Best of both technologies
- Personalization capability
- Quick changeovers
- Versatile production

**Disadvantages:**
- Higher equipment cost
- Complex operation
- Specialized training needed

## Choosing the Right Press

**Consider:**
1. Run length (short, medium, long)
2. Required print quality
3. Paper stock availability
4. Budget constraints
5. Turnaround time needs

## Summary

- Sheet-fed: Quality and versatility
- Web: Volume and speed
- Hybrid: Flexibility and personalization

Choose the press type that best fits your specific printing needs.
"""
        
        # Update using raw SQL to bypass any save() methods
        cursor.execute("UPDATE courses_lesson SET content = %s WHERE id = %s", [new_content, 3366])
        print(f"\n✅ Updated lesson ID {3366} with real content!")
        
        # Verify the update
        cursor.execute("SELECT content FROM courses_lesson WHERE id = 3366")
        updated = cursor.fetchone()
        print(f"Verification: Content preview - {updated[0][:100] if updated else 'None'}...")
    else:
        print("Lesson 3366 not found")

print("\n" + "="*70)
print("🎉 Direct database update complete!")