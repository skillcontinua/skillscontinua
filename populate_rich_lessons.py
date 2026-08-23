import os, django, json, random
os.environ.setdefault('DJANGO_SETTINGS_MODULE','core.settings')
django.setup()
from courses.models import Course, Lesson

# Rich lesson templates by category keywords - open resources style (FAO, UNESCO, WHO, etc.)
TEMPLATES = {
    'solar': """<h2>{title} - Comprehensive Guide for Africa</h2>
<h3>1. Introduction & Why It Matters in Africa</h3>
<p>{desc} In Africa, unreliable grid power makes this skill a business opportunity. Learners in Nigeria, Kenya, Tanzania, Mozambique, Angola can earn income providing this service.</p>
<h3>2. Theory - How It Works</h3>
<p>Fundamental principles, components, and physics. Understand voltage, current, energy flow. Open resources: IRENA, FAO energy guides.</p>
<h3>3. Tools & Materials Needed (Affordable in Africa)</h3>
<ul><li>Basic toolkit locally available in markets</li><li>Safety gear - gloves, goggles</li><li>Multimeter - essential</li><li>Local alternatives: use reclaimed materials where safe</li></ul>
<h3>4. Step-by-Step Practical</h3>
<ol><li>Preparation & site assessment</li><li>Safety check - disconnect power, use PPE</li><li>Installation / procedure following manufacturer spec</li><li>Testing - verify output, continuity</li><li>Troubleshooting common issues in dusty/hot climates</li></ol>
<h3>5. Common Mistakes & How to Avoid</h3><p>Undersizing, poor connections, ignoring heat, no maintenance plan.</p>
<h3>6. Safety</h3><p>Electrical shock, falls, burns. Always disconnect, work with partner, use insulated tools.</p>
<h3>7. Business Angle - Make Money</h3><p>Charge installation fee + maintenance contract. Target: homes, schools, clinics, small businesses. In East Africa Swahili market: offer "mkataba wa matengenezo". In Lusophone Angola/Mozambique: "contrato de manutenção".</p>
<h3>8. Practice Task</h3><p>Complete installation on sample board and document with photos.</p>
<h3>9. Further Learning</h3><p>IRENA, GIZ, Practical Action guides. UNESCO TVET.</p>
""",
    'farm': """<h2>{title} - Complete African Farming Guide</h2>
<h3>1. Why This Matters for Food Security</h3><p>{desc} FAO estimates Africa's food demand will double. This skill creates income.</p>
<h3>2. Biology / Principles</h3><p>Life cycle, breeds suited for Africa (heat tolerant, disease resistant), feeding, housing.</p>
<h3>3. What You Need (Low Cost)</h3><ul><li>Locally available breeds: improved indigenous</li><li>Feeding: local feed formulation to reduce cost</li><li>Housing: ventilated, low cost materials</li></ul>
<h3>4. Practical Steps</h3><ol><li>Site selection & preparation</li><li>Sourcing stock from certified hatchery/farm</li><li>Daily care routine</li><li>Disease prevention - biosecurity</li><li>Harvesting & processing</li></ol>
<h3>5. African Challenges</h3><p>Heat, water scarcity, feed cost. Solutions: shade, rainwater harvesting, Black Soldier Fly feed.</p>
<h3>6. Business & Marketing</h3><p>Record costs, sell at farm gate, local market, WhatsApp groups, cooperatives. Value addition: smoking, packaging.</p>
<h3>7. Task</h3><p>Raise 10 units and keep records for 2 weeks.</p>
""",
    'tech': """<h2>{title} - Practical Tech Skills for Africa</h2>
<h3>1. Overview</h3><p>{desc} Digital skills unlock remote work across Africa and beyond - Nigeria, Kenya, South Africa, Rwanda hubs.</p>
<h3>2. Core Concepts</h3><p>Explained simply, with analogies relevant to African learners.</p>
<h3>3. Tools - Free & Open Source</h3><p>Use free software: GIMP, Blender, VS Code, Linux. Works on low-spec laptops, even Android phones.</p>
<h3>4. Hands-On Lab</h3><ol><li>Setup environment</li><li>Build small project</li><li>Test & debug</li><li>Deploy / share</li></ol>
<h3>5. Mistakes to Avoid</h3><p>Skipping fundamentals, no backups, not testing on slow internet.</p>
<h3>6. Freelance Income</h3><p>Platforms: Upwork, Fiverr, Andela, local businesses need websites, data. Charge in USD.</p>
<h3>7. Assignment</h3><p>Build portfolio piece and publish.</p>
""",
    'default': """<h2>{title} - Rich Learning Module for Africa and Beyond</h2>
<h3>1. Introduction</h3><p>{desc} This module gives practical, hands-on skills you can apply immediately in your community across Africa - from Lagos to Nairobi, from Luanda to Dakar.</p>
<h3>2. What You Will Learn</h3><ul><li>Clear theory in simple language</li><li>Practical demonstration</li><li>Local examples from African context</li></ul>
<h3>3. Materials Needed</h3><p>Everyday items available in local markets. No expensive imports required.</p>
<h3>4. Step-by-Step Practice</h3><ol><li>Prepare workspace</li><li>Follow procedure carefully</li><li>Check quality</li><li>Improve with repetition</li></ol>
<h3>5. Safety & Quality</h3><p>Work safely, protect health, deliver quality to customers.</p>
<h3>6. Business Opportunity</h3><p>This skill can be a business: offer service in your area, teach others, create cooperative. Applicable across Africa and beyond.</p>
<h3>7. Practice & Reflection</h3><p>Do it 3 times, note what improved.</p>
<h3>8. Learn More</h3><p>Open resources: UNESCO, FAO, WHO, ILO TVET toolkits.</p>
"""
}

def pick_template(course_title):
    t = course_title.lower()
    if any(k in t for k in ['solar','inverter','battery','wind','electrical','wiring']):
        return TEMPLATES['solar']
    if any(k in t for k in ['farm','poultry','fish','catfish','cattle','bee','pig','agriculture','hydroponic']):
        return TEMPLATES['farm']
    if any(k in t for k in ['python','javascript','web','cloud','ai','machine','cyber','linux','windows','excel','word']):
        return TEMPLATES['tech']
    return TEMPLATES['default']

print("Enriching lessons with rich detailed content...")
courses = Course.objects.all().order_by('id')
total = 0
for course in courses:
    lessons = Lesson.objects.filter(course=course).order_by('order')
    for lesson in lessons:
        # Skip if already rich (>1000 chars and has h3)
        if len(lesson.content or '') > 1500 and '<h3>' in lesson.content:
            continue
        tmpl = pick_template(course.title)
        rich = tmpl.format(title=f"Module {lesson.order}: {lesson.title or course.title}", desc=course.description[:300])
        # Add module-specific focus
        rich = rich.replace("{title}", lesson.title or course.title)
        lesson.content = rich
        lesson.save()
        total += 1
        if total % 500 == 0:
            print(f"Enriched {total} lessons...")

print(f"RICH LESSONS DONE - Enriched {total} lessons with comprehensive Africa-ready content")
# Summary
print(f"Total courses: {Course.objects.count()}, Total lessons: {Lesson.objects.count()}")
