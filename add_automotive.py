# Run with: python manage.py shell < add_automotive.py
from courses.models import Category, Course

print("Creating Automotive Repairs & Maintenance...")

# 1. Create Automotive Category
auto_cat, created = Category.objects.get_or_create(
    pillar="AUTOMOTIVE_REPAIRS",
    defaults={
        'name': 'Automotive Repairs & Maintenance',
        'description': 'Car repairs, diagnostics, electrical, engine, panel beating for Aba youth',
        'icon': '🚗',
        'order': 10,
        'name_en': 'Automotive Repairs & Maintenance',
        'description_en': 'Car repairs, diagnostics, electrical, engine, panel beating',
    }
)
if created:
    print(f"✅ Created category: {auto_cat.name}")
else:
    print(f"✅ Found category: {auto_cat.name} - updating...")
    auto_cat.name = 'Automotive Repairs & Maintenance'
    auto_cat.icon = '🚗'
    auto_cat.order = 10
    auto_cat.save()

# 2. Automotive Courses
auto_courses = [
    {'title': 'Basic Car Maintenance & Servicing', 'desc': 'Oil change, brake pads, daily checks', 'hours': 40, 'level': 'beginner'},
    {'title': 'Engine Diagnostics & OBD Scanner', 'desc': 'OBD2 scanner, fault codes Toyota Honda Kia', 'hours': 60, 'level': 'intermediate'},
    {'title': 'Auto Electrical & Wiring', 'desc': 'Battery, alternator, starter, lighting wiring', 'hours': 50, 'level': 'intermediate'},
    {'title': 'Panel Beating & Spray Painting', 'desc': 'Body work, dent removal, painting Aba', 'hours': 80, 'level': 'beginner'},
    {'title': 'Motorcycle & Keke Repair (Tricycle)', 'desc': 'Okada Keke engine clutch most profitable', 'hours': 45, 'level': 'beginner'},
    {'title': 'Wheel Alignment, Balancing & Vulcanizing', 'desc': 'Vulcanizer shop, alignment machine daily cash', 'hours': 30, 'level': 'beginner'},
    {'title': 'Auto AC Repair & Refrigeration', 'desc': 'Car air conditioning gas, compressor repair', 'hours': 50, 'level': 'advanced'},
]

# 3. Create courses with ALL required fields
for data in auto_courses:
    course, created = Course.objects.get_or_create(
        title=data['title'],
        category=auto_cat,
        defaults={
            'description': data['desc'],
            'duration_hours': data['hours'],
            'level': data['level'],
            'age_group': 'all',
            'learning_approach': 'heutagogic',
            'is_active': True,
            'featured': True,
            'target_audience': 'Youth in Aba, Abia State',
            'prerequisites': 'No prior experience',
            'learning_objectives': f"Learn {data['title']} for self-employment",
        }
    )
    if created:
        print(f"  + Created: {course.title}")
    else:
        print(f"  = Exists: {course.title} - Activating...")
        course.is_active = True
        course.featured = True
        course.save()

print(f"\n✅ Done!")
print(f"Automotive: {Course.objects.filter(category=auto_cat).count()}")
print(f"Total Courses: {Course.objects.count()}")
print(f"Categories: {Category.objects.count()}")
for cat in Category.objects.order_by('order'):
    print(f" - {cat.order}. {cat.name} ({cat.pillar}): {cat.courses.count()} courses")