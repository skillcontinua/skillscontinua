import os
import sys
import django

# Add project root to path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from courses.models import Category

print("="*70)
print("📁 ADDING MISSING CATEGORIES")
print("="*70)

# Categories to add
new_categories = [
    {
        'pillar': 'animal_husbandry',
        'name': 'Animal Husbandry',
        'description': 'Complete animal husbandry - fishery, poultry, piggery, beekeeping, cattle, and livestock management.'
    },
    {
        'pillar': 'leather_work',
        'name': 'Leather Work and Tanning',
        'description': 'Leather tanning, processing, and craft - hides, skins, and leather product manufacturing.'
    },
    {
        'pillar': 'dairy',
        'name': 'Dairy Production',
        'description': 'Dairy production - milk processing, cheese making, yogurt production, and dairy product marketing.'
    },
    {
        'pillar': 'beekeeping',
        'name': 'Beekeeping and Apiary',
        'description': 'Beekeeping - honey production, hive management, queen rearing, and apiary business.'
    },
    {
        'pillar': 'blockchain',
        'name': 'Blockchain Technology',
        'description': 'Blockchain technology, cryptocurrency, smart contracts, and decentralized applications.'
    },
    {
        'pillar': 'artificial_intelligence',
        'name': 'Artificial Intelligence',
        'description': 'Artificial Intelligence, machine learning, ChatGPT, and generative AI applications.'
    },
    {
        'pillar': 'cloud_computing',
        'name': 'Cloud Computing',
        'description': 'Cloud computing - AWS, Google Cloud, Azure, and cloud services deployment.'
    },
    {
        'pillar': 'wind_energy',
        'name': 'Wind Energy',
        'description': 'Wind energy technology - turbines, installation, maintenance, and wind farm management.'
    },
    {
        'pillar': 'printing_technology',
        'name': 'Printing Technology',
        'description': 'Printing technology - offset, digital, screen, 3D printing, and print production.'
    },
]

# Add categories
total_added = 0

for cat_data in new_categories:
    cat, created = Category.objects.get_or_create(
        pillar=cat_data['pillar'],
        defaults={
            'name': cat_data['name'],
            'description': cat_data['description']
        }
    )
    if created:
        total_added += 1
        print(f"✅ Created: {cat.name} ({cat.pillar})")
    else:
        print(f"📚 Already exists: {cat.name} ({cat.pillar})")

print("\n" + "="*70)
print(f"📊 Total Categories Added: {total_added}")
print(f"📚 Total Categories: {Category.objects.count()}")
print("🎉 Category addition complete!")