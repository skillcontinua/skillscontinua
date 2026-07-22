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
print("🌱 ADDING ADVANCED AGRICULTURE COURSES")
print("="*70)

# Get categories
categories = {}
for cat in Category.objects.all():
    categories[cat.pillar] = cat

agriculture_courses = [
    {
        'title': 'Hydroponics - Modern Growing Systems',
        'category': 'agriculture',
        'description': 'Complete hydroponics training - NFT, DWC, aeroponics, drip systems, nutrient solutions, pH management, and modern soilless growing techniques.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 25,
        'objectives': 'Master hydroponics and modern soilless growing systems'
    },
    {
        'title': 'Vertical Farming Technology',
        'category': 'agriculture',
        'description': 'Vertical farming - indoor farming, LED lighting, climate control, automated systems, and commercial vertical farming operations.',
        'level': 'advanced',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 25,
        'objectives': 'Master vertical farming technology and operations'
    },
    {
        'title': 'Smart Agriculture and IoT',
        'category': 'agriculture',
        'description': 'Smart agriculture - IoT sensors, automated irrigation, drone monitoring, data analytics, and precision farming technologies.',
        'level': 'advanced',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 25,
        'objectives': 'Master smart agriculture and IoT farming technologies'
    },
    {
        'title': 'Aquaponics - Sustainable Food Production',
        'category': 'agriculture',
        'description': 'Complete aquaponics - fish farming, plant cultivation, water quality management, system design, and sustainable food production.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'andragogic',
        'duration': 25,
        'objectives': 'Master aquaponics and sustainable food production'
    },
    {
        'title': 'Organic Farming Certification Preparation',
        'category': 'agriculture',
        'description': 'Organic farming - soil management, organic fertilizers, pest control, crop rotation, and organic certification preparation.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'andragogic',
        'duration': 20,
        'objectives': 'Master organic farming practices and certification'
    },
    {
        'title': 'Agricultural Business Management',
        'category': 'agriculture',
        'description': 'Agricultural business - farm planning, financial management, marketing, supply chain, and agribusiness management.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'heutagogic',
        'duration': 20,
        'objectives': 'Master agricultural business management'
    },
    {
        'title': 'Greenhouse Technology and Climate Control',
        'category': 'agriculture',
        'description': 'Greenhouse technology - climate control, automated systems, irrigation, pest control, and commercial greenhouse operations.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 20,
        'objectives': 'Master greenhouse technology and climate control'
    },
    {
        'title': 'Agribusiness Export and Market Access',
        'category': 'agriculture',
        'description': 'Agribusiness export - market access, quality standards, certification, logistics, and international agricultural trade.',
        'level': 'advanced',
        'age_group': 'adult',
        'approach': 'heutagogic',
        'duration': 20,
        'objectives': 'Master agribusiness export and market access'
    },
]

# Add agriculture courses
total_added = 0

for course_data in agriculture_courses:
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
print(f"📊 Total Agriculture Courses Added: {total_added}")
print(f"📚 Total Courses in Database: {Course.objects.filter(is_active=True).count()}")
print("🎉 Agriculture course addition complete!")