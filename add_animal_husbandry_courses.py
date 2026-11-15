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
print("🐄 ADDING ANIMAL HUSBANDRY & AGRICULTURE COURSES")
print("="*70)

# Get categories
categories = {}
for cat in Category.objects.all():
    categories[cat.pillar] = cat

animal_courses = [
    # === FISHERY ===
    {
        'title': 'Fish Farming - Complete Guide',
        'category': 'agriculture',
        'description': 'Complete fish farming - pond construction, fingerling production, feeding, water quality management, harvesting, and fish processing.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'andragogic',
        'duration': 25,
        'objectives': 'Master fish farming and aquaculture business'
    },
    {
        'title': 'Aquaculture and Fish Processing',
        'category': 'agriculture',
        'description': 'Advanced aquaculture - fish hatchery, feed production, disease management, processing, and value addition for fish products.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 25,
        'objectives': 'Master aquaculture and fish processing techniques'
    },
    {
        'title': 'Catfish Farming - Production and Marketing',
        'category': 'agriculture',
        'description': 'Catfish farming - breeding, feeding, pond management, harvesting, processing, and marketing catfish products.',
        'level': 'beginner',
        'age_group': 'adult',
        'approach': 'andragogic',
        'duration': 20,
        'objectives': 'Master catfish farming and marketing'
    },
    
    # === POULTRY ===
    {
        'title': 'Poultry Farming - Complete Guide',
        'category': 'agriculture',
        'description': 'Complete poultry farming - broiler and layer production, housing, feeding, health management, and egg processing.',
        'level': 'beginner',
        'age_group': 'adult',
        'approach': 'andragogic',
        'duration': 25,
        'objectives': 'Master poultry farming and egg production'
    },
    {
        'title': 'Broiler Production and Management',
        'category': 'agriculture',
        'description': 'Broiler production - day-old chick management, feeding programs, vaccination, housing, disease prevention, and processing.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'andragogic',
        'duration': 20,
        'objectives': 'Master broiler chicken production and management'
    },
    {
        'title': 'Layer Production and Egg Processing',
        'category': 'agriculture',
        'description': 'Layer production - pullet rearing, egg production, egg grading, processing, and marketing eggs for profit.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'andragogic',
        'duration': 20,
        'objectives': 'Master layer production and egg processing'
    },
    
    # === PIGGERY ===
    {
        'title': 'Piggery Farming - Complete Guide',
        'category': 'agriculture',
        'description': 'Complete piggery farming - pig breeds, housing, feeding, breeding, health management, and pork production.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'andragogic',
        'duration': 25,
        'objectives': 'Master pig farming and pork production'
    },
    {
        'title': 'Breeding and Farrowing Management',
        'category': 'agriculture',
        'description': 'Breeding and farrowing - sow management, breeding techniques, farrowing, piglet care, and lactation management.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'andragogic',
        'duration': 20,
        'objectives': 'Master pig breeding and farrowing management'
    },
    
    # === BEEKEEPING ===
    {
        'title': 'Beekeeping and Honey Production',
        'category': 'agriculture',
        'description': 'Beekeeping - bee biology, hive construction, colony management, honey extraction, and marketing honey products.',
        'level': 'beginner',
        'age_group': 'adult',
        'approach': 'andragogic',
        'duration': 20,
        'objectives': 'Master beekeeping and honey production'
    },
    {
        'title': 'Advanced Beekeeping and Apiary Management',
        'category': 'agriculture',
        'description': 'Advanced beekeeping - queen rearing, disease management, pollination services, and commercial apiary management.',
        'level': 'advanced',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 20,
        'objectives': 'Master advanced beekeeping and apiary management'
    },
    
    # === CATTLE & DAIRY ===
    {
        'title': 'Cattle Rearing and Herd Management',
        'category': 'agriculture',
        'description': 'Cattle rearing - breeds, housing, feeding, health management, herd recording, and sustainable cattle production.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'andragogic',
        'duration': 25,
        'objectives': 'Master cattle rearing and herd management'
    },
    {
        'title': 'Dairy Production and Milk Processing',
        'category': 'agriculture',
        'description': 'Dairy production - milk production, milking techniques, milk quality, processing, and value-added dairy products.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 25,
        'objectives': 'Master dairy production and milk processing'
    },
    {
        'title': 'Cheese and Yogurt Making',
        'category': 'agriculture',
        'description': 'Cheese and yogurt making - milk preparation, fermentation, cheese types, ripening, and dairy product quality control.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'andragogic',
        'duration': 20,
        'objectives': 'Master cheese and yogurt production'
    },
    
    # === HIDES & SKINS / LEATHER ===
    {
        'title': 'Leather Tanning and Processing',
        'category': 'agriculture',
        'description': 'Leather tanning - hide collection, preservation, tanning methods, finishing, and quality control in leather production.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'andragogic',
        'duration': 25,
        'objectives': 'Master leather tanning and processing techniques'
    },
    {
        'title': 'Leather Craft and Product Making',
        'category': 'agriculture',
        'description': 'Leather craft - leather products, cutting, stitching, finishing, and creating quality leather goods for the market.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'andragogic',
        'duration': 25,
        'objectives': 'Master leather craft and product making'
    },
    {
        'title': 'Shoe and Bag Making',
        'category': 'agriculture',
        'description': 'Shoe and bag making - pattern making, cutting, assembly, finishing, and producing quality footwear and bags.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'andragogic',
        'duration': 25,
        'objectives': 'Master shoe and bag making techniques'
    },
]

# Add courses
total_added = 0

for course_data in animal_courses:
    category = categories.get(course_data['category'])
    
    if category:
        course, created = Course.objects.get_or_create(
            title=course_data['title'],
            category=category,
            defaults={
                'description': course_data['description'],
                'level': course_data['level'],
                'age_group': course_data['age_group'],
                'learning_approach': course_data['approach'],
                'duration_hours': course_data['duration'],
                'learning_objectives': course_data.get('objectives', ''),
                'is_active': True,
                'featured': True,
            }
        )
        if created:
            total_added += 1
            print(f"✅ Added: {course.title} (Category: {category.name})")
        else:
            print(f"📚 Already exists: {course.title}")
    else:
        print(f"⚠️ Category '{course_data['category']}' not found")

print("\n" + "="*70)
print(f"📊 Total Animal Husbandry Courses Added: {total_added}")
print(f"📚 Total Courses in Database: {Course.objects.filter(is_active=True).count()}")
print("🎉 Animal husbandry course addition complete!")