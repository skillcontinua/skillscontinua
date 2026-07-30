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
print("📚 DIRECT DATABASE UPDATE - ALL OFFSET PRINTING LESSONS")
print("="*70)

# Real content for Offset Printing Press Types
real_content = """## Offset Printing Press Types - Complete Guide

Offset printing presses come in three main types: Sheet-Fed, Web, and Hybrid.

## 1. Sheet-Fed Offset Presses

Sheet-fed offset presses feed individual sheets of paper through the press.

**Advantages:**
- Excellent print quality
- Versatile paper options
- Quick job changeovers
- Minimal paper waste

**Disadvantages:**
- Slower than web presses
- Higher cost per sheet

## 2. Web Offset Presses

Web offset presses use continuous rolls of paper.

**Advantages:**
- Very fast production speeds
- Cost-effective for large runs
- Integrated folding and cutting

**Disadvantages:**
- Limited paper options
- High setup costs

## 3. Hybrid Offset Presses

Hybrid presses combine offset and digital printing.

**Advantages:**
- Best of both technologies
- Variable data printing
- Quick changeovers

**Disadvantages:**
- Higher equipment costs
- Complex operation"""

with connection.cursor() as cursor:
    # Update ALL lessons that contain "Offset Printing Press Types"
    cursor.execute("""
        UPDATE courses_lesson 
        SET content = %s,
            content_en = %s,
            content_fr = %s,
            content_es = %s,
            content_pt = %s,
            content_sw = %s,
            content_ar = %s
        WHERE title LIKE '%Offset Printing Press Types%'
    """, [real_content, real_content, real_content, real_content, real_content, real_content, real_content])
    
    print(f"✅ Updated all lessons matching 'Offset Printing Press Types'")

# Verify
with connection.cursor() as cursor:
    cursor.execute("""
        SELECT id, content FROM courses_lesson 
        WHERE title LIKE '%Offset Printing Press Types%'
    """)
    results = cursor.fetchall()
    
    for row in results:
        print(f"\nLesson ID: {row[0]}")
        print(f"Content preview: {row[1][:150] if row[1] else 'EMPTY'}...")

print("\n" + "="*70)
print("🎉 Direct update complete!")