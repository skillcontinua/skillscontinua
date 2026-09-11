from django.core.management.base import BaseCommand
from courses.models import Category, Course

class Command(BaseCommand):
    help = 'Seed 14th Pillar: Automotive Repairs and Maintenance'

    def handle(self, *args, **options):
        # Use 'name' because Category has no slug - confirmed from error
        cat, created = Category.objects.get_or_create(
            name='AUTOMOTIVE REPAIRS & MAINTENANCE',
            defaults={
                'description': 'Aba Keke & Motor Repair Hub - Most profitable skills in Ariaria',
                'icon': '🚗',
                'order': 14,
            }
        )
        if not created:
            cat.description = 'Aba Keke & Motor Repair Hub - Most profitable skills in Ariaria'
            cat.icon = '🚗'
            cat.order = 14
            cat.save()
            self.stdout.write(self.style.WARNING(f'Updated category: {cat.name} (ID {cat.id})'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Created category: {cat.name} (ID {cat.id})'))

        automotive_courses = [
            {"title": "Motorcycle & Keke NAPEP Repair - Complete", "duration": 120, "level": "beginner", "desc": "Complete repair of Okada & Keke - engine, gearbox, wiring. Daily cash in Aba!", "featured": True},
            {"title": "Automotive Electrical & Wiring - Aba Method", "duration": 80, "level": "intermediate", "desc": "Fix all electrical faults, lighting, starter, alternator - no more push-start!", "featured": True},
            {"title": "Carburetor & Fuel System Specialist", "duration": 60, "level": "beginner", "desc": "Clean, tune, repair carburetor for Toyota, Honda, Keke. Save fuel!", "featured": True},
            {"title": "Auto Diagnostics with OBD Scanner", "duration": 40, "level": "intermediate", "desc": "Use OBD2 scanner to diagnose check engine - charge ₦5k per scan in Ariaria", "featured": True},
            {"title": "Engine Overhaul & Ringing", "duration": 100, "level": "advanced", "desc": "Complete engine rebuild - Toyota, Nissan, Keke. Most respected skill in Aba", "featured": False},
            {"title": "Brake & Suspension Systems - Safety First", "duration": 50, "level": "beginner", "desc": "Fix brake pads, shock absorbers, ball joints - safety is money", "featured": False},
            {"title": "Generator & Small Engine Repair", "duration": 45, "level": "beginner", "desc": "Repair I-better-pass my neighbor, Tiger generators - every home needs you!", "featured": False},
            {"title": "Tyre & Wheel Alignment - Vulcanizer Pro", "duration": 30, "level": "beginner", "desc": "Professional tyre repair, alignment, balancing - open shop at Faulks Road", "featured": False},
        ]

        created_count = 0
        for c in automotive_courses:
            course, is_new = Course.objects.get_or_create(
                title=c["title"],
                defaults={
                    'category': cat,
                    'description': c["desc"],
                    'duration_hours': c["duration"],
                    'level': c["level"],
                    'learning_approach': 'hands-on',
                    'is_active': True,
                    'featured': c["featured"],
                }
            )
            if is_new:
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f'  + Created: {c["title"]}'))
            else:
                course.category = cat
                course.is_active = True
                course.save()
                self.stdout.write(f'  - Exists: {c["title"]} - updated category')

        self.stdout.write(self.style.SUCCESS(f'\n✅ 14th PILLAR READY! {created_count} new courses added to {cat.name}'))
        self.stdout.write(self.style.SUCCESS(f'Total active courses in 14th pillar: {Course.objects.filter(category=cat, is_active=True).count()}'))
        self.stdout.write(self.style.SUCCESS(f'Total categories now: {Category.objects.count()}'))