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
print("🚤 ADDING ADVANCED MARINE & AUTOMOTIVE MARINE COURSES")
print("="*70)

# Get categories
categories = {}
for cat in Category.objects.all():
    categories[cat.pillar] = cat

# Marine Engine Courses
marine_courses = [
    {
        'title': 'Marine Engine Systems - Complete Guide',
        'category': 'auto_marine',
        'description': 'Complete marine engine systems - inboard engines, outboard motors, stern drives, and marine propulsion systems. Functions, repair, and maintenance.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'andragogic',
        'duration': 30,
        'objectives': 'Master marine engine systems, repair, and maintenance'
    },
    {
        'title': 'Outboard Motor Repair - Advanced',
        'category': 'auto_marine',
        'description': 'Advanced outboard motor repair - two-stroke and four-stroke engines, fuel systems, ignition, electrical, and advanced diagnostics.',
        'level': 'advanced',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 30,
        'objectives': 'Master advanced outboard motor repair and diagnostics'
    },
    {
        'title': 'Marine Fuel Systems and Carburetion',
        'category': 'auto_marine',
        'description': 'Marine fuel systems - carburetors, fuel injection, fuel pumps, filters, and troubleshooting fuel-related issues in marine engines.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'andragogic',
        'duration': 25,
        'objectives': 'Master marine fuel systems and carburetion'
    },
    {
        'title': 'Marine Electrical Systems',
        'category': 'auto_marine',
        'description': 'Marine electrical systems - wiring, navigation systems, lighting, battery systems, solar integration, and troubleshooting marine electrical issues.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 25,
        'objectives': 'Master marine electrical systems and installation'
    },
    {
        'title': 'Marine Cooling and Exhaust Systems',
        'category': 'auto_marine',
        'description': 'Marine cooling and exhaust systems - raw water cooling, closed cooling systems, heat exchangers, exhaust manifolds, and marine exhaust systems.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'andragogic',
        'duration': 20,
        'objectives': 'Master marine cooling and exhaust systems'
    },
    {
        'title': 'Boat Construction and Hull Repair',
        'category': 'auto_marine',
        'description': 'Complete boat construction and hull repair - fiberglass repair, wood boat repair, aluminium welding, and modern boat building techniques.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'andragogic',
        'duration': 30,
        'objectives': 'Master boat construction and hull repair techniques'
    },
    {
        'title': 'Marine Propulsion Systems',
        'category': 'auto_marine',
        'description': 'Marine propulsion systems - propellers, stern drives, jet drives, and modern propulsion technology. Performance optimization and maintenance.',
        'level': 'advanced',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 20,
        'objectives': 'Master marine propulsion systems and maintenance'
    },
    {
        'title': 'Marine Navigation and Safety Systems',
        'category': 'auto_marine',
        'description': 'Marine navigation and safety systems - GPS, radar, sonar, electronic charting, communication systems, and maritime safety protocols.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 20,
        'objectives': 'Master marine navigation and safety systems'
    },
]

# Add marine courses
total_added = 0

for course_data in marine_courses:
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
print(f"📊 Total Marine Courses Added: {total_added}")
print(f"📚 Total Courses in Database: {Course.objects.filter(is_active=True).count()}")
print("🎉 Marine course addition complete!")