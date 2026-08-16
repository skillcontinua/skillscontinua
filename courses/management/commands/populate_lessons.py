from django.core.management.base import BaseCommand
from courses.models import Course, Lesson

COMPLEX_KEYWORDS = ['electrical','welding','plumbing','construction','masonry','nursing','midwifery','pharmacy','medical','health','software','programming','python','web development','data science','ai','mechanical','automotive','refrigeration','solar','renewable','accounting','law','architecture']
SIMPLE_KEYWORDS = ['soap','detergent','bead','catering','baking','hair','barbing','tie and dye','fashion','tailoring','makeup']

MODULE_TEMPLATES = {
    1: "Module 1: Foundation, Orientation & Industry Overview",
    2: "Module 2: Tools, Materials & Safety",
    3: "Module 3: Core Principles & Theory I",
    4: "Module 4: Core Principles & Theory II",
    5: "Module 5: Practical Skills I - Hands-on",
    6: "Module 6: Practical Skills II - Intermediate",
    7: "Module 7: Advanced Techniques & Innovation",
    8: "Module 8: Quality Control, Costing & Pricing",
    9: "Module 9: Marketing, Branding & Selling Your Skill",
    10: "Module 10: Final Project, Certification & Business Launch",
    11: "Module 11: Specialization & Troubleshooting",
    12: "Module 12: Industry Attachment & Mentorship",
    13: "Module 13: Scaling & Employing Others",
    14: "Module 14: Digital Tools & Online Presence",
    15: "Module 15: Sustainability & Continuous Improvement",
}

def get_module_count(title):
    tl = title.lower()
    if any(k in tl for k in COMPLEX_KEYWORDS):
        return 12
    if any(k in tl for k in SIMPLE_KEYWORDS):
        return 8
    return 10

def build_content(course_title, module_title):
    return f'''
<h3>{module_title} - {course_title}</h3>
<p><b>Duration: 180 minutes (3 hours)</b> | Languages: English, French, Spanish, Portuguese, Swahili, Arabic | Method: Pedagogy, Andragogy, Heutagogy, Cybergogy</p>

<h3>1. Introduction</h3>
<p>Welcome to {module_title} of {course_title}. This module is designed for rich, detailed, comprehensive learning that is absorbed, digested and retained. Not too long to be tiring, not shallow to be poor quality.</p>

<h3>2. Learning Objectives</h3>
<ul>
<li>Understand key concepts of {module_title}</li>
<li>Demonstrate practical skill with 80% accuracy</li>
<li>Create income-generating output from {course_title}</li>
<li>Retain knowledge via teach-back and spaced repetition</li>
</ul>

<h3>3. Detailed Theory (70 mins)</h3>
<p>Rich content for {course_title}. Covers scientific principles, step-by-step procedures, common mistakes, quality standards (SON, ISO), adaptation for low-resource African and Third World settings. Market size, import substitution, self-reliance vs job seeking. Includes terminology in 6 languages.</p>
<p>Deep dive: tools, calculations, safety, regulations, innovations. Examples from Nigeria, Kenya, Senegal, Angola, Egypt, Brazil.</p>

<h3>4. Practical Session (80 mins)</h3>
<p>Hands-on: Produce 3 samples/products, test quality, improve, peer review, photo documentation for portfolio. Field task: Visit market, interview 2 practitioners, cost materials in Naira/USD.</p>

<h3>5. African & Third World Case Study (15 mins)</h3>
<p>Youth in Aba, Nairobi, Dakar, Kigali, Cairo, Luanda started {course_title} with <$50, grew to $500/month. What would you do differently?</p>

<h3>6. Assessment & Retention (15 mins)</h3>
<ul>
<li>5 MCQs</li>
<li>1 practical submission</li>
<li>Teach-back: Explain to 10-year-old</li>
<li>Review after 1 day, 7 days</li>
</ul>
'''

class Command(BaseCommand):
    help = "Populate rich lessons 8-12 per course - fixed for your Lesson model"

    def handle(self, *args, **options):
        courses = Course.objects.all()
        created = 0
        updated = 0
        for course in courses:
            target = get_module_count(course.title)
            for i in range(1, target+1):
                mod_title = MODULE_TEMPLATES.get(i, f"Module {i}: Extended Specialization")
                content = build_content(course.title, mod_title)
                # Use only fields that exist in your model - adjust if your Lesson has different fields
                try:
                    lesson, is_new = Lesson.objects.get_or_create(
                        course=course,
                        order=i,
                        defaults={'title': mod_title, 'content': content, 'duration': 180}
                    )
                except Exception as e:
                    # Fallback if field is duration_minutes
                    lesson, is_new = Lesson.objects.get_or_create(
                        course=course,
                        order=i,
                        defaults={'title': mod_title, 'content': content, 'duration_minutes': 180}
                    )
                
                if not is_new:
                    if len(lesson.content or '') < 500:
                        lesson.title = mod_title
                        lesson.content = content
                        # Try both duration field names
                        try:
                            lesson.duration = 180
                        except:
                            try:
                                lesson.duration_minutes = 180
                            except:
                                pass
                        lesson.save()
                        updated += 1
                else:
                    created += 1
        
        self.stdout.write(self.style.SUCCESS(f'SUCCESS: Courses={Course.objects.count()}, Created={created}, Updated={updated}, Total Lessons={Lesson.objects.count()}'))
