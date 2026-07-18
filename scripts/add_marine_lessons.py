import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from courses.models import Course, Lesson

print("🚤 Adding MARINE LESSON CONTENT...")
print("="*60)

# Marine lesson content
marine_lessons = {
    'Boat Engine Repair and Maintenance': [
        {'title': 'Introduction to Marine Engines', 
         'content': 'Learn about different types of marine engines - inboard, outboard, and stern drive. Understand the basic components and how they work together.\n\n📚 **Resources:**\n• Marine Engine Basics\n\n📝 **Exercise:** Identify the type of engine on a local boat.',
         'order': 1, 'duration': 30, 'free': True},
        {'title': 'Fuel Systems and Carburetion', 
         'content': 'Master marine fuel systems including carburetors, fuel injection, fuel pumps, and troubleshooting fuel issues.\n\n📚 **Resources:**\n• Marine Fuel System Guide\n\n📝 **Exercise:** Diagnose a fuel system problem.',
         'order': 2, 'duration': 35, 'free': False},
        {'title': 'Ignition and Electrical Systems', 
         'content': 'Learn about marine ignition systems, spark plugs, distributors, and basic electrical troubleshooting.\n\n📚 **Resources:**\n• Marine Electrical Systems\n\n📝 **Exercise:** Test and replace a spark plug.',
         'order': 3, 'duration': 35, 'free': False},
        {'title': 'Cooling and Exhaust Systems', 
         'content': 'Understand marine cooling systems, water pumps, thermostats, and exhaust systems.\n\n📚 **Resources:**\n• Marine Cooling Systems Guide\n\n📝 **Exercise:** Check and replace a water pump impeller.',
         'order': 4, 'duration': 35, 'free': False},
        {'title': 'Drive and Propeller Systems', 
         'content': 'Learn about sterndrive, propellers, trim tabs, and drive system maintenance and repair.\n\n📚 **Resources:**\n• Propeller Selection Guide\n\n📝 **Exercise:** Inspect and repair a propeller.',
         'order': 5, 'duration': 35, 'free': False},
        {'title': 'Engine Diagnostics and Troubleshooting', 
         'content': 'Master marine engine diagnostics using systematic troubleshooting techniques and modern diagnostic tools.\n\n📚 **Resources:**\n• Marine Diagnostic Guide\n\n📝 **Exercise:** Diagnose and fix a common engine problem.',
         'order': 6, 'duration': 40, 'free': False},
    ],
    'Outboard Motor Repair Fundamentals': [
        {'title': 'Two-Stroke and Four-Stroke Outboards', 
         'content': 'Understand the differences between 2-stroke and 4-stroke outboard motors. Learn basic operation and common issues.\n\n📚 **Resources:**\n• Outboard Engine Guide\n\n📝 **Exercise:** Identify the type of outboard motor.',
         'order': 1, 'duration': 30, 'free': True},
        {'title': 'Carburetor Repair and Adjustment', 
         'content': 'Learn to clean, rebuild, and adjust marine carburetors for optimal performance.\n\n📚 **Resources:**\n• Carburetor Repair Guide\n\n📝 **Exercise:** Rebuild a marine carburetor.',
         'order': 2, 'duration': 40, 'free': False},
        {'title': 'Lower Unit and Gearcase Repair', 
         'content': 'Master lower unit repair including gearcase service, water pump replacement, and seal maintenance.\n\n📚 **Resources:**\n• Lower Unit Repair Guide\n\n📝 **Exercise:** Service a lower unit gearcase.',
         'order': 3, 'duration': 40, 'free': False},
        {'title': 'Outboard Electrical Systems', 
         'content': 'Learn about outboard electrical systems including charging, ignition, and controls.\n\n📚 **Resources:**\n• Marine Electrical Guide\n\n📝 **Exercise:** Troubleshoot an electrical problem.',
         'order': 4, 'duration': 35, 'free': False},
        {'title': 'Seasonal Maintenance', 
         'content': 'Learn proper seasonal maintenance including winterization, storage, and preparation.\n\n📚 **Resources:**\n• Marine Maintenance Guide\n\n📝 **Exercise:** Prepare a boat for winter storage.',
         'order': 5, 'duration': 30, 'free': False},
    ],
    'Boat Building and Repair': [
        {'title': 'Boat Construction Methods', 
         'content': 'Learn different boat construction methods including fiberglass, wood, aluminum, and composite materials.\n\n📚 **Resources:**\n• Boat Building Guide\n\n📝 **Exercise:** Identify construction methods on local boats.',
         'order': 1, 'duration': 35, 'free': True},
        {'title': 'Fiberglass Repair Techniques', 
         'content': 'Master fiberglass repair including crack repair, gelcoat matching, and structural repairs.\n\n📚 **Resources:**\n• Fiberglass Repair Guide\n\n📝 **Exercise:** Repair a fiberglass crack.',
         'order': 2, 'duration': 45, 'free': False},
        {'title': 'Wooden Boat Repair', 
         'content': 'Learn traditional wooden boat repair including planking, caulking, and finishing.\n\n📚 **Resources:**\n• Wooden Boat Guide\n\n📝 **Exercise:** Repair a wooden boat plank.',
         'order': 3, 'duration': 45, 'free': False},
        {'title': 'Marine Painting and Finishing', 
         'content': 'Master marine painting techniques including surface preparation, bottom paint, and topcoat application.\n\n📚 **Resources:**\n• Marine Painting Guide\n\n📝 **Exercise:** Paint a small boat.',
         'order': 4, 'duration': 35, 'free': False},
        {'title': 'Boat Maintenance and Care', 
         'content': 'Learn proper boat maintenance including cleaning, waxing, and preventative care.\n\n📚 **Resources:**\n• Boat Maintenance Checklist\n\n📝 **Exercise:** Create a maintenance schedule.',
         'order': 5, 'duration': 30, 'free': False},
    ],
}

# Add lessons
total_added = 0
course_count = 0

for course_title, lessons in marine_lessons.items():
    try:
        course = Course.objects.get(title=course_title)
        print(f"\n📖 Adding lessons to: {course_title}")
        for lesson_data in lessons:
            lesson, created = Lesson.objects.get_or_create(
                course=course,
                title=lesson_data['title'],
                defaults={
                    'content': lesson_data['content'],
                    'order': lesson_data['order'],
                    'duration_minutes': lesson_data['duration'],
                    'is_free_preview': lesson_data.get('free', False),
                }
            )
            if created:
                total_added += 1
                print(f"  ✅ Added: {lesson.title}")
        course_count += 1
    except Course.DoesNotExist:
        print(f"⚠️ Course '{course_title}' not found")

print("\n" + "="*60)
print(f"📊 Courses Updated: {course_count}")
print(f"📊 Total Lessons Added: {total_added}")
print(f"📚 Total Lessons in Database: {Lesson.objects.count()}")
print("🎉 Marine lesson addition complete!")