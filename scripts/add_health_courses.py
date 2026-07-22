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
print("🏥 ADDING HEALTH & WELLNESS COURSES")
print("="*70)

# Get categories
categories = {}
for cat in Category.objects.all():
    categories[cat.pillar] = cat

health_courses = [
    {
        'title': 'First Aid and Emergency Response',
        'category': 'life_skills',
        'description': 'Complete first aid training - CPR, wound care, fracture management, choking, burns, emergency response, and life-saving techniques.',
        'level': 'beginner',
        'age_group': 'all',
        'approach': 'andragogic',
        'duration': 20,
        'objectives': 'Master first aid and emergency response skills'
    },
    {
        'title': 'Mental Health Awareness and Support',
        'category': 'life_skills',
        'description': 'Mental health awareness - common conditions, support techniques, community mental health, stigma reduction, and self-care strategies.',
        'level': 'beginner',
        'age_group': 'all',
        'approach': 'andragogic',
        'duration': 15,
        'objectives': 'Master mental health awareness and support skills'
    },
    {
        'title': 'Nutrition and Healthy Living',
        'category': 'life_skills',
        'description': 'Nutrition fundamentals - balanced diet, meal planning, food safety, nutritional deficiencies, and healthy living practices.',
        'level': 'beginner',
        'age_group': 'all',
        'approach': 'andragogic',
        'duration': 15,
        'objectives': 'Master nutrition and healthy living practices'
    },
    {
        'title': 'Community Health and Hygiene',
        'category': 'life_skills',
        'description': 'Community health - sanitation, disease prevention, water safety, hygiene practices, and community health education.',
        'level': 'beginner',
        'age_group': 'all',
        'approach': 'andragogic',
        'duration': 15,
        'objectives': 'Master community health and hygiene practices'
    },
    {
        'title': 'Stress Management and Wellness',
        'category': 'life_skills',
        'description': 'Stress management - stress reduction techniques, mindfulness, work-life balance, and personal wellness strategies.',
        'level': 'beginner',
        'age_group': 'all',
        'approach': 'andragogic',
        'duration': 12,
        'objectives': 'Master stress management and wellness strategies'
    },
    {
        'title': 'Public Health and Epidemiology',
        'category': 'life_skills',
        'description': 'Public health - epidemiology, disease prevention, health promotion, and community health program management.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'heutagogic',
        'duration': 20,
        'objectives': 'Master public health and epidemiology concepts'
    },
    {
        'title': 'Women\'s Health and Maternal Care',
        'category': 'life_skills',
        'description': 'Women\'s health - maternal care, reproductive health, prenatal care, postnatal care, and women\'s health education.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'andragogic',
        'duration': 18,
        'objectives': 'Master women\'s health and maternal care'
    },
]

# Add health courses
total_added = 0

for course_data in health_courses:
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
print(f"📊 Total Health Courses Added: {total_added}")
print(f"📚 Total Courses in Database: {Course.objects.filter(is_active=True).count()}")
print("🎉 Health course addition complete!")