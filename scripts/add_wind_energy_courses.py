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
print("🌬️ ADDING WIND ENERGY COURSES")
print("="*70)

# Get categories
categories = {}
for cat in Category.objects.all():
    categories[cat.pillar] = cat

wind_courses = [
    {
        'title': 'Wind Energy Technology - Complete Guide',
        'category': 'vocational',
        'description': 'Complete wind energy technology - evolution, types, uses, advantages, disadvantages, and modern innovations. From traditional windmills to modern wind turbines.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 25,
        'objectives': 'Master wind energy technology, selection, and application'
    },
    {
        'title': 'Wind Turbine Types and Selection',
        'category': 'vocational',
        'description': 'Wind turbine types - horizontal axis, vertical axis, offshore, onshore. Advantages, disadvantages, and selection criteria for different applications.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 20,
        'objectives': 'Master wind turbine selection and application'
    },
    {
        'title': 'Wind Turbine Installation and Maintenance',
        'category': 'vocational',
        'description': 'Professional wind turbine installation - site assessment, foundation, tower erection, turbine assembly, and ongoing maintenance procedures.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'andragogic',
        'duration': 30,
        'objectives': 'Master wind turbine installation and maintenance'
    },
    {
        'title': 'Modern Wind Energy Technology - Innovations',
        'category': 'vocational',
        'description': 'Modern wind energy innovations - floating wind turbines, smart wind farms, energy storage integration, and emerging wind technologies.',
        'level': 'advanced',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 20,
        'objectives': 'Master modern wind energy innovations and emerging technologies'
    },
    {
        'title': 'Wind Farm Design and Management',
        'category': 'vocational',
        'description': 'Wind farm design - site selection, layout, turbine placement, grid connection, and operational management of wind farms.',
        'level': 'advanced',
        'age_group': 'adult',
        'approach': 'heutagogic',
        'duration': 25,
        'objectives': 'Master wind farm design and operational management'
    },
    {
        'title': 'Wind-Solar Hybrid Systems',
        'category': 'vocational',
        'description': 'Hybrid renewable energy systems - integrating wind and solar for reliable power supply, complementary generation, and hybrid system design.',
        'level': 'advanced',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 25,
        'objectives': 'Master wind-solar hybrid system design and implementation'
    },
    {
        'title': 'Wind Energy Economics and Policy',
        'category': 'vocational',
        'description': 'Wind energy economics - cost analysis, financing, ROI, government policies, incentives, and renewable energy regulations.',
        'level': 'advanced',
        'age_group': 'adult',
        'approach': 'heutagogic',
        'duration': 20,
        'objectives': 'Master wind energy economics and policy frameworks'
    },
]

# Add wind courses
total_added = 0

for course_data in wind_courses:
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
print(f"📊 Total Wind Energy Courses Added: {total_added}")
print(f"📚 Total Courses in Database: {Course.objects.filter(is_active=True).count()}")
print("🎉 Wind energy course addition complete!")