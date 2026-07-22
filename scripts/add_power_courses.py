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
print("⚡ ADDING POWER & RENEWABLE ENERGY COURSES")
print("="*70)

# Get categories
categories = {}
for cat in Category.objects.all():
    categories[cat.pillar] = cat
    categories[cat.name.lower()] = cat

print("Available categories found:", list(categories.keys())[:10])

# Solar Energy Courses
solar_courses = [
    {
        'title': 'Solar Panel Technology - Complete Guide',
        'category': 'electrical',
        'description': 'Complete solar panel technology - evolution, types (monocrystalline, polycrystalline, thin-film), uses, advantages, disadvantages, and modern improvements.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 25,
        'objectives': 'Master solar panel technology, selection, and application'
    },
    {
        'title': 'Solar Panel Installation and Maintenance',
        'category': 'electrical',
        'description': 'Professional solar panel installation - system design, mounting, wiring, safety, maintenance, and troubleshooting for residential and commercial systems.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'andragogic',
        'duration': 30,
        'objectives': 'Master professional solar panel installation and maintenance'
    },
    {
        'title': 'Modern Solar Technology - Advancements',
        'category': 'electrical',
        'description': 'Modern solar technology - bifacial panels, PERC cells, solar tracking systems, floating solar, building-integrated photovoltaics, and emerging technologies.',
        'level': 'advanced',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 20,
        'objectives': 'Master modern solar technology and emerging innovations'
    },
]

# Inverter Technology Courses
inverter_courses = [
    {
        'title': 'Inverter Technology - Complete Guide',
        'category': 'electrical',
        'description': 'Complete inverter technology - evolution, types (string, central, micro, hybrid), uses, advantages, disadvantages, and modern improvements.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 25,
        'objectives': 'Master inverter technology, selection, and application'
    },
    {
        'title': 'Inverter Installation, Repair and Maintenance',
        'category': 'electrical',
        'description': 'Professional inverter installation, repair, and maintenance - system design, wiring, troubleshooting, component replacement, and safety protocols.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'andragogic',
        'duration': 30,
        'objectives': 'Master inverter installation, repair, and maintenance'
    },
    {
        'title': 'Modern Inverter Technology - Advancements',
        'category': 'electrical',
        'description': 'Modern inverter technology - smart inverters, grid-tie systems, hybrid inverters, battery-ready inverters, and IoT-enabled power management.',
        'level': 'advanced',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 20,
        'objectives': 'Master modern inverter technology and smart power management'
    },
]

# Inverter Battery Courses
battery_courses = [
    {
        'title': 'Inverter Battery Technology - Complete Guide',
        'category': 'electrical',
        'description': 'Complete inverter battery technology - evolution, types (lead-acid, lithium, gel, AGM), uses, advantages, disadvantages, and selection criteria.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 25,
        'objectives': 'Master inverter battery technology, selection, and application'
    },
    {
        'title': 'Battery Maintenance and Replacement',
        'category': 'electrical',
        'description': 'Professional battery maintenance, testing, replacement, and recycling - battery health assessment, charging protocols, and safety procedures.',
        'level': 'intermediate',
        'age_group': 'adult',
        'approach': 'andragogic',
        'duration': 20,
        'objectives': 'Master battery maintenance, testing, and replacement'
    },
    {
        'title': 'Lithium Battery Technology - Modern Solutions',
        'category': 'electrical',
        'description': 'Lithium battery technology - LiFePO4, NMC, LCO, LTO - advantages, disadvantages, applications, BMS (Battery Management Systems), and safety protocols.',
        'level': 'advanced',
        'age_group': 'adult',
        'approach': 'cybergogic',
        'duration': 25,
        'objectives': 'Master lithium battery technology and modern energy storage'
    },
]

# Add all courses
all_courses = solar_courses + inverter_courses + battery_courses
total_added = 0

for course_data in all_courses:
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
print(f"📊 Total Power & Energy Courses Added: {total_added}")
print(f"📚 Total Courses in Database: {Course.objects.filter(is_active=True).count()}")
print("🎉 Power & Energy course addition complete!")