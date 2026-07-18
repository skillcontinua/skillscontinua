import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from courses.models import Category, Course

print("🚤 Adding MARINE & BOAT ENGINE COURSES...")
print("="*60)

# Get categories
categories = {}
for cat in Category.objects.all():
    categories[cat.pillar] = cat
    categories[cat.name.lower()] = cat

# Marine courses
marine_courses = [
    {
        'title': 'Boat Engine Repair and Maintenance',
        'category': 'vocational',
        'description': 'Complete boat engine repair - inboard engines, outboard motors, diagnostics, fuel systems, and marine engine maintenance.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'andragogic',
        'duration': 30,
        'objectives': 'Master boat engine repair and maintenance for fishing and transport vessels'
    },
    {
        'title': 'Outboard Motor Repair Fundamentals',
        'category': 'vocational',
        'description': 'Professional outboard motor repair - 2-stroke and 4-stroke engines, carburetor repair, electrical systems, and troubleshooting.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'andragogic',
        'duration': 25,
        'objectives': 'Master outboard motor repair for small boats and fishing vessels'
    },
    {
        'title': 'Marine Engine Diagnostics',
        'category': 'vocational',
        'description': 'Advanced marine engine diagnostics - electronic fuel injection, computer diagnostics, sensor testing, and fault finding.',
        'level': 'advanced',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 25,
        'objectives': 'Master marine engine diagnostics using modern tools'
    },
    {
        'title': 'Boat Building and Repair',
        'category': 'vocational',
        'description': 'Complete boat building and repair - fiberglass repair, woodworking, welding, hull repair, and vessel maintenance.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'andragogic',
        'duration': 35,
        'objectives': 'Master boat construction and repair techniques'
    },
    {
        'title': 'Marine Electrical Systems',
        'category': 'vocational',
        'description': 'Marine electrical systems - wiring, navigation systems, lighting, battery systems, and solar power for boats.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 25,
        'objectives': 'Master marine electrical systems and installation'
    },
    {
        'title': 'Canoe and Kayak Maintenance',
        'category': 'vocational',
        'description': 'Canoe and kayak maintenance - repair, fiberglass work, painting, and winter storage for small watercraft.',
        'level': 'beginner',
        'age_group': 'adult',
        'approach': 'andragogic',
        'duration': 15,
        'objectives': 'Master canoe and kayak maintenance and repair'
    },
    {
        'title': 'Navigation and Marine Safety',
        'category': 'life_skills',
        'description': 'Marine navigation - chart reading, GPS usage, weather interpretation, and maritime safety protocols.',
        'level': 'beginner',
        'age_group': 'adult',
        'approach': 'andragogic',
        'duration': 20,
        'objectives': 'Master navigation and marine safety skills'
    },
]

# Add courses
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
            print(f"✅ Added: {course.title} ({course_data['approach'].upper()})")
        else:
            print(f"📚 Already exists: {course.title}")
    else:
        print(f"⚠️ Category '{course_data['category']}' not found")

print("\n" + "="*60)
print(f"📊 Marine Courses Added: {total_added}")
print(f"📚 Total Courses in Database: {Course.objects.filter(is_active=True).count()}")
print("🎉 Marine course addition complete!")