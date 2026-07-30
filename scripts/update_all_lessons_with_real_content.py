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
print("📚 UPDATING ALL LESSONS WITH REAL CONTENT")
print("="*70)

# Define real content for key lessons
real_content = {
    "Offset Printing Press Types": """## Offset Printing Press Types - Complete Guide

Offset printing presses come in three main types. Each type serves different printing needs and production volumes.

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
- Choose based on your specific printing needs""",
    
    "Offset Printing Basics": """## Offset Printing Basics

Offset printing is a widely used printing technique where the inked image is transferred from a plate to a rubber blanket, then to the printing surface.

## The Basic Process

1. **Plate Making:** The image is created on a printing plate
2. **Inking:** Ink is applied to the plate
3. **Transfer:** The image is transferred to a rubber blanket
4. **Printing:** The image is transferred to paper

## Key Components

- **Printing Plate:** Holds the image
- **Rubber Blanket:** Transfers the image
- **Impression Cylinder:** Presses paper against the blanket
- **Ink Rollers:** Apply ink to the plate
- **Dampening System:** Keeps non-image areas wet

## Quality Factors

- **Registration:** Accurate alignment of colors
- **Color Consistency:** Consistent ink coverage
- **Density:** Proper ink density
- **Dot Gain:** Control of dot spread

## Common Applications

- Brochures and catalogs
- Magazines and newspapers
- Books and manuals
- Packaging and labels

## Key Takeaways

- Offset printing provides high-quality results
- Understanding the process helps in quality control
- Proper maintenance ensures consistent output
- Professional results require proper setup""",
}

with connection.cursor() as cursor:
    total_updated = 0
    for title, content in real_content.items():
        cursor.execute("""
            UPDATE courses_lesson 
            SET content = %s,
                content_en = %s,
                content_fr = %s,
                content_es = %s,
                content_pt = %s,
                content_sw = %s,
                content_ar = %s
            WHERE title = %s
        """, [content, content, content, content, content, content, content, title])
        total_updated += cursor.rowcount
        print(f"✅ Updated: {title}")

print(f"\n📊 Total lessons updated: {total_updated}")
print("🎉 All lessons updated!")