# C:\skillscontinua\courses\management\commands\seed_cloud_master.py
from django.core.management.base import BaseCommand
from courses.models import Category, Course, Lesson

class Command(BaseCommand):
    help = 'Seeds all 14 pillars and core courses safely on Render PostgreSQL or local SQLite.'

    def handle(self, *args, **options):
        self.stdout.write("Initializing 14 Strategic Pillars & Core Curriculum...")
        
        PILLARS = [
            ("Renewable Energy & Solar", "renewable_energy_solar", "☀️", "Solar Installation, Inverters, Lithium Batteries, Wind & Off-Grid Power Systems."),
            ("IT Technology & Software", "it_technology_software", "💻", "Computers, Hardware Repair, Operating Systems, Drones, CCTV, Networking, Cloud, Cybersecurity, AI & Certifications."),
            ("Automotive Repairs & Maintenance", "automotive_repairs_maintenance", "🚗", "OBD2 Diagnostics, Keke/Okada Repair, Engines, Carburetors & Mechanical Enterprise."),
            ("Trades & Craftsmanship", "trades_craftsmanship", "🛠️", "Tailoring, Carpentry, Welding, Plumbing, Electrical & Building Trades."),
            ("Agriculture & Agro-Business", "agriculture_agro_business", "🌾", "Poultry, Fish Farming, Apiculture, Piggery, Crop Production & Agro-Export."),
            ("Business & Entrepreneurship", "business_entrepreneurship", "💼", "Starting a Business, Ariaria Importation, Sales, E-commerce & CAC Registration."),
            ("Finance & Professional Services", "finance_professional_services", "💰", "Bookkeeping, Tax, Real Estate, Investment & Shop Accounting."),
            ("Health & Wellness", "health_wellness", "❤️", "First Aid, Community Nursing, Nutrition & Traditional Herbal Medicine."),
            ("Education & Teaching", "education_teaching", "🎓", "Nursery Teaching, Adult Literacy, JAMB Tutoring & Pedagogical Skills."),
            ("Media & Creative Arts", "media_creative_arts", "🎭", "Phone Videography, Graphic Design, Photography, DJ & Cultural Heritage."),
            ("Beauty & Personal Care", "beauty_personal_care", "💄", "Advanced Barbing, Wig Making, Makeup & Manicure/Pedicure."),
            ("Transport & Logistics", "transport_logistics", "🚚", "Ride-Hailing, Courier Services, Fleet Management & Shipping."),
            ("Government & Social Impact", "government_social_impact", "🤝", "NGO Setup, Grant Writing, Community Leadership & Advocacy."),
            ("Vocational & Technical Skills", "vocational_technical_skills", "🔧", "General Foundational Vocational & Technical Training Tracks."),
        ]

        cats = {}
        for name, pillar_slug, icon, desc in PILLARS:
            cat, _ = Category.objects.get_or_create(
                pillar=pillar_slug,
                defaults={'name': name, 'icon': icon, 'description': desc}
            )
            cats[pillar_slug] = cat

        # Core anchor courses to guarantee full catalog availability on Render
        CORE_COURSES = [
            ("Solar Installation & Business - Power Aba Homes, Shops, Churches", "renewable_energy_solar", "beginner", 80, "Install solar for homes, shops, churches. Charge ₦150k-₦500k per job."),
            ("Inverter & Battery Repair - Fix Dead Systems", "renewable_energy_solar", "intermediate", 60, "Repair dead inverters, battery recovery, and maintenance."),
            ("Motorcycle & Keke NAPEP Repair - Complete Business", "automotive_repairs_maintenance", "beginner", 120, "Complete Okada & Keke repair - engine, gearbox, wiring, pricing, daily cash."),
            ("Auto Diagnostics with OBD2 Scanner - Professional Scan", "automotive_repairs_maintenance", "intermediate", 60, "Use OBD2 scanner to diagnose Toyota, Honda, Kia. Clear codes, live data."),
            ("Apiculture & Beekeeping - Honey Production & Processing", "agriculture_agro_business", "beginner", 40, "Commercial beekeeping, hive management, honey harvesting, processing, and packaging for export."),
            ("Piggery Management - Breeding & Pork Production", "agriculture_agro_business", "beginner", 50, "Modern pig farming, housing, feeding formulations, disease prevention, and profitable pork marketing."),
            ("Fish Farming - Catfish Production & Processing", "agriculture_agro_business", "beginner", 80, "Catfish 6 months, ₦1.5M profit - comprehensive course from fingerlings to table size."),
            ("Poultry - 100 to 1000 Birds Management", "agriculture_agro_business", "beginner", 80, "Egg business, feeding, vaccination, brooding, marketplace pricing."),
            ("CCTV Installation & Business - Cameras, DVR, Phone View", "it_technology_software", "beginner", 60, "Analog vs IP camera, DVR NVR, BNC, RJ45, install, configure, view on phone."),
            ("AI Technology for Business - ChatGPT, Gemini, Midjourney", "it_technology_software", "beginner", 60, "Use ChatGPT to write business proposals, AI images for flyers, AI video adverts."),
            ("CompTIA A+ Certification Complete Prep - Hardware & Software", "it_technology_software", "beginner", 60, "CompTIA A+ 1101 1102, hardware, networking, mobile, troubleshooting, exam prep."),
            ("Hair Dressing & Wig Making - Aba Women Money Maker", "beauty_personal_care", "beginner", 60, "Comprehensive professional training course tailored for practical mastery and economic empowerment."),
            ("Start Business with ₦50k - Zero to CEO", "business_entrepreneurship", "beginner", 80, "Business with small capital, lean startup, cash flow management, customer acquisition."),
            ("Importation from China - 1688 & Logistics", "business_entrepreneurship", "beginner", 80, "Import via 1688, WeChat pay, shipping agents, clearing, retailing for high profit."),
            ("N-Power & Government Grants - How to Apply & Win", "government_social_impact", "beginner", 40, "Comprehensive professional training course tailored for practical mastery and self-reliance."),
        ]

        added = 0
        for title, pillar_key, level, duration, desc in CORE_COURSES:
            cat = cats.get(pillar_key, cats['vocational_technical_skills'])
            course, created = Course.objects.get_or_create(
                title=title,
                category=cat,
                defaults={
                    "description": desc,
                    "level": level,
                    "learning_approach": "andragogic",
                    "duration_hours": duration,
                    "is_active": True,
                    "featured": True
                }
            )
            if created:
                added += 1

        self.stdout.write(self.style.SUCCESS(f"Cloud seed complete! Verified pillars and added {added} core courses. Total courses in DB: {Course.objects.count()}"))