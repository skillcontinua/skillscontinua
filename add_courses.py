import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from courses.models import Category, Course

print("📚 Adding courses to SkillsContinua...")

# Create categories
categories = [
    {'name': 'Foundational Literacy', 'pillar': 'literacy', 
     'description': 'From complete illiteracy to confident reading, writing and numeracy'},
    {'name': 'Computer Literacy', 'pillar': 'computer', 
     'description': 'Basic to advanced IT skills - hardware, software, cybersecurity, and AI'},
    {'name': 'Vocational Trades', 'pillar': 'vocational', 
     'description': 'Practical skills for self-employment - construction, repair, and artisan trades'},
    {'name': 'Certifications', 'pillar': 'certification', 
     'description': 'Professional certifications - CompTIA, Cisco, and international credentials'},
    {'name': 'Life Skills', 'pillar': 'life_skills', 
     'description': 'Essential life competencies - financial literacy, emotional intelligence'},
    {'name': 'Primary Education', 'pillar': 'primary', 
     'description': 'Complete primary curriculum - literacy, numeracy, science'},
    {'name': 'Secondary Education', 'pillar': 'secondary', 
     'description': 'Advanced secondary education - STEM, commerce, and technical tracks'},
]

category_objects = {}
for cat_data in categories:
    cat, created = Category.objects.get_or_create(
        pillar=cat_data['pillar'],
        defaults={
            'name': cat_data['name'],
            'description': cat_data['description']
        }
    )
    category_objects[cat.pillar] = cat
    print(f"{'✅' if created else '📚'} Category: {cat.name}")

# Add sample courses
courses_data = [
    {
        'title': 'Alphabet and Phonics',
        'category': category_objects['literacy'],
        'description': 'Learn the alphabet, letter sounds, and phonics rules to start reading',
        'level': 'beginner',
        'age_group': 'all',
        'learning_approach': 'pedagogic',
        'duration_hours': 10,
    },
    {
        'title': 'Basic Reading Skills',
        'category': category_objects['literacy'],
        'description': 'Learn to read words, sentences, and simple stories',
        'level': 'beginner',
        'age_group': 'all',
        'learning_approach': 'pedagogic',
        'duration_hours': 15,
    },
    {
        'title': 'Basic Writing Skills',
        'category': category_objects['literacy'],
        'description': 'Learn to write clearly and correctly',
        'level': 'beginner',
        'age_group': 'all',
        'learning_approach': 'pedagogic',
        'duration_hours': 12,
    },
    {
        'title': 'Computer Basics',
        'category': category_objects['computer'],
        'description': 'Introduction to computers, hardware, and basic software',
        'level': 'beginner',
        'age_group': 'all',
        'learning_approach': 'andragogic',
        'duration_hours': 15,
    },
    {
        'title': 'Introduction to Carpentry',
        'category': category_objects['vocational'],
        'description': 'Learn basic woodworking skills - measurement, cutting, joining',
        'level': 'beginner',
        'age_group': 'adult',
        'learning_approach': 'andragogic',
        'duration_hours': 20,
    },
    {
        'title': 'Financial Literacy Basics',
        'category': category_objects['life_skills'],
        'description': 'Learn to manage money, create budgets, and plan for the future',
        'level': 'beginner',
        'age_group': 'adult',
        'learning_approach': 'andragogic',
        'duration_hours': 12,
    },
]

count = 0
for course_data in courses_data:
    course, created = Course.objects.get_or_create(
        title=course_data['title'],
        category=course_data['category'],
        defaults={
            'description': course_data['description'],
            'level': course_data['level'],
            'age_group': course_data['age_group'],
            'learning_approach': course_data['learning_approach'],
            'duration_hours': course_data['duration_hours'],
            'is_active': True,
            'featured': True if count < 3 else False,
        }
    )
    if created:
        count += 1
        print(f"✅ Added: {course.title}")
    else:
        print(f"📚 Already exists: {course.title}")

print(f"\n📊 Total Courses Added: {count}")
print(f"📚 Total Courses in Database: {Course.objects.filter(is_active=True).count()}")
print("🎉 Course addition complete!")