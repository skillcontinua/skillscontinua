from django.core.management.base import BaseCommand
from courses.models import Category

class Command(BaseCommand):
    def handle(self, *args, **options):
        cats = Category.objects.all().order_by('order', 'id')
        print(f"\n--- {cats.count()} CATEGORIES IN DB ---")
        for c in cats:
            count = c.courses.filter(is_active=True).count()
            print(f"ID {c.id} | Order {c.order} | {c.icon} {c.name} | {count} courses")
        print("\n---")