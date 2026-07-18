import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skillscontinua_core.settings')
django.setup()

from courses.models import Category, Course
from accounts.models import User

admin = User.objects.filter(is_superuser=True).first()

# Get or create Vocational category
def get_category(name, pillar, language='English'):
    cat, _ = Category.objects.get_or_create(
        name=name,
        defaults={'pillar': pillar, 'language': language}
    )
    return cat

# ============================================================
# NEW VOCATIONAL COURSES
# ============================================================
vocational_cat = Category.objects.filter(pillar='vocational').first()
if not vocational_cat:
    vocational_cat = Category.objects.create(name='Vocational Trades', pillar='vocational', language='English')

new_courses = [
    {
        'title': 'Motorcycle and Tricycle Repairs',
        'description': 'Master the maintenance and repair of motorcycles (okada) and tricycles (keke/achaba) — the most common commercial vehicles in West Africa. Covers engines, electrical systems, brakes, tyres and running a profitable repair workshop.',
        'level': 'beginner',
        'duration_hours': 40,
        'is_compulsory': False,
    },
    {
        'title': 'Car Repairs and Maintenance',
        'description': 'Professional car maintenance and repair skills covering modern petrol and diesel vehicles. Engine systems, gearbox, brakes, suspension, electrical diagnostics and customer service for a thriving vehicle repair business.',
        'level': 'intermediate',
        'duration_hours': 60,
        'is_compulsory': False,
    },
    {
        'title': 'Truck and Commercial Vehicle Maintenance',
        'description': 'Specialised maintenance and repair of trucks, lorries and commercial vehicles. Diesel engines, air brakes, heavy axles, fleet maintenance planning and working with transport companies.',
        'level': 'intermediate',
        'duration_hours': 50,
        'is_compulsory': False,
    },
    {
        'title': 'Heavy Plant and Equipment Operation',
        'description': 'Operation and basic maintenance of heavy construction equipment — excavators, bulldozers, graders, loaders and compactors. Safety, pre-operational checks, site procedures and career pathways in construction.',
        'level': 'intermediate',
        'duration_hours': 60,
        'is_compulsory': False,
    },
    {
        'title': 'Tailoring and Fashion Design',
        'description': 'Professional garment making from taking measurements to cutting, sewing and finishing. Covers traditional African styles, modern fashion, pattern drafting and running a profitable tailoring business.',
        'level': 'beginner',
        'duration_hours': 50,
        'is_compulsory': False,
    },
    {
        'title': 'Catering and Food Processing',
        'description': 'Professional food preparation, catering operations, food safety and hygiene, event catering, and small-scale food processing and preservation for commercial sale.',
        'level': 'beginner',
        'duration_hours': 40,
        'is_compulsory': False,
    },
    {
        'title': 'Phone and Electronics Repairs',
        'description': 'Diagnosing and repairing smartphones, tablets and electronic devices. Screen replacement, battery replacement, water damage recovery, software issues and running a profitable phone repair business.',
        'level': 'beginner',
        'duration_hours': 40,
        'is_compulsory': False,
    },
    {
        'title': 'Solar Energy Installation',
        'description': 'Designing and installing solar power systems for homes and small businesses. Solar panels, charge controllers, inverters, batteries, wiring and sizing systems for West African energy needs.',
        'level': 'intermediate',
        'duration_hours': 45,
        'is_compulsory': False,
    },
    {
        'title': 'Photography and Videography',
        'description': 'Professional photography and video production for events, portraits, commercial work and social media content. Camera skills, lighting, editing, and building a profitable creative business.',
        'level': 'beginner',
        'duration_hours': 35,
        'is_compulsory': False,
    },
    {
        'title': 'Hair and Beauty',
        'description': 'Professional hair styling, braiding, relaxing, colouring and beauty treatments. Covers both men\'s and women\'s services, salon management, health and safety, and business development.',
        'level': 'beginner',
        'duration_hours': 40,
        'is_compulsory': False,
    },
    {
        'title': 'Livestock Farming and Animal Husbandry',
        'description': 'Profitable small-scale livestock production covering poultry, goats, pigs and cattle. Feeding, health management, disease prevention, record keeping and marketing your produce.',
        'level': 'beginner',
        'duration_hours': 35,
        'is_compulsory': False,
    },
    {
        'title': 'Crop Farming and Agribusiness',
        'description': 'Modern farming techniques for profitable crop production. Soil preparation, planting, irrigation, pest management, post-harvest handling and selling to markets and processors.',
        'level': 'beginner',
        'duration_hours': 40,
        'is_compulsory': False,
    },
    {
        'title': 'Refrigeration and Air Conditioning',
        'description': 'Installation, maintenance and repair of domestic and commercial refrigeration and air conditioning systems. Gas handling, electrical principles, fault diagnosis and building a service business.',
        'level': 'intermediate',
        'duration_hours': 50,
        'is_compulsory': False,
    },
    {
        'title': 'Security Services and Guard Training',
        'description': 'Professional security guarding principles, access control, emergency response, report writing, customer service and career pathways in the growing private security industry.',
        'level': 'beginner',
        'duration_hours': 30,
        'is_compulsory': False,
    },
    {
        'title': 'Event Planning and Management',
        'description': 'Professional event planning from brief to delivery. Venue selection, budgeting, vendor management, marketing, logistics and managing events from small gatherings to large celebrations.',
        'level': 'beginner',
        'duration_hours': 35,
        'is_compulsory': False,
    },
]

created_count = 0
for course_data in new_courses:
    course, created = Course.objects.get_or_create(
        title=course_data['title'],
        defaults={
            'category': vocational_cat,
            'description': course_data['description'],
            'level': course_data['level'],
            'age_group': 'adult',
            'language': 'English',
            'duration_hours': course_data['duration_hours'],
            'is_compulsory': course_data['is_compulsory'],
            'is_active': True,
            'created_by': admin,
        }
    )
    if created:
        created_count += 1
        print(f'CREATED: {course.title}')
    else:
        print(f'EXISTS:  {course.title}')

print(f'\nNew courses created: {created_count}')
print(f'Total courses now: {Course.objects.count()}')

# Show all vocational courses
print('\nAll vocational courses:')
for c in Course.objects.filter(category__pillar='vocational').order_by('title'):
    print(f'  {c.title} — {c.lessons.count()} lessons')