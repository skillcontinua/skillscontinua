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
print("📚 MANUAL SQL UPDATE")
print("="*70)

# Real content for lesson 3366
new_content = """## Offset Printing Press Types - Complete Guide

Offset printing presses come in three main types: Sheet-Fed, Web, and Hybrid. Each type serves different printing needs and production volumes.

## 1. Sheet-Fed Offset Presses

Sheet-fed offset presses feed individual sheets of paper through the press. They are ideal for:
- Short to medium runs (500-50,000 copies)
- High-quality printing on various paper stocks
- Specialty papers and heavy cardstock
- Variable sheet sizes

**Advantages:**
- Excellent print quality with sharp details
- Versatile paper options
- Quick job changeovers
- Minimal paper waste

**Disadvantages:**
- Slower than web presses
- Higher cost per sheet
- Limited to sheet sizes

## 2. Web Offset Presses

Web offset presses use continuous rolls of paper (webs). They are designed for:
- Long runs (50,000+ copies)
- Newspapers, magazines, and catalogs
- High-speed production
- Cost-effective for large volumes

**Advantages:**
- Very fast production speeds
- Cost-effective for large runs
- Integrated folding and cutting
- Lower paper cost per unit

**Disadvantages:**
- Limited paper stock options
- Higher setup costs
- Not suitable for short runs

## 3. Hybrid Offset Presses

Hybrid offset presses combine offset and digital printing capabilities. They offer:
- Integration of variable data
- On-demand printing capabilities
- Short-run flexibility
- Quality of offset with digital customization

**Advantages:**
- Best of both technologies
- Variable data printing
- Reduced setup time
- Personalized printing

**Disadvantages:**
- Higher equipment costs
- Complex operation
- Specialized training needed

## Choosing the Right Press

When selecting an offset press type, consider:
1. Run length (short, medium, long)
2. Required print quality
3. Paper stock availability
4. Budget constraints
5. Turnaround time requirements

## Key Takeaways
- Sheet-fed: Best for quality and versatility
- Web: Best for high-volume, long runs
- Hybrid: Best for flexibility and personalization
- Choose based on your specific printing needs"""

lesson_id = 3366

with connection.cursor() as cursor:
    # Update all content fields
    cursor.execute("""
        UPDATE courses_lesson 
        SET content = %s, 
            content_en = %s,
            content_fr = %s,
            content_es = %s,
            content_pt = %s,
            content_sw = %s,
            content_ar = %s
        WHERE id = %s
    """, [new_content, new_content, new_content, new_content, new_content, new_content, new_content, lesson_id])
    
    print(f"✅ Updated lesson {lesson_id}")
    
    # Verify
    cursor.execute("SELECT content FROM courses_lesson WHERE id = %s", [lesson_id])
    result = cursor.fetchone()
    print(f"\nVerification - content preview:")
    print(f"{result[0][:200] if result[0] else 'EMPTY'}...")

print("\n" + "="*70)
print("🎉 Manual SQL update complete!")