from django.core.management.base import BaseCommand
from courses.models import Category, Course

class Command(BaseCommand):
    help = 'Seed 104 REAL Aba skills grouped into 16 pillars'

    def handle(self, *args, **options):
        # Delete dummy
        Course.objects.all().delete()
        print("Deleted dummy courses")

        pillars_data = {
            "Solar & Energy": [
                "Solar Panel Installation for Aba Homes", "Inverter & Battery Setup", "Solar Street Light Maintenance",
                "Solar-Powered Sewing Machine Setup", "Mini-Grid for Aba Market", "Solar Water Pumping", "Energy Auditing for Shops"
            ],
            "Tailoring & Fashion": [
                "Aba Made Shoe Making - Male", "Aba Made Shoe Making - Female", "Senator Wear Tailoring",
                "Ankara & Lace Design", "Industrial Machine Operation", "Pattern Drafting & Cutting", "Fashion Branding & Export"
            ],
            "Agriculture": [
                "Poultry Farming in Aba", "Fish Farming (Catfish)", "Cassava Processing to Garri",
                "Palm Oil Production", "Vegetable Farming (Ugu, Okra)", "Snail Farming", "Agribusiness Marketing"
            ],
            "Aba Market Trade": [
                "Ariaria Market Trading Skills", "Importation from China (Aba Focus)", "E-commerce for Aba Made",
                "Shop Management & Inventory", "Customer Service Igbo/English", "Pricing & Negotiation", "Export Documentation"
            ],
            "Igbo & Culture": [
                "Igbo Language for Business", "Igbo Proverbs & Storytelling", "Mmanwu & Cultural Crafts",
                "Igbo Traditional Attire Making", "Igbo Cuisine & Catering", "History of Aba & Ngwa", "Igbo Gospel Music"
            ],
            "Business & Entrepreneurship": [
                "CAC Registration Umuahia", "Business Plan for ABIAPOLY Students", "POS & Mobile Money Business",
                "Bookkeeping for Market Women", "Digital Marketing", "Fundraising & Grants", "Cooperative Formation"
            ],
            "Tech & Digital": [
                "Phone Repair & Unlocking", "Laptop Repair Aba", "Graphics Design (Corel for Aba Print)",
                "Website for Aba Shops (No Code)", "Social Media for Tailors", "AI for Business", "Starlink Setup & Maintenance"
            ],
            "Construction": [
                "Block Moulding", "Tiling & Interlocking", "POP Ceiling Design", "Painting & Screeding",
                "Bricklaying for Aba Houses", "Aluminum Windows", "Building Cost Estimation"
            ],
            "Food Processing": [
                "Chin-Chin & Snacks Production", "Baking - Bread & Cake Aba Style", "Zobo & Tiger Nut Drink",
                "Abacha & Food Packaging", "Palm Wine Bottling", "Spice Blending", "Food Safety (NAFDAC)"
            ],
            "Beauty & Cosmetology": [
                "Hair Making & Wig Installation", "Barbing & Dreadlocks", "Makeup & Gele Tying",
                "Soap & Cream Production", "Perfume & Deodorant Making", "Nail Tech", "Beauty Shop Management"
            ],
            "Automobile": [
                "Keke & Okada Repair", "Car Diagnostics (OBD)", "Auto Electrical", "Spray Painting",
                "Vulcanizing & Tyre", "Driving School Theory", "Spare Parts Business"
            ],
            "Welding & Fabrication": [
                "Arc Welding Basics", "Gate & Burglary Fabrication", "Water Tank Stand", "Metal Furniture",
                "Aluminum Fabrication", "Generator Cage Making", "Welding Safety"
            ],
            "Electrical": [
                "House Wiring Aba Standard", "Generator Repair", "Rewinding Electric Motors", "CCTV Installation",
                "Sound System Setup for Churches", "Electrical Safety - No NEPA", "Solar Inverter Wiring"
            ],
            "Plumbing": [
                "Plumbing for Bungalow", "Borehole Installation", "Water Closet Repair", "Pipe Fitting PVC",
                "Water Treatment Small Scale", "Plumbing Tools", "Estimation & Quotation"
            ],
            "Creative Arts": [
                "Photography for Aba Events", "Video Editing for Churches", "Sign Writing & Banners",
                "Printing - Flex & SAV", "Drumming & Igbo Instruments", "Comedy & MC for Aba Events", "Content Creation (TikTok for Market)"
            ],
            "General Africa & World": [
                "English for Global Market", "French for Africa Trade", "Customer Service Worldwide",
                "Global Fundraising", "Diaspora Collaboration"
            ],
        }

        total = 0
        for pillar_name, courses in pillars_data.items():
            try:
                cat = Category.objects.get(name=pillar_name)
            except Category.DoesNotExist:
                cat = Category.objects.get(pillar=pillar_name.lower().replace(' & ','_').replace(' ','_'))
            
            for idx, title in enumerate(courses, 1):
                Course.objects.create(
                    category=cat,
                    title=title,
                    description=f"{title} - Practical Aba skill for youth empowerment, South-East pilot (Imo/Rivers/Abia/NDDC ready), global market. Includes Igbo explanation.",
                    level='beginner' if idx <= 3 else 'intermediate',
                    age_group='adult',
                    learning_approach='andragogy',
                    duration_hours=20,
                    learning_objectives=f"Learn {title} hands-on, start business in Aba",
                    target_audience="Aba Youth, ABIAPOLY students, Market women",
                    is_active=True,
                    featured=(idx==1)
                )
                total += 1
        self.stdout.write(self.style.SUCCESS(f"✅ Seeded {total} REAL Aba courses grouped into 16 pillars!"))