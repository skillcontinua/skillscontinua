import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from courses.models import Category, Course

print("📚 Adding CORE COMPULSORY courses to SkillsContinua...")

# Get categories
categories = {}
for cat in Category.objects.all():
    categories[cat.pillar] = cat

# Core compulsory courses organized by learning approach
core_courses = [
    # PEDAGOGIC (For Children - Structured, Fun, Interactive)
    {
        'title': 'Financial Literacy for Kids',
        'category': 'life_skills',
        'description': 'Learn about money, saving, and making smart choices - designed for young learners with fun activities.',
        'level': 'beginner',
        'age_group': 'child',
        'learning_approach': 'pedagogic',
        'duration': 15,
        'is_core': True
    },
    {
        'title': 'Communication Skills for Kids',
        'category': 'life_skills',
        'description': 'Learn to express yourself clearly, listen well, and make friends through fun activities.',
        'level': 'beginner',
        'age_group': 'child',
        'learning_approach': 'pedagogic',
        'duration': 12,
        'is_core': True
    },
    {
        'title': 'Logic and Reasoning for Kids',
        'category': 'life_skills',
        'description': 'Develop critical thinking skills through puzzles, games, and fun challenges.',
        'level': 'beginner',
        'age_group': 'child',
        'learning_approach': 'pedagogic',
        'duration': 14,
        'is_core': True
    },
    {
        'title': 'Cognitive Development - Memory and Focus',
        'category': 'life_skills',
        'description': 'Fun exercises to improve memory, concentration, and learning abilities.',
        'level': 'beginner',
        'age_group': 'child',
        'learning_approach': 'pedagogic',
        'duration': 12,
        'is_core': True
    },
    
    # ANDRAGOGIC (For Adults - Practical, Self-Directed)
    {
        'title': 'Financial Management for Adults',
        'category': 'life_skills',
        'description': 'Master personal finance - budgeting, saving, investing, and planning for financial freedom.',
        'level': 'intermediate',
        'age_group': 'adult',
        'learning_approach': 'andragogic',
        'duration': 25,
        'is_core': True
    },
    {
        'title': 'Advanced Communication Skills',
        'category': 'life_skills',
        'description': 'Master professional communication - public speaking, negotiation, conflict resolution, and persuasion.',
        'level': 'intermediate',
        'age_group': 'adult',
        'learning_approach': 'andragogic',
        'duration': 20,
        'is_core': True
    },
    {
        'title': 'Logic and Critical Thinking',
        'category': 'life_skills',
        'description': 'Develop logical reasoning, analyze arguments, and make better decisions in personal and professional life.',
        'level': 'intermediate',
        'age_group': 'adult',
        'learning_approach': 'andragogic',
        'duration': 22,
        'is_core': True
    },
    {
        'title': 'Cognitive Training for Adults',
        'category': 'life_skills',
        'description': 'Improve memory, problem-solving, and cognitive abilities through proven brain training exercises.',
        'level': 'intermediate',
        'age_group': 'adult',
        'learning_approach': 'andragogic',
        'duration': 18,
        'is_core': True
    },
    {
        'title': 'Qualitative and Quantitative Appraisal',
        'category': 'life_skills',
        'description': 'Learn to analyze data, make informed decisions, and evaluate information using both qualitative and quantitative methods.',
        'level': 'advanced',
        'age_group': 'adult',
        'learning_approach': 'andragogic',
        'duration': 25,
        'is_core': True
    },
    
    # HEUTAGOGIC (For Advanced Learners - Self-Determined)
    {
        'title': 'Advanced Financial Strategy',
        'category': 'life_skills',
        'description': 'Strategic financial planning, investment analysis, and wealth creation for advanced learners.',
        'level': 'advanced',
        'age_group': 'adult',
        'learning_approach': 'heutagogic',
        'duration': 30,
        'is_core': True
    },
    {
        'title': 'Strategic Communication and Leadership',
        'category': 'life_skills',
        'description': 'Master communication at the highest level - leadership communication, corporate influence, and strategic messaging.',
        'level': 'advanced',
        'age_group': 'adult',
        'learning_approach': 'heutagogic',
        'duration': 25,
        'is_core': True
    },
    {
        'title': 'Advanced Logic and Systems Thinking',
        'category': 'life_skills',
        'description': 'Develop systems thinking, complex problem-solving, and advanced logical frameworks for tackling complex challenges.',
        'level': 'advanced',
        'age_group': 'adult',
        'learning_approach': 'heutagogic',
        'duration': 30,
        'is_core': True
    },
    {
        'title': 'Cognitive Enhancement and Neuroplasticity',
        'category': 'life_skills',
        'description': 'Advanced techniques for enhancing cognitive performance, learning speed, and brain optimization.',
        'level': 'advanced',
        'age_group': 'adult',
        'learning_approach': 'heutagogic',
        'duration': 25,
        'is_core': True
    },
    {
        'title': 'Advanced Research and Appraisal Methods',
        'category': 'life_skills',
        'description': 'Master research methodologies, advanced data analysis, and comprehensive appraisal techniques.',
        'level': 'advanced',
        'age_group': 'adult',
        'learning_approach': 'heutagogic',
        'duration': 30,
        'is_core': True
    },
]

# Add core courses
count = 0
for course_data in core_courses:
    category = categories.get(course_data['category'])
    if category:
        course, created = Course.objects.get_or_create(
            title=course_data['title'],
            category=category,
            defaults={
                'description': course_data['description'],
                'level': course_data['level'],
                'age_group': course_data['age_group'],
                'learning_approach': course_data['learning_approach'],
                'duration_hours': course_data['duration'],
                'is_active': True,
                'featured': True,  # Mark core courses as featured
                'learning_objectives': 'Core compulsory course - essential for all learners',
                'target_audience': f"Learners following the {course_data['learning_approach']} approach",
            }
        )
        if created:
            count += 1
            print(f"✅ Added CORE course: {course.title} ({course_data['learning_approach'].upper()})")
        else:
            print(f"📚 Already exists: {course.title}")
    else:
        print(f"⚠️ Category '{course_data['category']}' not found")

print(f"\n" + "="*50)
print(f"📊 Core Courses Added: {count}")
print(f"📚 Total Courses: {Course.objects.filter(is_active=True).count()}")
print(f"📊 Core courses by approach:")

# Show summary by learning approach
for approach in ['pedagogic', 'andragogic', 'heutagogic']:
    count = Course.objects.filter(learning_approach=approach, is_active=True).count()
    print(f"  📖 {approach.upper()}: {count} courses")

print("🎉 Core course addition complete!")