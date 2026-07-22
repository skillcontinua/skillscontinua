import os
import sys
import django

project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from courses.models import Category

print("="*60)
print("📚 AVAILABLE CATEGORIES")
print("="*60)

for cat in Category.objects.all():
    print(f"  {cat.pillar}: {cat.name}")

print("="*60)