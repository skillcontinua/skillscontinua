from django.core.management.base import BaseCommand
from courses.models import Category, Course
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Create 14 FINAL Pillars'

    def handle(self, *args, **options):
        # Clean old empty categories already done, now only ID11 left
        # Delete any categories with empty pillar duplicates
        try:
            # Try to clear pillar constraint by setting unique pillar values
            for cat in Category.objects.all():
                if not cat.pillar or cat.pillar == '':
                    cat.pillar = slugify(cat.name)[:50]
                    # Ensure unique
                    base = cat.pillar
                    counter = 1
                    while Category.objects.filter(pillar=cat.pillar).exclude(id=cat.id).exists():
                        cat.pillar = f"{base}-{counter}"
                        counter += 1
                    cat.save()
        except Exception as e:
            self.stdout.write(self.style.WARNING(f"Pillar fix attempt: {e}"))

        pillars_14 = [
            {"order": 1, "slug": "renewable-energy-solar", "name": "RENEWABLE ENERGY & SOLAR", "icon": "☀️", "desc": "Solar Installation, Inverter & Battery, Solar Business"},
            {"order": 2, "slug": "technology-software", "name": "TECHNOLOGY & SOFTWARE", "icon": "💻", "desc": "Web Dev, Mobile App, UI/UX, Cybersecurity, AI & ChatGPT"},
            {"order": 3, "slug": "trades-craftsmanship", "name": "TRADES & CRAFTSMANSHIP", "icon": "🛠️", "desc": "Tailoring, Carpentry, Welding, Plumbing, Electrical, Tiling"},
            {"order": 4, "slug": "agriculture-agro-business", "name": "AGRICULTURE & AGRO-BUSINESS", "icon": "🌾", "desc": "Poultry, Fish Farming, Snail, Export Business"},
            {"order": 5, "slug": "business-entrepreneurship", "name": "BUSINESS & ENTREPRENEURSHIP", "icon": "💼", "desc": "Start Business, Sales & Marketing, Import/Export"},
            {"order": 6, "slug": "digital-marketing-content", "name": "DIGITAL MARKETING & CONTENT", "icon": "📱", "desc": "Facebook Ads, Google Ads, TikTok, Content Creation"},
            {"order": 7, "slug": "health-wellness", "name": "HEALTH & WELLNESS", "icon": "❤️", "desc": "First Aid, Nursing Assistant, Fitness, Nutrition"},
            {"order": 8, "slug": "education-teaching", "name": "EDUCATION & TEACHING", "icon": "🎓", "desc": "Nursery Teaching, JAMB Tutoring, Online Teaching"},
            {"order": 9, "slug": "finance-professional", "name": "FINANCE & PROFESSIONAL SERVICES", "icon": "💰", "desc": "Accounting, Tax, Investment, Real Estate, Logistics"},
            {"order": 10, "slug": "media-creative-arts", "name": "MEDIA & CREATIVE ARTS", "icon": "🎭", "desc": "Music, Photography, Cinematography, African Heritage"},
            {"order": 11, "slug": "transport-logistics", "name": "TRANSPORT & LOGISTICS", "icon": "🚚", "desc": "Ride Hailing, Trucking, Shipping, Delivery Business"},
            {"order": 12, "slug": "beauty-personal-care", "name": "BEAUTY & PERSONAL CARE", "icon": "💄", "desc": "Barbering, Hairdressing, Makeup, Nail Tech, Skincare"},
            {"order": 13, "slug": "government-social-impact", "name": "GOVERNMENT & SOCIAL IMPACT", "icon": "🤝", "desc": "NGO Management, Grant Writing, Leadership, Returnee Support"},
            {"order": 14, "slug": "automotive-repairs-maintenance", "name": "AUTOMOTIVE REPAIRS & MAINTENANCE", "icon": "🚗", "desc": "Keke, Okada, Car, Diagnostics, Generator - Most Profitable in Aba!"},
        ]

        for p in pillars_14:
            # Try get by pillar slug first (unique field)
            cat = Category.objects.filter(pillar=p["slug"]).first()
            if not cat:
                cat = Category.objects.filter(name=p["name"]).first()
            
            if cat:
                cat.name = p["name"]
                cat.pillar = p["slug"]
                cat.icon = p["icon"]
                cat.description = p["desc"]
                cat.order = p["order"]
                cat.save()
                self.stdout.write(f'Updated {p["order"]:02d}. {p["name"]}')
            else:
                try:
                    cat = Category.objects.create(
                        name=p["name"],
                        pillar=p["slug"],
                        icon=p["icon"],
                        description=p["desc"],
                        order=p["order"]
                    )
                    self.stdout.write(self.style.SUCCESS(f'Created {p["order"]:02d}. {p["name"]}'))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Failed {p["name"]}: {e}'))

        print(f"\n--- FINAL {Category.objects.count()} PILLARS ---")
        for c in Category.objects.all().order_by('order'):
            cnt = c.courses.filter(is_active=True).count()
            print(f"{c.order:02d}. {c.icon} {c.name} | pillar={c.pillar} | {cnt} courses")