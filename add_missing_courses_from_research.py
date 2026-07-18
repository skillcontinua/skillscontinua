import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from courses.models import Category, Course

print("🔍 Adding MISSING COURSES from research...")
print("="*60)

# Get categories
categories = {}
for cat in Category.objects.all():
    categories[cat.pillar] = cat
    categories[cat.name.lower()] = cat

# Additional missing courses identified from research
research_courses = [
    # ===== MARINE & BOAT (Already added - keeping for reference) =====
    # These are already added via add_marine_courses.py
    
    # ===== ADDITIONAL MISSING AREAS =====
    {
        'title': 'Renewable Energy Systems',
        'category': 'technology',
        'description': 'Comprehensive renewable energy - solar, wind, hydro, and biomass systems for sustainable energy solutions.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 30,
        'objectives': 'Master renewable energy systems and sustainable energy solutions'
    },
    {
        'title': 'Solar Panel Installation and Maintenance',
        'category': 'technology',
        'description': 'Professional solar panel installation - system design, installation, maintenance, and troubleshooting.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 25,
        'objectives': 'Master solar panel installation and maintenance'
    },
    {
        'title': 'Climate Change and Environmental Awareness',
        'category': 'life_skills',
        'description': 'Understanding climate change, environmental challenges, and sustainable practices for communities.',
        'level': 'beginner',
        'age_group': 'all',
        'approach': 'andragogic',
        'duration': 15,
        'objectives': 'Master climate change awareness and sustainable practices'
    },
    {
        'title': 'First Aid and Emergency Response',
        'category': 'life_skills',
        'description': 'Complete first aid training - CPR, wound care, emergency response, and life-saving techniques.',
        'level': 'beginner',
        'age_group': 'all',
        'approach': 'andragogic',
        'duration': 20,
        'objectives': 'Master first aid and emergency response skills'
    },
    {
        'title': 'Mental Health Awareness and Support',
        'category': 'life_skills',
        'description': 'Understanding mental health, common conditions, support techniques, and community mental health.',
        'level': 'beginner',
        'age_group': 'all',
        'approach': 'andragogic',
        'duration': 15,
        'objectives': 'Master mental health awareness and support skills'
    },
    {
        'title': 'Blockchain and Cryptocurrency Fundamentals',
        'category': 'computer',
        'description': 'Blockchain technology, cryptocurrency basics, decentralized finance, and practical applications.',
        'level': 'advanced',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 25,
        'objectives': 'Master blockchain and cryptocurrency fundamentals'
    },
    {
        'title': '3D Printing and Additive Manufacturing',
        'category': 'technology',
        'description': '3D printing technology - design, operation, materials, and practical applications in manufacturing.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 20,
        'objectives': 'Master 3D printing and additive manufacturing'
    },
    {
        'title': 'Game Development Fundamentals',
        'category': 'computer',
        'description': 'Game development - design, programming, art, and production of digital games.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 30,
        'objectives': 'Master game development fundamentals'
    },
    {
        'title': 'Sustainable Agriculture Practices',
        'category': 'agriculture',
        'description': 'Sustainable farming, organic practices, permaculture, and eco-friendly agricultural methods.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'andragogic',
        'duration': 25,
        'objectives': 'Master sustainable agriculture practices'
    },
    {
        'title': 'Hydroponics and Vertical Farming',
        'category': 'agriculture',
        'description': 'Hydroponics, aquaponics, vertical farming, and modern food production techniques.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 20,
        'objectives': 'Master hydroponics and vertical farming'
    },
]

# Add research courses
total_added = 0
for course_data in research_courses:
    # Try to find category by pillar or name
    category = None
    if course_data['category'] in categories:
        category = categories[course_data['category']]
    else:
        for cat in Category.objects.all():
            if course_data['category'].lower() in cat.name.lower():
                category = cat
                break
    
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
print(f"📊 Research Courses Added: {total_added}")
print(f"📚 Total Courses in Database: {Course.objects.filter(is_active=True).count()}")
print("🎉 Research course addition complete!")