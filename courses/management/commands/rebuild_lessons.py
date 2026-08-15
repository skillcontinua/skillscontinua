from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from django.db import connection

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM courses_lesson")
        
        count=0
        for course in Course.objects.all().order_by('id'):
            title = course.title
            lessons = [
                (f"Module 1: Foundations of {title} - Theory, Safety & Standards", f"OBJECTIVE: Understand fundamentals, SON/ITF safety, Abia economy relevance. THEORY: History, principles. PRACTICAL: Identify 10 real applications in Ariaria Market, interview 2 artisans. TOOLS: Notebook, PPE. REAL SCENARIO: Client asks for {title} service - intake questions. ASSESSMENT: Safety checklist + market survey.", 1),
                (f"Module 2: Tools, Materials, Workshop Setup & Costing", f"OBJECTIVE: Select tools/materials, setup workshop, cost with profit. THEORY: Tool types, material grades, cost-plus pricing. PRACTICAL: Visit 3 suppliers in Aba, price materials, create N50k budget. TOOLS: Measuring, PPE. REAL SCENARIO: Startup with N50k. ASSESSMENT: Tool list with prices.", 2),
                (f"Module 3: Core Practical - Complete Real Job Start to Finish", f"OBJECTIVE: Execute full professional job public will pay for. THEORY: Step-by-step, quality control. PRACTICAL (5 hours): Perform 1 complete real job. Document with photos. ASSESSMENT: Must pass instructor + client inspection 80%.", 3),
                (f"Module 4: Advanced Techniques, Fault Diagnosis & Complaint Resolution", f"OBJECTIVE: Handle complex jobs and fix failures. THEORY: Diagnostics, handling difficult clients. PRACTICAL: Fix 3 common failures in {title}. REAL SCENARIO: Client brings faulty work from another artisan - diagnose and fix. ASSESSMENT: Fix-it challenge.", 4),
                (f"Module 5: Business, Client Service & Final Certification Project (Certificate Credibility)", f"OBJECTIVE: Serve public professionally, earn certificate with market value. THEORY: Pricing, customer service Igbo/English, CAC, WhatsApp marketing. PRACTICAL: Serve 3 REAL paying clients in Aba, collect testimonials, before/after photos. FINAL PROJECT MANDATORY FOR CERTIFICATE: Public job with documentation: brief, quotation, photos, invoice, testimonial video, reflection. Without this, no certificate. This gives credence to SkillsContinua certificate.", 5),
            ]
            for t,c,o in lessons:
                Lesson.objects.create(course=course, title=t, content=c, order=o, duration_minutes=180, is_free_preview=(o==1))
                count+=1
        self.stdout.write(f"SUCCESS: {Course.objects.count()} courses, {count} lessons")