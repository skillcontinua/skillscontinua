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
print("🚗 ADDING ADVANCED AUTOMOTIVE COURSES")
print("="*70)

# Get categories
categories = {}
for cat in Category.objects.all():
    categories[cat.pillar] = cat
    categories[cat.name.lower()] = cat

# Automotive courses - Fuel Management
fuel_courses = [
    {
        'title': 'Carburetor Systems - Complete Guide',
        'category': 'auto_cars',
        'description': 'Complete carburetor systems - types, functions, repair, maintenance, tuning, advantages, and disadvantages. Learn to diagnose and fix carburetor issues.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'andragogic',
        'duration': 25,
        'objectives': 'Master carburetor systems, repair, and maintenance for all vehicle types'
    },
    {
        'title': 'Fuel Injection Systems - Advanced',
        'category': 'auto_cars',
        'description': 'Advanced fuel injection systems - types (MPFI, GDI, CRDi), functions, repair, maintenance, diagnostics, advantages, and disadvantages.',
        'level': 'advanced',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 30,
        'objectives': 'Master fuel injection systems, diagnostics, and advanced repair techniques'
    },
    {
        'title': 'Turbocharger and Supercharger Systems',
        'category': 'auto_cars',
        'description': 'Complete turbocharger and supercharger systems - types, functions, repair, maintenance, advantages, disadvantages, and performance optimization.',
        'level': 'advanced',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 25,
        'objectives': 'Master turbocharger and supercharger systems for performance vehicles'
    },
]

# Automotive courses - Diagnostic Tools
diagnostic_courses = [
    {
        'title': 'Automotive Diagnostic Tools - Complete Guide',
        'category': 'auto_cars',
        'description': 'Complete guide to automotive diagnostic tools - OBD scanners, multimeters, oscilloscopes, smoke testers, compression testers. Functions, usage, and upgrading.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 25,
        'objectives': 'Master all automotive diagnostic tools for professional troubleshooting'
    },
    {
        'title': 'Engine Diagnostics and Troubleshooting',
        'category': 'auto_cars',
        'description': 'Complete engine diagnostics - identifying problems, using diagnostic tools, interpreting error codes, and systematic troubleshooting for all engine types.',
        'level': 'advanced',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 30,
        'objectives': 'Master engine diagnostics and systematic troubleshooting'
    },
    {
        'title': 'Vehicle Performance Optimization',
        'category': 'auto_cars',
        'description': 'Optimize vehicle performance for long-distance travel. Learn to identify potential problems, perform preventative maintenance, and prepare vehicles for long journeys.',
        'level': 'advanced',
        'age_group': 'adult',
        'approach': 'heutagogic',
        'duration': 25,
        'objectives': 'Master vehicle performance optimization for long-distance reliability'
    },
]

# Automotive courses - Electric Vehicles
ev_courses = [
    {
        'title': 'Electric Vehicle Technology - Complete',
        'category': 'auto_cars',
        'description': 'Complete electric vehicle technology - EV components, battery systems, electric motors, charging systems, diagnostics, repair, and maintenance.',
        'level': 'advanced',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 35,
        'objectives': 'Master electric vehicle technology, repair, and maintenance'
    },
    {
        'title': 'Electric Vehicle Battery Systems',
        'category': 'auto_cars',
        'description': 'EV battery systems - types, functions, repair, maintenance, battery management systems, and safety protocols for EV batteries.',
        'level': 'advanced',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 30,
        'objectives': 'Master electric vehicle battery systems and maintenance'
    },
]

# Add all courses
all_courses = fuel_courses + diagnostic_courses + ev_courses
total_added = 0

for course_data in all_courses:
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
            print(f"✅ Added: {course.title}")
        else:
            print(f"📚 Already exists: {course.title}")
    else:
        print(f"⚠️ Category '{course_data['category']}' not found")

print("\n" + "="*70)
print(f"📊 Total Automotive Courses Added: {total_added}")
print(f"📚 Total Courses in Database: {Course.objects.filter(is_active=True).count()}")
print("🎉 Automotive course addition complete!")