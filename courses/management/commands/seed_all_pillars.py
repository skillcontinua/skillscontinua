from django.core.management.base import BaseCommand
from courses.models import Category, Course, Lesson

class Command(BaseCommand):
    def handle(self, *args, **options):
        # CORRECT SLUGS FROM YOUR DB
        lessons_template = [
            ("Why This Business is Goldmine in Aba - Market Analysis 2026", "video"),
            ("Tools Needed - Full List with Prices in Ariaria Market", "pdf"),
            ("Safety & Workshop Setup", "video"),
            ("Basics Theory - Simple English + Igbo Explanation", "video"),
            ("Practical Demo 1 - Hands On", "video"),
            ("Intermediate Level - Step by Step", "video"),
            ("Practical Demo 2 - Real Customer Job", "video"),
            ("Advanced Expert Level", "video"),
            ("How to Charge & Get Customers in Aba", "text"),
            ("Where to Buy Materials Cheap - Aba & Lagos", "text"),
            ("Pricing Template - 2026 Aba Prices", "pdf"),
            ("Marketing - Parks, Markets, WhatsApp Status", "text"),
            ("Mobile Service - Extra Income", "text"),
            ("Saving & Expanding - From 1 to 5 Boys", "text"),
            ("Branding, Receipt, Warranty - Be Professional", "text"),
            ("Common Mistakes & Troubleshooting", "text"),
            ("Final Practical - Do 3 Real Jobs", "video"),
            ("Business Plan - Start with ₦50k", "pdf"),
            ("Mentorship - Find Master in Aba", "text"),
            ("Next Steps - From Learning to Earning", "text"),
        ]

        pillars_courses = [
            ("renewable-energy-solar", "Solar Installation - Power Aba Homes", "Install solar, charge ₦150k-₦500k"),
            ("renewable-energy-solar", "Inverter & Battery Repair", "Repair dead inverters, batteries"),
            ("renewable-energy-solar", "Solar Cold Room for Market Women", "Build solar freezer for Ariaria"),
            ("technology-software", "Phone Repair - Ariaria Phone Village", "Fix Android, iPhone - ₦3k-₦15k per repair"),
            ("technology-software", "Web Dev for Aba Shops", "Build sites for shops, charge ₦50k-₦150k"),
            ("technology-software", "POS Business Setup", "POS business, make ₦5k daily"),
            ("trades-craftsmanship", "Welding & Fabrication - Gates, Tanks", "Welding most needed in Aba"),
            ("trades-craftsmanship", "Plumbing - No More Leak", "Fix house plumbing"),
            ("trades-craftsmanship", "Carpentry & Furniture", "Chair ₦25k, Wardrobe ₦80k"),
            ("agriculture-agro-business", "Poultry - 100 to 1000 Birds", "Egg business ₦3k/crate profit"),
            ("agriculture-agro-business", "Fish Farming - Catfish", "Catfish 6 months, ₦1.5M profit"),
            ("agriculture-agro-business", "Garri & Palm Oil Processing", "Export from Aba"),
            ("business-entrepreneurship", "Start Business with ₦50k - Zero to CEO", "Business with small capital"),
            ("business-entrepreneurship", "Importation from China - Ariaria", "Import via 1688 to Ariaria"),
            ("business-entrepreneurship", "Shop Management - Ariaria Methods", "Manage shop, stock, sales"),
            ("digital-marketing-content", "Facebook & WhatsApp Marketing for Market Women", "Sell via WhatsApp Status"),
            ("digital-marketing-content", "Content Creation - Phone Video", "Shoot product videos ₦10k each"),
            ("digital-marketing-content", "Influencer Business in Aba", "Become influencer"),
            ("health-wellness", "Community Health - First Aid, Patent Medicine", "First aid, BP check, drugs"),
            ("health-wellness", "Igbo Herbal Medicine", "Igbo herbs, dosage, safety"),
            ("health-wellness", "Food & Nutrition - Aba Foods", "Balanced diet with local foods"),
            ("education-teaching", "Teaching Children 6-12 - Lesson Note", "Teach nursery/primary"),
            ("education-teaching", "Adult Education - Market Women", "Teach adults to read, write"),
            ("education-teaching", "Computer for Teachers", "Use projector, Excel"),
            ("finance-professional", "Bookkeeping for Aba Shops", "Record sales, profit daily"),
            ("finance-professional", "POS & QuickBooks", "Accounting app"),
            ("finance-professional", "Tax & CAC Registration", "Register business ₦25k"),
            ("media-creative-arts", "Photography & Video - Aba Weddings", "Wedding ₦150k-₦500k"),
            ("media-creative-arts", "Graphic Design with Phone - Canva", "Design flyers ₦3k each"),
            ("media-creative-arts", "DJ & Sound System Business", "DJ for events"),
            ("transport-logistics", "Keke Fleet Owner Business", "Own 5 Keke, ₦25k daily"),
            ("transport-logistics", "Interstate Transport Business", "Manage buses, park"),
            ("transport-logistics", "Delivery & Courier in Aba", "Jumia style in Aba"),
            ("beauty-personal-care", "Barbing Salon Business", "Cut ₦500-₦1k, 20 customers = ₦15k/day"),
            ("beauty-personal-care", "Hair Dressing & Wig Making", "Wig ₦15k-₦50k, women business"),
            ("beauty-personal-care", "Makeup & Gele Tying", "Makeup ₦20k-₦50k per bride"),
            ("government-social-impact", "N-Power & Grants - How to Apply", "FG grants, BOI, SMEDAN"),
            ("government-social-impact", "NGO & Community Development", "Start foundation, proposal"),
            ("government-social-impact", "Youth Leadership & Politics", "Leadership for Aba youths"),
            ("automotive-repairs-maintenance", "Panel Beating & Spray Painting", "Body work ₦50k-₦200k per car"),
            ("automotive-repairs-maintenance", "Tyre & Vulcanizer Pro", "Tyre repair daily cash"),
            ("automotive-repairs-maintenance", "Motorcycle & Keke Business - Daily Cash", "Complete Keke repair daily cash"),
        ]

        total_c = 0
        total_l = 0
        for pillar_slug, title, desc in pillars_courses:
            try:
                cat = Category.objects.get(pillar=pillar_slug)
            except Category.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"Pillar not found: {pillar_slug}"))
                continue

            course, created = Course.objects.get_or_create(
                category=cat,
                title=title,
                defaults={
                    "description": f"{desc} - Comprehensive course for poor Africans, Aba-focused, practical, from zero to earning. Simple English + Igbo, market prices, workshop videos.",
                    "level": "beginner",
                    "age_group": "adult",
                    "learning_approach": "andragogic",
                    "duration_hours": 80,
                    "learning_objectives": f"After this, you can start business in Aba, charge customers, make daily income. {desc}",
                    "is_active": True,
                    "featured": True
                }
            )
            if created:
                total_c += 1
            if course.lessons.count() < 10:
                for idx, (lt, ct) in enumerate(lessons_template, 1):
                    Lesson.objects.get_or_create(
                        course=course, order=idx,
                        defaults={
                            "title": f"{idx}. {lt}",
                            "content": f"FULL DETAILED LESSON: {lt} for {title}. Includes step by step, tools with Ariaria prices, safety, common mistakes, how to charge customer, real Aba workshop video. Simple English + Igbo. Goal: Earn money immediately. For poor Africans.",
                            "content_type": ct,
                            "duration_minutes": 45
                        }
                    )
                    total_l += 1

        self.stdout.write(self.style.SUCCESS(f"\n=== DONE: {total_c} new courses, {total_l} lessons ==="))
        self.stdout.write(self.style.SUCCESS(f"TOTAL: {Course.objects.filter(is_active=True).count()} courses, {Lesson.objects.count()} lessons"))