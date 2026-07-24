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
print("🤖 ADDING BLOCKCHAIN, AI & CLOUD COMPUTING COURSES")
print("="*70)

# Get categories
categories = {}
for cat in Category.objects.all():
    categories[cat.pillar] = cat

tech_courses = [
    # === BLOCKCHAIN ===
    {
        'title': 'Blockchain Technology - Complete Guide',
        'category': 'digital',
        'description': 'Complete blockchain technology - history, evolution, types, uses, advantages, and emerging applications in various industries.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 25,
        'objectives': 'Master blockchain technology and its applications'
    },
    {
        'title': 'Cryptocurrency and Digital Finance',
        'category': 'digital',
        'description': 'Cryptocurrency - Bitcoin, Ethereum, and other digital currencies. Trading, investing, and digital finance management.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 25,
        'objectives': 'Master cryptocurrency and digital finance'
    },
    {
        'title': 'Smart Contracts and Decentralized Applications',
        'category': 'digital',
        'description': 'Smart contracts - creation, deployment, and management. DApps and decentralized finance (DeFi) applications.',
        'level': 'advanced',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 30,
        'objectives': 'Master smart contracts and DApp development'
    },
    
    # === ARTIFICIAL INTELLIGENCE ===
    {
        'title': 'Artificial Intelligence Fundamentals',
        'category': 'digital',
        'description': 'AI fundamentals - history, evolution, types, and applications. Understanding AI and its impact on society and business.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 25,
        'objectives': 'Master AI fundamentals and applications'
    },
    {
        'title': 'Machine Learning - Complete Guide',
        'category': 'digital',
        'description': 'Machine learning - supervised, unsupervised, and reinforcement learning. Algorithms, models, and practical applications.',
        'level': 'advanced',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 30,
        'objectives': 'Master machine learning algorithms and applications'
    },
    {
        'title': 'ChatGPT and Generative AI',
        'category': 'digital',
        'description': 'ChatGPT and generative AI - prompt engineering, content creation, automation, and practical uses in business and education.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 20,
        'objectives': 'Master ChatGPT and generative AI applications'
    },
    
    # === CLOUD COMPUTING ===
    {
        'title': 'Cloud Computing - Complete Guide',
        'category': 'digital',
        'description': 'Cloud computing - history, evolution, types (IaaS, PaaS, SaaS), and major cloud providers. Understanding cloud architecture.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 25,
        'objectives': 'Master cloud computing fundamentals and applications'
    },
    {
        'title': 'Amazon Web Services (AWS) Fundamentals',
        'category': 'digital',
        'description': 'AWS cloud services - EC2, S3, RDS, and other AWS services. Cloud deployment and management on AWS.',
        'level': 'advanced',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 30,
        'objectives': 'Master AWS cloud services and deployment'
    },
    {
        'title': 'Google Cloud Platform (GCP) Fundamentals',
        'category': 'digital',
        'description': 'Google Cloud Platform - computing, storage, databases, and machine learning services on GCP.',
        'level': 'advanced',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 25,
        'objectives': 'Master Google Cloud Platform services'
    },
    {
        'title': 'Microsoft Azure Fundamentals',
        'category': 'digital',
        'description': 'Microsoft Azure - cloud services, virtual machines, storage, and Azure solutions for business.',
        'level': 'advanced',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 25,
        'objectives': 'Master Microsoft Azure cloud services'
    },
]

# Add courses
total_added = 0

for course_data in tech_courses:
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
print(f"📊 Total Technology Courses Added: {total_added}")
print(f"📚 Total Courses in Database: {Course.objects.filter(is_active=True).count()}")
print("🎉 Technology course addition complete!")