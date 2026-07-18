import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from courses.models import Course, Lesson

print("📚 Adding lessons to courses that are empty...")

# Find empty courses
empty_courses = []
for course in Course.objects.filter(is_active=True):
    if course.lessons.count() == 0:
        empty_courses.append(course)

print(f"Found {len(empty_courses)} empty courses")

if len(empty_courses) == 0:
    print("🎉 All courses already have lessons!")
    exit()

total_added = 0

for course in empty_courses:
    print(f"\n📖 Adding lessons to: {course.title}")
    
    # Generic lessons based on level
    if course.level == 'beginner':
        lesson_list = [
            {'title': f'Introduction to {course.title}', 'content': f'Welcome to {course.title}. This course will help you develop essential skills.', 'order': 1, 'duration': 20},
            {'title': 'Understanding the Basics', 'content': 'Learn the fundamental concepts and principles.', 'order': 2, 'duration': 25},
            {'title': 'Practical Exercises', 'content': 'Apply what you have learned through practical exercises.', 'order': 3, 'duration': 30},
            {'title': 'Review and Practice', 'content': 'Review key concepts and practice your skills.', 'order': 4, 'duration': 25},
            {'title': 'Next Steps', 'content': 'Plan your continued learning journey.', 'order': 5, 'duration': 20},
        ]
    elif course.level == 'intermediate':
        lesson_list = [
            {'title': f'Advanced Introduction to {course.title}', 'content': f'Building on your existing knowledge of {course.title}.', 'order': 1, 'duration': 25},
            {'title': 'Core Principles and Theories', 'content': 'Understand the underlying principles and theories.', 'order': 2, 'duration': 30},
            {'title': 'Practical Applications', 'content': 'Apply advanced concepts to real situations.', 'order': 3, 'duration': 35},
            {'title': 'Case Studies', 'content': 'Learn from real-world examples and case studies.', 'order': 4, 'duration': 30},
            {'title': 'Challenges and Problem Solving', 'content': 'Tackle complex problems and challenges.', 'order': 5, 'duration': 35},
            {'title': 'Continuous Improvement', 'content': 'Strategies for ongoing growth and skill development.', 'order': 6, 'duration': 25},
        ]
    else:  # advanced
        lesson_list = [
            {'title': f'Mastering {course.title}', 'content': f'Advanced concepts and deep dive into {course.title}.', 'order': 1, 'duration': 30},
            {'title': 'Advanced Theories and Frameworks', 'content': 'Study the advanced theoretical frameworks.', 'order': 2, 'duration': 35},
            {'title': 'Strategic Applications', 'content': 'Apply your knowledge at a strategic level.', 'order': 3, 'duration': 35},
            {'title': 'Innovation and Creativity', 'content': 'Push boundaries and explore innovative approaches.', 'order': 4, 'duration': 30},
            {'title': 'Leadership and Influence', 'content': 'Lead and inspire others in this field.', 'order': 5, 'duration': 35},
            {'title': 'Mastery and Continued Growth', 'content': 'Achieve mastery and plan your continued development.', 'order': 6, 'duration': 30},
        ]
    
    for lesson_data in lesson_list:
        lesson, created = Lesson.objects.get_or_create(
            course=course,
            title=lesson_data['title'],
            defaults={
                'content': lesson_data['content'],
                'order': lesson_data['order'],
                'duration_minutes': lesson_data['duration'],
                'is_free_preview': True if lesson_data['order'] == 1 else False,
            }
        )
        if created:
            total_added += 1
            print(f"  ✅ Added: {lesson.title}")

print("\n" + "="*50)
print(f"📊 Total Lessons Added: {total_added}")
print(f"📚 Total Lessons in Database: {Lesson.objects.count()}")
print("🎉 Lesson addition complete!")