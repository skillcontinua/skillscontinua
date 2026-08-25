import os, django, random
os.environ.setdefault('DJANGO_SETTINGS_MODULE','core.settings')
django.setup()
from courses.models import Course, Lesson

print("=== CONTENT MEAT AUDIT - Is it fine for beneficiaries? ===\n")

# Check 1: Sample actual lesson content
samples = Lesson.objects.all().order_by('?')[:5]
for i, lesson in enumerate(samples, 1):
    print(f"\n--- SAMPLE {i}: Course {lesson.course.id} - {lesson.course.title[:50]} ---")
    print(f"Lesson {lesson.order}: {lesson.title}")
    content = lesson.content or ''
    print(f"Length: {len(content)} chars")
    checks = {
        'has_h2/h3': '<h2' in content.lower() or '<h3' in content.lower(),
        'has_steps': '<ol' in content.lower() or 'Step' in content or 'practical' in content.lower(),
        'has_tools': 'tool' in content.lower() or 'material' in content.lower(),
        'has_safety': 'safety' in content.lower() or 'ppe' in content.lower() or 'danger' in content.lower(),
        'has_business': 'business' in content.lower() or 'money' in content.lower() or 'income' in content.lower() or 'market' in content.lower(),
        'has_africa': 'africa' in content.lower() or 'nigeria' in content.lower() or 'kenya' in content.lower() or 'tanzania' in content.lower(),
        'is_placeholder': 'Theory and practical for module' in content and len(content) < 500
    }
    for k,v in checks.items():
        print(f"  {k}: {v}")
    if checks['is_placeholder']:
        print("  ❌ PLACEHOLDER - needs enrichment!")
    else:
        print("  ✅ Rich content")
    print(f"Preview: {content[:400]}...\n")

# Check 2: Overall stats
total = Lesson.objects.count()
rich = 0
placeholder = 0
with_business = 0
with_safety = 0
with_africa = 0
for l in Lesson.objects.all():
    c = l.content or ''
    if 'Theory and practical for module' in c and len(c) < 500:
        placeholder += 1
    else:
        rich += 1
    if 'business' in c.lower() or 'income' in c.lower():
        with_business += 1
    if 'safety' in c.lower():
        with_safety += 1
    if 'africa' in c.lower():
        with_africa += 1

print("\n=== OVERALL CONTENT QUALITY ===")
print(f"Total lessons: {total}")
print(f"Rich lessons: {rich} ({rich*100//total}%)")
print(f"Placeholder (thin): {placeholder} ({placeholder*100//total}%)")
print(f"With business/income angle: {with_business} ({with_business*100//total}%)")
print(f"With safety: {with_safety} ({with_safety*100//total}%)")
print(f"With Africa context: {with_africa} ({with_africa*100//total}%)")

# Quality score
score = (rich*0.4 + with_business*0.2 + with_safety*0.2 + with_africa*0.2) / total * 100
print(f"\nQUALITY SCORE: {score:.1f}/100")

if placeholder > 0:
    print(f"\n⚠️  {placeholder} lessons still placeholders - run populate_rich_lessons.py again with force")
if with_business < total*0.8:
    print(f"⚠️  Only {with_business} have business angle - beneficiaries need income guidance")
if with_safety < total*0.8:
    print(f"⚠️  Only {with_safety} have safety - critical for hands-on skills")

if score >= 90:
    print("\n✅ CONTENT IS FINE - Ready for huge beneficiaries, job creation, self-reliant!")
elif score >= 70:
    print("\n⚠️  CONTENT GOOD but can be better for humanitarian impact")
else:
    print("\n❌ CONTENT NEEDS WORK - not yet ready for beneficiaries")