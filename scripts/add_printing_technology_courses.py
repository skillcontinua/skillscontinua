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
print("🖨️ ADDING PRINTING TECHNOLOGY COURSES")
print("="*70)

# Get categories
categories = {}
for cat in Category.objects.all():
    categories[cat.pillar] = cat

printing_courses = [
    {
        'title': 'Printing Technology - Complete Guide',
        'category': 'vocational',
        'description': 'Complete printing technology - evolution from ancient to modern, types, methods, applications, and industry trends. Comprehensive overview of the printing industry.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 25,
        'objectives': 'Master printing technology and industry practices'
    },
    {
        'title': 'Offset Printing - Traditional and Modern',
        'category': 'vocational',
        'description': 'Offset printing - history, principles, equipment, plate making, press operations, and modern digital offset technology.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'andragogic',
        'duration': 25,
        'objectives': 'Master offset printing processes and operations'
    },
    {
        'title': 'Digital Printing Technology',
        'category': 'vocational',
        'description': 'Digital printing - laser printing, inkjet printing, 3D printing, digital workflow, and applications in modern printing.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 25,
        'objectives': 'Master digital printing technology and applications'
    },
    {
        'title': 'Screen Printing - Techniques and Applications',
        'category': 'vocational',
        'description': 'Screen printing - history, methods, equipment, materials, and applications in textiles, signage, and commercial printing.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'andragogic',
        'duration': 20,
        'objectives': 'Master screen printing techniques and applications'
    },
    {
        'title': '3D Printing Technology - Complete Guide',
        'category': 'vocational',
        'description': '3D printing - evolution, types (FDM, SLA, SLS, DLP), materials, applications, and emerging trends in additive manufacturing.',
        'level': 'advanced',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 30,
        'objectives': 'Master 3D printing technology and applications'
    },
    {
        'title': 'Printing Materials and Inks',
        'category': 'vocational',
        'description': 'Printing materials - papers, boards, inks, toners, special coatings, and sustainable materials in modern printing.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'andragogic',
        'duration': 20,
        'objectives': 'Master printing materials selection and application'
    },
    {
        'title': 'Print Finishing and Binding',
        'category': 'vocational',
        'description': 'Print finishing - cutting, folding, binding, lamination, and post-press processes for professional print production.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'andragogic',
        'duration': 20,
        'objectives': 'Master print finishing and binding techniques'
    },
    {
        'title': 'Color Management in Printing',
        'category': 'vocational',
        'description': 'Color management - color theory, calibration, ICC profiles, and achieving accurate color reproduction in printing.',
        'level': 'advanced',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 20,
        'objectives': 'Master color management for professional printing'
    },
    {
        'title': 'Prepress and Print Production Workflow',
        'category': 'vocational',
        'description': 'Prepress and production workflow - file preparation, proofing, plate making, and quality control in print production.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 25,
        'objectives': 'Master prepress and production workflow'
    },
    {
        'title': 'Printing Business Management and Marketing',
        'category': 'vocational',
        'description': 'Printing business management - operations, pricing, customer service, marketing, and building a successful printing enterprise.',
        'level': 'advanced',
        'age_group': 'adult',
        'approach': 'heutagogic',
        'duration': 20,
        'objectives': 'Master printing business management and marketing'
    },
]

# Add printing courses
total_added = 0

for course_data in printing_courses:
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
print(f"📊 Total Printing Technology Courses Added: {total_added}")
print(f"📚 Total Courses in Database: {Course.objects.filter(is_active=True).count()}")
print("🎉 Printing technology course addition complete!")