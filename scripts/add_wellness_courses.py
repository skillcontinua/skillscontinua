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
print("🧘 ADDING WELLNESS COURSES")
print("="*70)

# First, create Wellness category if it doesn't exist
wellness_category, created = Category.objects.get_or_create(
    pillar='wellness',
    defaults={
        'name': 'Wellness and Holistic Health',
        'description': 'Complete wellness and holistic health - Tai Chi, meditation, yoga, and holistic health practices.'
    }
)

if created:
    print(f"✅ Created category: {wellness_category.name}")
else:
    print(f"📚 Category already exists: {wellness_category.name}")

# Reload categories dictionary after creating new category
categories = {}
for cat in Category.objects.all():
    categories[cat.pillar] = cat

# Now use the category
category = categories.get('wellness')

if category:
    print(f"✅ Using category: {category.name}")

wellness_courses = [
    {
        'title': 'Tai Chi - Complete Guide',
        'category': 'wellness',
        'description': 'Complete Tai Chi - history, philosophy, forms, health benefits, and mastering Tai Chi for physical and mental wellness.',
        'level': 'beginner',
        'age_group': 'all',
        'approach': 'andragogic',
        'duration': 25,
        'objectives': 'Master Tai Chi for health and wellness'
    },
    {
        'title': 'Advanced Tai Chi and Qigong',
        'category': 'wellness',
        'description': 'Advanced Tai Chi and Qigong - complex forms, energy cultivation, and advanced health applications.',
        'level': 'advanced',
        'age_group': 'adult',
        'approach': 'heutagogic',
        'duration': 25,
        'objectives': 'Master advanced Tai Chi and Qigong practices'
    },
    {
        'title': 'Meditation and Mindfulness',
        'category': 'wellness',
        'description': 'Meditation and mindfulness - techniques, practices, health benefits, and incorporating mindfulness into daily life.',
        'level': 'beginner',
        'age_group': 'all',
        'approach': 'andragogic',
        'duration': 15,
        'objectives': 'Master meditation and mindfulness practices'
    },
    {
        'title': 'Yoga - Complete Guide',
        'category': 'wellness',
        'description': 'Complete yoga - history, philosophy, postures, breathing techniques, and yoga for health and wellness.',
        'level': 'beginner',
        'age_group': 'all',
        'approach': 'andragogic',
        'duration': 25,
        'objectives': 'Master yoga for physical and mental wellness'
    },
    {
        'title': 'Advanced Yoga and Pranayama',
        'category': 'wellness',
        'description': 'Advanced yoga - complex postures, advanced breathing techniques, meditation, and holistic health practices.',
        'level': 'advanced',
        'age_group': 'adult',
        'approach': 'heutagogic',
        'duration': 25,
        'objectives': 'Master advanced yoga and pranayama techniques'
    },
    {
        'title': 'Holistic Health and Wellness',
        'category': 'wellness',
        'description': 'Holistic health - nutrition, exercise, stress management, sleep, and creating a balanced healthy lifestyle.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'andragogic',
        'duration': 20,
        'objectives': 'Master holistic health and wellness practices'
    },
    {
        'title': 'Stress Management and Relaxation',
        'category': 'wellness',
        'description': 'Stress management - techniques, relaxation practices, and building resilience for a balanced life.',
        'level': 'beginner',
        'age_group': 'all',
        'approach': 'andragogic',
        'duration': 15,
        'objectives': 'Master stress management and relaxation techniques'
    },
    {
        'title': 'Mind-Body Connection and Health',
        'category': 'wellness',
        'description': 'Mind-body connection - understanding the relationship between mental and physical health, and practices for optimal well-being.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'heutagogic',
        'duration': 20,
        'objectives': 'Master mind-body connection for optimal health'
    },
]

# Add courses
total_added = 0

for course_data in wellness_courses:
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
print(f"📊 Total Wellness Courses Added: {total_added}")
print(f"📚 Total Courses in Database: {Course.objects.filter(is_active=True).count()}")
print("🎉 Wellness course addition complete!")