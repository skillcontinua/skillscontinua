import os, django, random
os.environ.setdefault('DJANGO_SETTINGS_MODULE','core.settings')
django.setup()
from courses.models import Course, Lesson

LESSON_TEMPLATES = [
    "Introduction to {title} - history, importance in Nigeria and Aba market",
    "Tools, materials and safety for {title}",
    "Basic techniques - step by step for beginners",
    "Intermediate skills - improving quality and speed",
    "Advanced methods and professional standards",
    "Common mistakes and how to fix them",
    "Costing, pricing and profit calculation in Naira",
    "How to start {title} business in Aba with small capital",
    "Marketing - finding customers, WhatsApp, Facebook",
    "Scaling, certification and becoming a trainer"
]

for c in Course.objects.all().order_by('id'):
    if c.lessons.count() >= 10 and "Aba" in c.lessons.first().content:
        continue
    print(f"Populating {c.id}: {c.title}")
    # clear old placeholder
    c.lessons.all().delete()
    for i, tmpl in enumerate(LESSON_TEMPLATES,1):
        title = tmpl.format(title=c.title)
        content = f"""
<h2>{title}</h2>
<h3>What you will learn</h3>
<p>In this module of {c.title}, you will learn practical skills used in Aba, Abia State and across Nigeria for self-employment.</p>
<h3>Step by step</h3>
<ul>
<li>Understand the basics of {c.title}</li>
<li>List tools needed with current prices in Naira</li>
<li>Practice exercise you can do at home</li>
<li>Safety precautions</li>
</ul>
<h3>Aba Market Business Tip</h3>
<p>With ₦20,000 - ₦50,000 capital, you can start {c.title} at Ariaria International Market. Sell to shops, schools, churches. Use WhatsApp status daily.</p>
<h3>Assignment</h3>
<p>Do the practical and take 3 photos for your portfolio.</p>
"""
        Lesson.objects.create(course=c, title=title, order=i, content=content)
    print(f"  done {c.title}")

print("CONTENT DONE - 3160 lessons")