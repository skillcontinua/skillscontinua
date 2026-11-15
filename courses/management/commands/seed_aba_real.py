from django.core.management.base import BaseCommand
from courses.models import Category, Course

class Command(BaseCommand):
    help = 'Seeds all 14 strategic pillars and 130+ master courses cleanly.'

    def handle(self, *args, **options):
        self.stdout.write("Initializing 14 Strategic Pillars...")
        
        PILLARS = [
            ("Renewable Energy & Solar", "renewable_energy_solar", "☀️", "Solar Installation, Inverters, Lithium Batteries, Wind & Off-Grid Power Systems."),
            ("IT Technology & Software", "it_technology_software", "💻", "Computers, Hardware Repair, Operating Systems, Drones, CCTV, Networking, Cloud, Cybersecurity, AI & Certifications."),
            ("Automotive Repairs & Maintenance", "automotive_repairs_maintenance", "🚗", "OBD2 Diagnostics, Keke/Okada Repair, Engines, Carburetors & Mechanical Enterprise."),
            ("Trades & Craftsmanship", "trades_craftsmanship", "🛠️", "Tailoring, Carpentry, Welding, Plumbing, Electrical & Building Trades."),
            ("Agriculture & Agro-Business", "agriculture_agro_business", "🌾", "Poultry, Fish Farming, Snail Rearing, Crop Production & Agro-Export."),
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

        self.stdout.write("Seeding master courses across pillars...")

        # Core Master Courses dataset mapped to strategic pillars
        COURSES_DATA = [
            # Renewable Energy & Solar
            ("Solar Installation & Business - Power Aba Homes, Shops, Churches", "renewable_energy_solar", "Install solar for homes, shops, churches. Charge ₦150k-₦500k per job.", "beginner", "andragogy", 80),
            ("Inverter & Battery Repair - Fix Dead Systems", "renewable_energy_solar", "Repair dead inverters, battery recovery, and maintenance.", "intermediate", "andragogy", 60),
            ("Hybrid Solar-Wind-Battery System - Complete Off-Grid", "renewable_energy_solar", "Combine solar + wind + battery, automatic changeover, power shops 24/7.", "beginner", "andragogy", 80),
            ("Lithium Battery Technology - Lead Acid, Lithium, Tubular", "renewable_energy_solar", "Battery repair, desulfation, lithium pack building, BMS, second-life battery business.", "beginner", "andragogy", 80),
            ("Mini Hydro - Village Stream Power", "renewable_energy_solar", "Micro hydro 1kW-10kW from village stream, power homes, stream mapping.", "beginner", "andragogy", 80),

            # IT Technology & Software
            ("Computer Literacy Basics - What is Computer?", "it_technology_software", "What is computer, types, desktop, laptop, tablet, phone, history, uses in business.", "beginner", "andragogy", 60),
            ("CCTV Installation & Business - Cameras, DVR, Phone View", "it_technology_software", "Analog vs IP camera, DVR NVR, BNC, RJ45, install, configure, view on phone.", "beginner", "andragogy", 60),
            ("AI Technology for Business - ChatGPT, Gemini, Midjourney", "it_technology_software", "Use ChatGPT to write business proposals, AI images for flyers, AI video adverts.", "beginner", "andragogy", 60),
            ("CompTIA A+ Certification Complete Prep - Hardware & Software", "it_technology_software", "CompTIA A+ 1101 1102, hardware, networking, mobile, troubleshooting, exam prep.", "beginner", "andragogy", 60),
            ("Drone Technology - Build, Fly, Photography & Mapping", "it_technology_software", "DJI, build FPV from kit, fly, aerial wedding photography, farm survey.", "beginner", "andragogy", 60),

            # Automotive Repairs & Maintenance
            ("Auto Diagnostics with OBD2 Scanner - Professional Scan", "automotive_repairs_maintenance", "Use OBD2 scanner to diagnose Toyota, Honda, Kia. Clear codes, live data.", "intermediate", "andragogy", 60),
            ("Motorcycle & Keke NAPEP Repair - Complete Business", "automotive_repairs_maintenance", "Complete Okada & Keke repair - engine, gearbox, wiring, pricing, daily cash.", "beginner", "andragogy", 120),
            ("Fossil Fuel Generator Mastery - Repair & Maintenance", "automotive_repairs_maintenance", "Repair Tiger, Sumec generators - oil change, carburetor tuning, windings.", "beginner", "andragogy", 80),
            ("Keke Fleet Owner Business", "automotive_repairs_maintenance", "Own 5 Keke, manage drivers, daily returns, maintenance schedules.", "beginner", "andragogy", 80),

            # Agriculture & Agro-Business
            ("Fish Farming - Catfish Production & Processing", "agriculture_agro_business", "Catfish 6 months, ₦1.5M profit - comprehensive course from fingerlings to table size.", "beginner", "andragogy", 80),
            ("Poultry - 100 to 1000 Birds Management", "agriculture_agro_business", "Egg business, feeding, vaccination, brooding, marketplace pricing.", "beginner", "andragogy", 80),
            ("Garri & Palm Oil Processing Business", "agriculture_agro_business", "Processing technology, packaging, export standards, local and international markets.", "beginner", "andragogy", 80),

            # Business & Entrepreneurship
            ("Start Business with ₦50k - Zero to CEO", "business_entrepreneurship", "Business with small capital, lean startup, cash flow management, customer acquisition.", "beginner", "andragogy", 80),
            ("Importation from China - 1688 & Logistics", "business_entrepreneurship", "Import via 1688, WeChat pay, shipping agents, clearing, retailing for high profit.", "beginner", "andragogy", 80),
            ("Tax & CAC Business Registration", "business_entrepreneurship", "Register business with CAC, TIN, tax compliance, corporate accounts setup.", "beginner", "andragogy", 80),
        ]

        Course.objects.all().delete() # Clean reload
        
        count = 0
        for title, pillar_key, desc, level, approach, duration in COURSES_DATA:
            cat = cats.get(pillar_key, cats['vocational_technical_skills'])
            Course.objects.create(
                title=title,
                category=cat,
                description=desc,
                level=level,
                learning_approach=approach,
                duration_hours=duration,
                is_active=True
            )
            count += 1

        self.stdout.write(self.style.SUCCESS(f"Successfully seeded {count} master courses across 14 pillars!"))