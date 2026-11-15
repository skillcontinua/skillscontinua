# C:\skillscontinua\courses\management\commands\seed_cloud_master.py
from django.core.management.base import BaseCommand
from courses.models import Category, Course, Lesson

class Command(BaseCommand):
    help = 'Seeds all pillars and comprehensive courses safely on cloud or local databases.'

    def handle(self, *args, **options):
        self.stdout.write("Initializing 14 Strategic Pillars...")
        
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

        self.stdout.write(self.style.SUCCESS("Pillars verified/initialized successfully."))