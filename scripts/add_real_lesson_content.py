import os
import sys
import django

# Add project root to path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from courses.models import Course, Lesson

print("="*70)
print("📚 ADDING REAL LESSON CONTENT")
print("="*70)

# Real lesson content for key courses
real_content = {
    # === OFFSET PRINTING ===
    'Offset Printing Press Types': """
Offset printing presses come in three main types, each suited for different applications and production volumes.

## Sheet-Fed Offset Presses
Sheet-fed offset presses feed individual sheets of paper through the press. They are ideal for:
- Short to medium runs (500-50,000 copies)
- High-quality printing on various paper stocks
- Specialty papers and heavy cardstock
- Variable sheet sizes
- Quick job changeovers

**Advantages:**
- Excellent print quality
- Versatility with paper types
- Quick setup for different jobs
- Minimal paper waste

**Disadvantages:**
- Slower than web presses
- Higher labor costs per sheet
- Limited to sheet sizes

## Web Offset Presses
Web offset presses use continuous rolls of paper (webs). They are designed for:
- Long runs (50,000+ copies)
- Newspapers, magazines, and catalogs
- High-speed production
- Cost-effective for large volumes

**Advantages:**
- Very fast production speeds
- Cost-effective for large runs
- Can print both sides simultaneously
- Integrated folding and cutting

**Disadvantages:**
- Limited paper stock options
- Higher setup costs
- More paper waste during setup
- Not suitable for short runs

## Hybrid Offset Presses
Hybrid offset presses combine offset and digital printing capabilities. They offer:
- Integration of variable data
- On-demand printing capabilities
- Short-run flexibility
- Quality of offset with digital customization

**Advantages:**
- Best of both technologies
- Can handle variable data printing
- Reduced setup time
- Quick job changeovers

**Disadvantages:**
- Higher equipment costs
- More complex to operate
- Requires specialized training

## Choosing the Right Press

When selecting an offset press type, consider:
1. Run length (short, medium, long)
2. Required print quality
3. Paper stock availability
4. Budget constraints
5. Turnaround time requirements
6. Post-press finishing needs

For most commercial printers, a combination of sheet-fed and digital presses offers the best flexibility. Large volume printers often add web presses for high-volume jobs.
""",

    'Sculpture - Complete Guide': """
Sculpture is the art of creating three-dimensional forms through carving, modeling, or assembling materials.

## Introduction to Sculpture
Sculpture is one of the oldest art forms, with examples dating back to prehistoric times. It involves the creation of three-dimensional objects from various materials.

## Sculpture Materials
Common sculpture materials include:
- **Clay:** Versatile and easy to work with, ideal for modeling
- **Stone:** Durable, requires carving with chisels
- **Wood:** Warm and organic, works with carving tools
- **Metal:** Strong and durable, can be cast or welded
- **Plaster:** Good for casting and prototypes
- **Bronze:** Classic material for cast sculptures

## Sculpture Techniques
Key sculpture techniques include:
- **Carving:** Removing material to reveal the form
- **Modeling:** Adding material to build up the form
- **Casting:** Pouring material into a mold
- **Construction:** Assembling various materials
- **Welding:** Joining metal pieces together
""",

    'Introduction to Painting': """
Painting is the practice of applying pigment to a surface to create images and express ideas.

## Introduction to Painting
Painting has been practiced for tens of thousands of years, evolving from cave paintings to sophisticated contemporary works.

## Painting Mediums
Common painting mediums include:
- **Oil Paint:** Slow-drying, versatile, rich colors
- **Acrylic Paint:** Fast-drying, water-soluble, versatile
- **Watercolor:** Transparent, delicate, luminous
- **Gouache:** Opaque watercolor, matte finish
- **Tempera:** Egg-based, traditional, durable
- **Encaustic:** Wax-based, ancient technique

## Painting Techniques
Key painting techniques include:
- **Glazing:** Thin, transparent layers
- **Impasto:** Thick, textured application
- **Scumbling:** Thin, semi-transparent layers
- **Washes:** Diluted paint for tonal effects
- **Blending:** Smooth transitions between colors
""",
}

# Add real content to lessons
total_added = 0
total_found = 0

for title, content in real_content.items():
    try:
        lesson = Lesson.objects.get(title=title)
        # Check if the lesson content is still just the template
        if "Lesson Content" in lesson.content or len(lesson.content) < 200:
            # Replace with real content
            lesson.content = content
            lesson.save()
            total_added += 1
            print(f"✅ Added real content to: {title}")
        else:
            print(f"📚 Already has content: {title}")
        total_found += 1
    except Lesson.DoesNotExist:
        print(f"⚠️ Lesson not found: {title}")

print("\n" + "="*70)
print(f"📊 Lessons Updated: {total_added}")
print(f"📚 Lessons Found: {total_found}")
print("🎉 Real lesson content added!")