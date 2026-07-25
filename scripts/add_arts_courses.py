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
print("🎨 ADDING ARTS COURSES")
print("="*70)

# First, create Arts category if it doesn't exist
arts_category, created = Category.objects.get_or_create(
    pillar='arts',
    defaults={
        'name': 'Arts and Creative Crafts',
        'description': 'Complete arts and crafts - sculpture, carving, painting, drawing, pottery, weaving, and creative expression.'
    }
)

if created:
    print(f"✅ Created category: {arts_category.name}")
else:
    print(f"📚 Category already exists: {arts_category.name}")

# Reload categories dictionary after creating new category
categories = {}
for cat in Category.objects.all():
    categories[cat.pillar] = cat

# Now use the category
category = categories.get('arts')

if category:
    print(f"✅ Using category: {category.name}")

arts_courses = [
    {
        'title': 'Sculpture - Complete Guide',
        'category': 'arts',
        'description': 'Complete sculpture - materials, techniques, tools, and creating professional sculptures. From clay to bronze and modern materials.',
        'level': 'intermediate',
        'age_group': 'all',
        'approach': 'andragogic',
        'duration': 25,
        'objectives': 'Master sculpture techniques and create professional works'
    },
    {
        'title': 'Wood Carving - Techniques and Tools',
        'category': 'arts',
        'description': 'Wood carving - tools, techniques, wood selection, and creating beautiful carved pieces. From basic to advanced carving.',
        'level': 'intermediate',
        'age_group': 'all',
        'approach': 'andragogic',
        'duration': 20,
        'objectives': 'Master wood carving techniques and create artistic pieces'
    },
    {
        'title': 'Stone Carving and Sculpture',
        'category': 'arts',
        'description': 'Stone carving - stone selection, tools, techniques, and creating durable stone sculptures and architectural elements.',
        'level': 'advanced',
        'age_group': 'adult',
        'approach': 'andragogic',
        'duration': 30,
        'objectives': 'Master stone carving and create professional sculptures'
    },
    {
        'title': 'Painting - Complete Guide',
        'category': 'arts',
        'description': 'Complete painting - oils, acrylics, watercolors, techniques, color theory, and creating professional paintings.',
        'level': 'beginner',
        'age_group': 'all',
        'approach': 'pedagogic',
        'duration': 25,
        'objectives': 'Master painting techniques and create professional artwork'
    },
    {
        'title': 'Drawing and Sketching Fundamentals',
        'category': 'arts',
        'description': 'Drawing and sketching - techniques, materials, perspective, anatomy, and creating professional drawings.',
        'level': 'beginner',
        'age_group': 'all',
        'approach': 'pedagogic',
        'duration': 20,
        'objectives': 'Master drawing and sketching techniques'
    },
    {
        'title': 'Advanced Drawing and Illustration',
        'category': 'arts',
        'description': 'Advanced drawing - figure drawing, portraiture, illustration techniques, and professional illustration work.',
        'level': 'advanced',
        'age_group': 'adult',
        'approach': 'heutagogic',
        'duration': 25,
        'objectives': 'Master advanced drawing and illustration techniques'
    },
    {
        'title': 'Pottery and Ceramics - Complete Guide',
        'category': 'arts',
        'description': 'Pottery and ceramics - clay preparation, wheel throwing, hand building, glazing, firing, and creating professional pottery.',
        'level': 'intermediate',
        'age_group': 'all',
        'approach': 'andragogic',
        'duration': 25,
        'objectives': 'Master pottery and ceramics techniques'
    },
    {
        'title': 'Basket Weaving and Fiber Arts',
        'category': 'arts',
        'description': 'Basket weaving and fiber arts - materials, weaving techniques, patterns, and creating functional and decorative baskets.',
        'level': 'beginner',
        'age_group': 'all',
        'approach': 'andragogic',
        'duration': 15,
        'objectives': 'Master basket weaving and fiber arts'
    },
    {
        'title': 'Advanced Weaving and Textile Arts',
        'category': 'arts',
        'description': 'Advanced weaving - loom techniques, pattern design, textile creation, and professional weaving practices.',
        'level': 'advanced',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 20,
        'objectives': 'Master advanced weaving and textile arts'
    },
    {
        'title': 'Mixed Media and Contemporary Art',
        'category': 'arts',
        'description': 'Mixed media and contemporary art - combining materials, techniques, and creating innovative contemporary artwork.',
        'level': 'advanced',
        'age_group': 'adult',
        'approach': 'heutagogic',
        'duration': 20,
        'objectives': 'Master mixed media and contemporary art techniques'
    },
]

# Add courses
total_added = 0

for course_data in arts_courses:
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
print(f"📊 Total Arts Courses Added: {total_added}")
print(f"📚 Total Courses in Database: {Course.objects.filter(is_active=True).count()}")
print("🎉 Arts course addition complete!")