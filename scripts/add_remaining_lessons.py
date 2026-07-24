import os
import sys
import django

# Add project root to path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from courses.models import Course, Lesson

print("="*70)
print("📚 ADDING REMAINING LESSONS TO ALL COURSES")
print("="*70)

# Get all courses that need lessons
courses_to_update = []
for course in Course.objects.filter(is_active=True):
    if course.lessons.count() == 0:
        courses_to_update.append(course)

print(f"📚 Found {len(courses_to_update)} courses with no lessons")

if len(courses_to_update) == 0:
    print("🎉 All courses have lessons!")
    exit()

# Generic lesson templates for different course types
def get_lessons_for_course(course):
    """Generate appropriate lessons based on course title and category"""
    
    # Check if it's an Agriculture course
    if 'agriculture' in course.category.pillar.lower() or 'animal' in course.category.pillar.lower():
        return [
            {'title': f'Introduction to {course.title}', 'content': f'Welcome to {course.title}. This comprehensive course covers all aspects of this important agricultural field.', 'order': 1, 'duration': 30},
            {'title': 'Understanding the Basics', 'content': 'Learn the fundamental concepts and principles. This is the foundation for everything else in this course.', 'order': 2, 'duration': 35},
            {'title': 'Practical Applications', 'content': 'Apply what you have learned to real-world situations. Practical examples and hands-on exercises.', 'order': 3, 'duration': 35},
            {'title': 'Advanced Techniques', 'content': 'Explore advanced techniques and professional practices in this field.', 'order': 4, 'duration': 30},
            {'title': 'Business Management', 'content': 'Learn to manage and grow a successful business in this field.', 'order': 5, 'duration': 30},
            {'title': 'Case Studies', 'content': 'Study real-world case studies and learn from successful practitioners.', 'order': 6, 'duration': 25},
            {'title': 'Troubleshooting and Problem Solving', 'content': 'Identify common challenges and learn proven solutions.', 'order': 7, 'duration': 25},
            {'title': 'Quality Control', 'content': 'Learn quality control standards and best practices.', 'order': 8, 'duration': 25},
            {'title': 'Marketing and Sales', 'content': 'Market your products and services effectively.', 'order': 9, 'duration': 30},
            {'title': 'Future Trends and Growth', 'content': 'Explore emerging trends and opportunities for growth.', 'order': 10, 'duration': 25},
        ]
    
    # Check if it's a Leather or Craft course
    elif 'leather' in course.category.pillar.lower() or 'craft' in course.title.lower():
        return [
            {'title': f'Introduction to {course.title}', 'content': f'Welcome to {course.title}. This comprehensive course covers all aspects of this craft.', 'order': 1, 'duration': 30},
            {'title': 'Materials and Tools', 'content': 'Learn about the materials, tools, and equipment used in this craft.', 'order': 2, 'duration': 35},
            {'title': 'Basic Techniques', 'content': 'Master the basic techniques and foundational skills.', 'order': 3, 'duration': 35},
            {'title': 'Advanced Techniques', 'content': 'Explore advanced techniques and professional practices.', 'order': 4, 'duration': 30},
            {'title': 'Design and Creativity', 'content': 'Develop your design skills and creative abilities.', 'order': 5, 'duration': 30},
            {'title': 'Quality Control', 'content': 'Learn quality control standards and best practices.', 'order': 6, 'duration': 25},
            {'title': 'Business Management', 'content': 'Learn to manage and grow a successful business.', 'order': 7, 'duration': 30},
            {'title': 'Marketing and Sales', 'content': 'Market your products and services effectively.', 'order': 8, 'duration': 25},
            {'title': 'Case Studies', 'content': 'Study real-world case studies and learn from successful practitioners.', 'order': 9, 'duration': 25},
            {'title': 'Future Trends and Growth', 'content': 'Explore emerging trends and opportunities for growth.', 'order': 10, 'duration': 25},
        ]
    
    # Default lessons
    else:
        return [
            {'title': f'Introduction to {course.title}', 'content': f'Welcome to {course.title}. This comprehensive course covers everything you need to know about this field.', 'order': 1, 'duration': 30},
            {'title': 'Core Concepts', 'content': 'Learn the fundamental concepts and principles. This is the building block for everything else.', 'order': 2, 'duration': 35},
            {'title': 'Practical Skills', 'content': 'Develop practical skills through hands-on exercises and real-world applications.', 'order': 3, 'duration': 35},
            {'title': 'Advanced Topics', 'content': 'Explore advanced topics and professional practices.', 'order': 4, 'duration': 30},
            {'title': 'Industry Standards', 'content': 'Learn about industry standards, best practices, and quality control.', 'order': 5, 'duration': 30},
            {'title': 'Business Development', 'content': 'Learn to build and grow a successful business in this field.', 'order': 6, 'duration': 30},
            {'title': 'Marketing and Sales', 'content': 'Market your products and services effectively.', 'order': 7, 'duration': 25},
            {'title': 'Case Studies', 'content': 'Study real-world case studies and learn from successful practitioners.', 'order': 8, 'duration': 25},
            {'title': 'Troubleshooting', 'content': 'Identify common challenges and learn proven solutions.', 'order': 9, 'duration': 25},
            {'title': 'Future Trends', 'content': 'Explore emerging trends and opportunities for growth.', 'order': 10, 'duration': 25},
        ]

# Add lessons
total_added = 0
total_courses = 0

for course in courses_to_update:
    print(f"\n📖 Adding lessons to: {course.title} (Category: {course.category.name})")
    
    lessons = get_lessons_for_course(course)
    course_count = 0
    
    for lesson_info in lessons:
        lesson = Lesson.objects.create(
            course=course,
            title=lesson_info['title'],
            content=lesson_info['content'],
            order=lesson_info['order'],
            duration_minutes=lesson_info['duration'],
            is_free_preview=True if lesson_info['order'] == 1 else False,
        )
        course_count += 1
        total_added += 1
        print(f"  ✅ Added: {lesson.title}")
    
    if course_count > 0:
        total_courses += 1
        print(f"  📊 Added {course_count} lessons to {course.title}")

print("\n" + "="*70)
print(f"📊 Courses Updated: {total_courses}")
print(f"📚 Total Lessons Added: {total_added}")
print(f"📚 Total Lessons in Database: {Lesson.objects.count()}")
print("🎉 Remaining lesson addition complete!")