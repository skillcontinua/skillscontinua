import os
import sys
import django

# Add project root to path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from courses.models import Category, Course

print("="*70)
print("📦 MOVING COURSES TO CORRECT CATEGORIES")
print("="*70)

# Get all categories
categories = {}
for cat in Category.objects.all():
    categories[cat.name] = cat
    categories[cat.pillar] = cat

# Course mappings - which category they should be in
course_mappings = {
    # Animal Husbandry courses
    'Fish Farming - Complete Guide': 'Animal Husbandry',
    'Aquaculture and Fish Processing': 'Animal Husbandry',
    'Catfish Farming - Production and Marketing': 'Animal Husbandry',
    'Poultry Farming - Complete Guide': 'Animal Husbandry',
    'Broiler Production and Management': 'Animal Husbandry',
    'Layer Production and Egg Processing': 'Animal Husbandry',
    'Piggery Farming - Complete Guide': 'Animal Husbandry',
    'Breeding and Farrowing Management': 'Animal Husbandry',
    'Beekeeping and Honey Production': 'Beekeeping and Apiary',
    'Advanced Beekeeping and Apiary Management': 'Beekeeping and Apiary',
    'Cattle Rearing and Herd Management': 'Animal Husbandry',
    'Dairy Production and Milk Processing': 'Dairy Production',
    'Cheese and Yogurt Making': 'Dairy Production',
    
    # Leather courses
    'Leather Tanning and Processing': 'Leather Work and Tanning',
    'Leather Craft and Product Making': 'Leather Work and Tanning',
    'Shoe and Bag Making': 'Leather Work and Tanning',
    
    # Wind Energy
    'Wind Energy Technology - Complete Guide': 'Wind Energy',
    'Wind Turbine Types and Selection': 'Wind Energy',
    'Wind Turbine Installation and Maintenance': 'Wind Energy',
    'Modern Wind Energy Technology - Innovations': 'Wind Energy',
    'Wind Farm Design and Management': 'Wind Energy',
    'Wind-Solar Hybrid Systems': 'Wind Energy',
    'Wind Energy Economics and Policy': 'Wind Energy',
    
    # Printing Technology
    'Printing Technology - Complete Guide': 'Printing Technology',
    'Offset Printing - Traditional and Modern': 'Printing Technology',
    'Digital Printing Technology': 'Printing Technology',
    'Screen Printing - Techniques and Applications': 'Printing Technology',
    '3D Printing Technology - Complete Guide': 'Printing Technology',
    'Printing Materials and Inks': 'Printing Technology',
    'Print Finishing and Binding': 'Printing Technology',
    'Color Management in Printing': 'Printing Technology',
    'Prepress and Print Production Workflow': 'Printing Technology',
    'Printing Business Management and Marketing': 'Printing Technology',
    
    # Blockchain, AI, Cloud
    'Blockchain Technology - Complete Guide': 'Blockchain Technology',
    'Cryptocurrency and Digital Finance': 'Blockchain Technology',
    'Smart Contracts and Decentralized Applications': 'Blockchain Technology',
    'Artificial Intelligence Fundamentals': 'Artificial Intelligence',
    'Machine Learning - Complete Guide': 'Artificial Intelligence',
    'ChatGPT and Generative AI': 'Artificial Intelligence',
    'Cloud Computing - Complete Guide': 'Cloud Computing',
    'Amazon Web Services (AWS) Fundamentals': 'Cloud Computing',
    'Google Cloud Platform (GCP) Fundamentals': 'Cloud Computing',
    'Microsoft Azure Fundamentals': 'Cloud Computing',
}

# Move courses
total_moved = 0
total_not_found = 0

for course_title, category_name in course_mappings.items():
    try:
        course = Course.objects.get(title=course_title)
        category = categories.get(category_name)
        
        if category:
            old_category = course.category.name
            course.category = category
            course.save()
            total_moved += 1
            print(f"✅ Moved: {course_title} -> {category_name} (from {old_category})")
        else:
            print(f"⚠️ Category '{category_name}' not found")
            total_not_found += 1
            
    except Course.DoesNotExist:
        print(f"⚠️ Course '{course_title}' not found")
        total_not_found += 1

print("\n" + "="*70)
print(f"📊 Courses Moved: {total_moved}")
print(f"📚 Courses Not Found: {total_not_found}")
print("🎉 Course relocation complete!")