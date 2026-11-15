# C:\skillscontinua\courses\management\commands\import_backup_courses.py`
import sqlite3
from django.core.management.base import BaseCommand
from django.db import transaction
from courses.models import Category, Course, Lesson


class Command(BaseCommand):
    help = 'Imports all 175 courses and 1,113 lessons from C:\\skillscontinua_backup\\db.sqlite3 mapped into the 14 pillars.'

    def handle(self, *args, **options):
        backup_path = r'C:\skillscontinua_backup\db.sqlite3'
        self.stdout.write(f"Connecting to backup database at {backup_path}...")

        conn = sqlite3.connect(backup_path)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

        # Map old backup category IDs / pillars to your current 14 Strategic Pillars
        OLD_TO_NEW_PILLAR = {
            'literacy': 'education_teaching',
            'primary': 'education_teaching',
            'secondary': 'education_teaching',
            'secondary_arts': 'education_teaching',
            'secondary_commercial': 'business_entrepreneurship',
            'secondary_science': 'education_teaching',
            'secondary_technical': 'vocational_technical_skills',
            'secondary_trade': 'trades_craftsmanship',
            'computer': 'it_technology_software',
            'it': 'it_technology_software',
            'digital': 'it_technology_software',
            'certification': 'it_technology_software',
            'vocational': 'vocational_technical_skills',
            'building': 'trades_craftsmanship',
            'housing': 'trades_craftsmanship',
            'electrical': 'renewable_energy_solar',
            'carpentry': 'trades_craftsmanship',
            'welding': 'trades_craftsmanship',
            'tailoring': 'trades_craftsmanship',
            'auto_motorcycle': 'automotive_repairs_maintenance',
            'auto_cars': 'automotive_repairs_maintenance',
            'auto_heavy': 'automotive_repairs_maintenance',
            'beauty_hair': 'beauty_personal_care',
            'beauty_makeup': 'beauty_personal_care',
            'agriculture': 'agriculture_agro_business',
            'financial': 'finance_professional_services',
            'life_skills': 'business_entrepreneurship',
        }

        # Ensure all 14 pillars exist in active DB
        PILLAR_DEFAULTS = {
            "renewable_energy_solar": ("Renewable Energy & Solar", "☀️", "Solar Installation, Inverters, Lithium Batteries, Wind & Off-Grid Power Systems."),
            "it_technology_software": ("IT Technology & Software", "💻", "Computers, Hardware Repair, Operating Systems, Drones, CCTV, Networking, Cloud, Cybersecurity, AI & Certifications."),
            "automotive_repairs_maintenance": ("Automotive Repairs & Maintenance", "🚗", "OBD2 Diagnostics, Keke/Okada Repair, Engines, Carburetors & Mechanical Enterprise."),
            "trades_craftsmanship": ("Trades & Craftsmanship", "🛠️", "Tailoring, Carpentry, Welding, Plumbing, Electrical & Building Trades."),
            "agriculture_agro_business": ("Agriculture & Agro-Business", "🌾", "Poultry, Fish Farming, Snail Rearing, Crop Production & Agro-Export."),
            "business_entrepreneurship": ("Business & Entrepreneurship", "💼", "Starting a Business, Ariaria Importation, Sales, E-commerce & CAC Registration."),
            "finance_professional_services": ("Finance & Professional Services", "💰", "Bookkeeping, Tax, Real Estate, Investment & Shop Accounting."),
            "health_wellness": ("Health & Wellness", "❤️", "First Aid, Community Nursing, Nutrition & Traditional Herbal Medicine."),
            "education_teaching": ("Education & Teaching", "🎓", "Nursery Teaching, Adult Literacy, JAMB Tutoring & Pedagogical Skills."),
            "media_creative_arts": ("Media & Creative Arts", "🎭", "Phone Videography, Graphic Design, Photography, DJ & Cultural Heritage."),
            "beauty_personal_care": ("Beauty & Personal Care", "💄", "Advanced Barbing, Wig Making, Makeup & Manicure/Pedicure."),
            "transport_logistics": ("Transport & Logistics", "🚚", "Ride-Hailing, Courier Services, Fleet Management & Shipping."),
            "government_social_impact": ("Government & Social Impact", "🤝", "NGO Setup, Grant Writing, Community Leadership & Advocacy."),
            "vocational_technical_skills": ("Vocational & Technical Skills", "🔧", "General Foundational Vocational & Technical Training Tracks."),
        }

        active_categories = {}
        for slug, (name, icon, desc) in PILLAR_DEFAULTS.items():
            cat, _ = Category.objects.get_or_create(
                pillar=slug,
                defaults={'name': name, 'icon': icon, 'description': desc}
            )
            active_categories[slug] = cat

        # Load old categories lookup
        old_cats = {
            row['id']: row['pillar']
            for row in cur.execute("SELECT id, pillar FROM courses_category").fetchall()
        }

        # Inspect active Course & Lesson model fields so we only set valid columns
        course_field_names = {f.name for f in Course._meta.get_fields()}
        lesson_field_names = {f.name for f in Lesson._meta.get_fields()}

        backup_courses = cur.execute("SELECT * FROM courses_course").fetchall()
        imported_courses = 0
        imported_lessons = 0

        with transaction.atomic():
            for bc in backup_courses:
                old_pillar = old_cats.get(bc['category_id'], 'vocational')
                target_pillar = OLD_TO_NEW_PILLAR.get(old_pillar, 'vocational_technical_skills')
                target_cat = active_categories[target_pillar]

                course_defaults = {
                    'category': target_cat,
                    'description': bc['description'] or '',
                    'level': bc['level'] or 'beginner',
                    'learning_approach': bc['learning_approach'] or 'andragogic',
                    'duration_hours': bc['duration_hours'] or 40,
                    'is_active': bool(bc['is_active']),
                    'featured': bool(bc['featured']),
                }

                # Optional fields present on your model
                optional_course_fields = [
                    'age_group', 'learning_objectives', 'prerequisites', 'target_audience'
                ]
                for field in optional_course_fields:
                    if field in course_field_names and field in bc.keys():
                        course_defaults[field] = bc[field] or ''

                course_obj, created = Course.objects.get_or_create(
                    title=bc['title'],
                    defaults=course_defaults
                )
                if created:
                    imported_courses += 1

                # Fetch all lessons belonging to this backup course
                backup_lessons = cur.execute(
                    "SELECT * FROM courses_lesson WHERE course_id = ? ORDER BY \"order\" ASC",
                    (bc['id'],)
                ).fetchall()

                for bl in backup_lessons:
                    lesson_defaults = {
                        'title': bl['title'],
                        'content': bl['content'] or '',
                        'duration_minutes': bl['duration_minutes'] or 30,
                    }
                    if 'video_url' in lesson_field_names and 'video_url' in bl.keys():
                        lesson_defaults['video_url'] = bl['video_url'] or ''
                    if 'is_free_preview' in lesson_field_names and 'is_free_preview' in bl.keys():
                        lesson_defaults['is_free_preview'] = bool(bl['is_free_preview'])

                    _, l_created = Lesson.objects.get_or_create(
                        course=course_obj,
                        order=bl['order'],
                        defaults=lesson_defaults
                    )
                    if l_created:
                        imported_lessons += 1

        conn.close()
        self.stdout.write(self.style.SUCCESS(
            f"Import Complete! Added {imported_courses} new courses and {imported_lessons} new lessons. "
            f"Total Active DB Courses: {Course.objects.count()} | Total Lessons: {Lesson.objects.count()}"
        ))