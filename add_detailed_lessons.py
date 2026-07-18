import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from courses.models import Course, Lesson

print("📚 Adding detailed lessons to ALL courses (10 lessons each)...")

# Get all courses
all_courses = Course.objects.filter(is_active=True)
print(f"Found {all_courses.count()} courses")

total_added = 0

for course in all_courses:
    # Check if course already has lessons
    existing_count = course.lessons.count()
    
    if existing_count >= 10:
        print(f"📚 {course.title}: Already has {existing_count} lessons (skipping)")
        continue
    
    print(f"\n📖 Adding detailed lessons to: {course.title} (existing: {existing_count})")
    
    # Create detailed lessons based on course title and approach
    course_title = course.title
    approach = course.learning_approach
    
    # Define lesson templates based on learning approach
    if approach == 'pedagogic':
        # Child-friendly lessons with fun activities
        lessons = [
            {'title': f'Welcome to {course_title}!', 'content': f"Welcome, young learner! This course will help you learn about {course_title} in a fun and exciting way. Let's get started!", 'order': 1, 'duration': 15},
            {'title': 'Let\'s Learn Together', 'content': 'In this lesson, we will explore the basics together. Remember, learning is fun when we do it with friends and family.', 'order': 2, 'duration': 20},
            {'title': 'Fun Activities and Games', 'content': 'Time for some fun activities! These games will help you remember what you learn. Get ready to play and learn!', 'order': 3, 'duration': 25},
            {'title': 'Discovering New Things', 'content': 'Every day is a chance to discover something new. Let\'s explore interesting facts and ideas together.', 'order': 4, 'duration': 20},
            {'title': 'Practice Makes Perfect', 'content': 'Practice what you have learned. Try these exercises and see how much you have improved.', 'order': 5, 'duration': 25},
            {'title': 'Stories and Examples', 'content': 'Stories help us understand better. Listen to these stories and learn from real-life examples.', 'order': 6, 'duration': 20},
            {'title': 'Working with Others', 'content': 'Learning is better when we help each other. Learn how to work with friends and share what you know.', 'order': 7, 'duration': 20},
            {'title': 'Creative Thinking', 'content': 'Use your imagination and creativity. Think of new ideas and express yourself in different ways.', 'order': 8, 'duration': 25},
            {'title': 'Review and Remember', 'content': 'Let\'s review what we have learned. These exercises will help you remember everything.', 'order': 9, 'duration': 20},
            {'title': 'Celebrating Your Progress', 'content': 'Well done! You have completed this course. Celebrate your progress and think about what you want to learn next.', 'order': 10, 'duration': 15},
        ]
    elif approach == 'andragogic':
        # Adult-focused practical lessons
        lessons = [
            {'title': f'Introduction to {course_title}', 'content': f'Welcome to {course_title}. This course is designed to give you practical, actionable skills that you can apply immediately in your personal and professional life.', 'order': 1, 'duration': 25},
            {'title': 'Understanding the Fundamentals', 'content': 'Master the core principles and foundational knowledge. This is the building block for everything else in this course.', 'order': 2, 'duration': 30},
            {'title': 'Practical Applications', 'content': 'Learn how to apply these skills in real-world situations. These practical examples will help you see immediate results.', 'order': 3, 'duration': 35},
            {'title': 'Case Studies and Examples', 'content': 'Study real-life case studies and examples. Learn from the experiences of others and see how these skills have been applied successfully.', 'order': 4, 'duration': 30},
            {'title': 'Tools and Resources', 'content': 'Discover the tools, resources, and techniques that professionals use. Get hands-on experience with practical exercises.', 'order': 5, 'duration': 35},
            {'title': 'Challenges and Solutions', 'content': 'Identify common challenges and learn proven solutions. This will prepare you to handle real situations confidently.', 'order': 6, 'duration': 30},
            {'title': 'Professional Development', 'content': 'Take your skills to the next level. Learn how to advance in your career and achieve your professional goals.', 'order': 7, 'duration': 30},
            {'title': 'Networking and Collaboration', 'content': 'Build professional relationships and learn to collaborate effectively. Success often comes from working well with others.', 'order': 8, 'duration': 25},
            {'title': 'Continuous Learning', 'content': 'Discover strategies for ongoing growth. Learning is a lifelong journey, and this lesson will help you continue improving.', 'order': 9, 'duration': 30},
            {'title': 'Action Plan and Next Steps', 'content': 'Create your personal action plan. Identify your next steps and start applying everything you have learned.', 'order': 10, 'duration': 25},
        ]
    else:  # heutagogic - advanced, self-directed
        lessons = [
            {'title': f'Mastering {course_title}', 'content': f'Welcome to this advanced course on {course_title}. This is designed for self-directed learners ready to achieve mastery.', 'order': 1, 'duration': 30},
            {'title': 'Advanced Theories and Frameworks', 'content': 'Explore the advanced theories and frameworks that underpin this field. Deepen your understanding of the core concepts.', 'order': 2, 'duration': 35},
            {'title': 'Strategic Thinking and Analysis', 'content': 'Develop strategic thinking skills and learn to analyze complex situations. This lesson focuses on higher-order thinking.', 'order': 3, 'duration': 40},
            {'title': 'Innovation and Creativity', 'content': 'Push boundaries and think creatively. Learn to innovate and find new solutions to complex problems.', 'order': 4, 'duration': 35},
            {'title': 'Leadership and Influence', 'content': 'Develop leadership skills and learn to influence others positively. Great leaders continuously learn and grow.', 'order': 5, 'duration': 35},
            {'title': 'Complex Problem Solving', 'content': 'Tackle complex, real-world problems using advanced problem-solving frameworks.', 'order': 6, 'duration': 40},
            {'title': 'Research and Evidence-Based Practice', 'content': 'Learn to conduct research and use evidence to inform your decisions and practice.', 'order': 7, 'duration': 35},
            {'title': 'Systems Thinking', 'content': 'Understand how systems work and learn to think holistically about challenges and solutions.', 'order': 8, 'duration': 35},
            {'title': 'Mentorship and Knowledge Sharing', 'content': 'Learn to mentor others and share your knowledge effectively. Teaching is one of the best ways to deepen understanding.', 'order': 9, 'duration': 30},
            {'title': 'Mastery and Continued Excellence', 'content': 'Achieve mastery and plan for continued excellence. This is the beginning of your journey to becoming a thought leader.', 'order': 10, 'duration': 30},
        ]
    
    # Add lessons (skip existing ones to avoid duplicates)
    added_count = 0
    for lesson_data in lessons:
        # Check if lesson already exists
        exists = Lesson.objects.filter(course=course, title=lesson_data['title']).exists()
        if not exists:
            lesson = Lesson.objects.create(
                course=course,
                title=lesson_data['title'],
                content=lesson_data['content'],
                order=lesson_data['order'],
                duration_minutes=lesson_data['duration'],
                is_free_preview=True if lesson_data['order'] == 1 else False,
            )
            added_count += 1
            total_added += 1
            print(f"  ✅ Added: {lesson.title}")
    
    if added_count > 0:
        print(f"  📊 Added {added_count} new lessons to {course.title}")
    elif existing_count >= 10:
        print(f"  📚 Course already has 10+ lessons ({existing_count})")

print("\n" + "="*60)
print(f"📊 Total New Lessons Added: {total_added}")
print(f"📚 Total Lessons in Database: {Lesson.objects.count()}")

# Summary by approach
print("\n📊 Summary by Learning Approach:")
for approach in ['pedagogic', 'andragogic', 'heutagogic']:
    courses = Course.objects.filter(learning_approach=approach, is_active=True)
    for course in courses:
        lesson_count = course.lessons.count()
        if lesson_count > 0:
            print(f"  📖 {course.title[:40]}... ({approach.upper()}): {lesson_count} lessons")

print("\n🎉 Detailed lesson addition complete!")