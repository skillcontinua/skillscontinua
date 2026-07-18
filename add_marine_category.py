import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from courses.models import Category, Course

print("🚤 Creating AUTOMOTIVE MARINE category...")
print("="*60)

# Create the Automotive Marine category
marine_category, created = Category.objects.get_or_create(
    pillar='auto_marine',
    defaults={
        'name': 'Automotive Marine',
        'description': 'Marine engines, boat repairs, outboard motors, and watercraft maintenance and repair.',
        'order': 50,
    }
)

if created:
    print(f"✅ Created category: {marine_category.name}")
else:
    print(f"📚 Category already exists: {marine_category.name}")

# Find all marine-related courses and assign to this category
marine_course_titles = [
    'Boat Engine Repair and Maintenance',
    'Outboard Motor Repair Fundamentals',
    'Marine Engine Diagnostics',
    'Boat Building and Repair',
    'Marine Electrical Systems',
    'Canoe and Kayak Maintenance',
    'Navigation and Marine Safety',
]

updated_count = 0
for title in marine_course_titles:
    try:
        course = Course.objects.get(title=title)
        course.category = marine_category
        course.save()
        updated_count += 1
        print(f"✅ Moved: {course.title} -> {marine_category.name}")
    except Course.DoesNotExist:
        print(f"⚠️ Course not found: {title}")

print("\n" + "="*60)
print(f"📊 Marine Courses Updated: {updated_count}")
print(f"📚 Total Categories: {Category.objects.count()}")
print("🎉 Automotive Marine category created!")