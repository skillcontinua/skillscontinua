from django.core.management.base import BaseCommand
from courses.models import Category, Course

class Command(BaseCommand):
    def handle(self, *args, **options):
        auto_cat, created = Category.objects.get_or_create(
            pillar="AUTOMOTIVE_REPAIRS",
            defaults={
                'name': 'Automotive Repairs & Maintenance',
                'description': 'Car repairs, diagnostics, electrical, engine, panel beating for Aba youth',
                'icon': '🚗',
                'order': 10,
                'name_en': 'Automotive Repairs & Maintenance',
            }
        )
        courses_data = [
            {'title': 'Basic Car Maintenance & Servicing', 'desc': 'Oil change, brake pads, daily checks', 'hours': 40, 'level': 'beginner'},
            {'title': 'Engine Diagnostics & OBD Scanner', 'desc': 'OBD2 scanner, fault codes Toyota Honda Kia', 'hours': 60, 'level': 'intermediate'},
            {'title': 'Auto Electrical & Wiring', 'desc': 'Battery, alternator, starter, lighting wiring', 'hours': 50, 'level': 'intermediate'},
            {'title': 'Panel Beating & Spray Painting', 'desc': 'Body work, dent removal, painting Aba', 'hours': 80, 'level': 'beginner'},
            {'title': 'Motorcycle & Keke Repair (Tricycle)', 'desc': 'Okada Keke engine clutch most profitable', 'hours': 45, 'level': 'beginner'},
            {'title': 'Wheel Alignment, Balancing & Vulcanizing', 'desc': 'Vulcanizer shop, alignment machine daily cash', 'hours': 30, 'level': 'beginner'},
            {'title': 'Auto AC Repair & Refrigeration', 'desc': 'Car AC gas compressor repair', 'hours': 50, 'level': 'advanced'},
        ]
        for data in courses_data:
            Course.objects.get_or_create(
                title=data['title'],
                category=auto_cat,
                defaults={
                    'description': data['desc'],
                    'duration_hours': data['hours'],
                    'level': data['level'],
                    'age_group': 'all',
                    'learning_approach': 'heutagogic',
                    'is_active': True,
                    'featured': True,
                    'target_audience': 'Youth in Aba',
                    'prerequisites': 'No experience',
                    'learning_objectives': data['desc'],
                }
            )
        self.stdout.write(self.style.SUCCESS(f"✅ Automotive done! Total: {Course.objects.count()}"))