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
print("📚 ADDING LESSONS TO COURSES WITH NO LESSONS")
print("="*70)

# Find courses with no lessons
no_lessons = []
for course in Course.objects.filter(is_active=True):
    if course.lessons.count() == 0:
        no_lessons.append(course)

print(f"Found {len(no_lessons)} courses with no lessons")

def generate_lesson_content(course_title, category_name, lesson_num, total_lessons):
    """Generate content for each lesson"""
    return f"""
## {course_title} - Lesson {lesson_num} of {total_lessons}

This lesson covers essential concepts in {course_title} within the context of {category_name}.

### Learning Objectives
- Understand the core concepts of this lesson
- Apply practical skills in real-world scenarios
- Develop problem-solving abilities
- Build confidence in your knowledge

### Key Concepts
1. **Fundamentals:** Understanding the basics
2. **Practical Application:** How to use what you learn
3. **Common Challenges:** What to watch out for
4. **Best Practices:** Professional approaches

### Step-by-Step Guide
1. **Preparation:** Gather materials and information
2. **Study:** Learn the concepts thoroughly
3. **Practice:** Apply what you've learned
4. **Review:** Evaluate your progress

### Practical Exercise
- Apply the concepts you've learned
- Document your approach and results
- Reflect on what worked and what could be improved

### Summary
This lesson has introduced you to key concepts in {course_title}. Continue practicing to build your expertise.

### Next Steps
- Review the material if needed
- Practice the skills learned
- Proceed to the next lesson
"""

total_lessons_added = 0

for course in no_lessons:
    print(f"\n📖 Adding lessons to: {course.title}")
    
    # Add 5 lessons per course
    for i in range(1, 6):
        lesson = Lesson.objects.create(
            course=course,
            title=f"Lesson {i}: Introduction to {course.title}",
            content=generate_lesson_content(course.title, course.category.name, i, 5),
            order=i,
            duration_minutes=30,
            is_free_preview=True if i == 1 else False,
        )
        total_lessons_added += 1
        print(f"  ✅ Added: {lesson.title}")

print("\n" + "="*70)
print(f"📊 Total Lessons Added: {total_lessons_added}")
print(f"📚 Total Lessons in Database: {Lesson.objects.count()}")
print("🎉 Lesson addition complete!")