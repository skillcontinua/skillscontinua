import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
from courses.models import Course, Lesson

course = Course.objects.get(id=315)  # Flywheel
lessons = course.lessons.order_by('order')
print(f"Populating {course.title} - {lessons.count()} lessons")

templates = [
    ("Introduction to {title}", "In this introduction you will learn what {title} is, why it matters in Nigeria, and safety rules."),
    ("Module 1: Foundations", "Theory, safety & industry standards. Covers {title} basics, tools needed, and Nigerian regulations."),
    ("Core Concept", "Deep dive into {title}: how it works, physics, calculations, with diagrams and real examples."),
    ("Practical Workshop", "Hands-on: Step-by-step to build/install {title}. Materials list, costing for Aba market, safety checks."),
]

for i, lesson in enumerate(lessons, 1):
    # Keep title, but expand content from highlight
    base = lesson.title
    full_content = f"""
<h3>{base}</h3>
<p><strong>Objective:</strong> By end of this lesson, you will be able to explain and apply {base} for Flywheel Energy Storage.</p>

<h4>1. Theory (40 mins)</h4>
<p>{base} is critical for renewable energy in Nigeria. This section explains definition, principles, and why it matters for off-grid power in Abia State.</p>
<ul>
<li>What is {base}?</li>
<li>Why it matters for flywheel systems</li>
<li>Safety precautions</li>
</ul>

<h4>2. Practical Steps (60 mins)</h4>
<ol>
<li>Prepare tools: multimeter, spanners, safety gloves</li>
<li>Follow workshop setup as per Module 2</li>
<li>Test and measure output</li>
<li>Document results in portfolio</li>
</ol>

<h4>3. Business Angle (30 mins)</h4>
<p>How to charge clients in Aba for {base} service, costing, and customer complaint handling.</p>

<h4>4. Task</h4>
<p>Practice {base} today and upload photo to portfolio.</p>
"""
    lesson.content = full_content
    lesson.save()
    print(f"  {i}. Done: {base[:50]}")

print("DONE - 315 populated")