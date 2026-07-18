import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from courses.models import Course, Lesson

print("📚 Adding lessons to CORE courses...")

# Lessons for core courses
core_lessons = {
    'Financial Management for Adults': [
        {'title': 'Introduction to Financial Management', 'content': 'Understanding the importance of financial management and setting financial goals.', 'order': 1, 'duration': 30},
        {'title': 'Creating a Budget', 'content': 'Step-by-step guide to creating and maintaining a personal budget.', 'order': 2, 'duration': 35},
        {'title': 'Saving and Emergency Funds', 'content': 'Why saving matters and how to build an emergency fund.', 'order': 3, 'duration': 25},
        {'title': 'Understanding Credit and Debt', 'content': 'How credit works, managing debt, and building a good credit history.', 'order': 4, 'duration': 30},
        {'title': 'Investing Basics', 'content': 'Introduction to different investment options and building wealth over time.', 'order': 5, 'duration': 35},
        {'title': 'Retirement Planning', 'content': 'Planning for retirement and securing your financial future.', 'order': 6, 'duration': 30},
        {'title': 'Entrepreneurship and Business Finance', 'content': 'Managing finances for small businesses and startups.', 'order': 7, 'duration': 35},
    ],
    'Advanced Communication Skills': [
        {'title': 'Principles of Effective Communication', 'content': 'Understanding the fundamentals of clear and effective communication.', 'order': 1, 'duration': 25},
        {'title': 'Active Listening Skills', 'content': 'How to listen actively and understand others better.', 'order': 2, 'duration': 30},
        {'title': 'Public Speaking and Presentation', 'content': 'Techniques for speaking confidently in public and delivering presentations.', 'order': 3, 'duration': 35},
        {'title': 'Non-Verbal Communication', 'content': 'Understanding body language, facial expressions, and tone of voice.', 'order': 4, 'duration': 25},
        {'title': 'Written Communication', 'content': 'Writing emails, reports, and professional documents effectively.', 'order': 5, 'duration': 30},
        {'title': 'Conflict Resolution', 'content': 'Managing and resolving conflicts in personal and professional settings.', 'order': 6, 'duration': 30},
        {'title': 'Persuasion and Influence', 'content': 'Techniques for persuading others and building influence.', 'order': 7, 'duration': 35},
    ],
    'Logic and Critical Thinking': [
        {'title': 'Introduction to Logic', 'content': 'Understanding logical thinking and why it matters.', 'order': 1, 'duration': 25},
        {'title': 'Identifying Arguments', 'content': 'How to identify and analyze arguments in everyday life.', 'order': 2, 'duration': 30},
        {'title': 'Common Logical Fallacies', 'content': 'Recognizing and avoiding common errors in reasoning.', 'order': 3, 'duration': 35},
        {'title': 'Deductive Reasoning', 'content': 'Understanding deductive reasoning and how to use it.', 'order': 4, 'duration': 30},
        {'title': 'Inductive Reasoning', 'content': 'Understanding inductive reasoning and making sound generalizations.', 'order': 5, 'duration': 30},
        {'title': 'Critical Thinking in Decision Making', 'content': 'Applying critical thinking to make better decisions.', 'order': 6, 'duration': 35},
        {'title': 'Problem Solving Frameworks', 'content': 'Using structured approaches to solve complex problems.', 'order': 7, 'duration': 35},
    ],
    'Qualitative and Quantitative Appraisal': [
        {'title': 'Understanding Appraisal Methods', 'content': 'Introduction to qualitative and quantitative appraisal techniques.', 'order': 1, 'duration': 30},
        {'title': 'Qualitative Research Methods', 'content': 'Understanding interviews, focus groups, and observational research.', 'order': 2, 'duration': 35},
        {'title': 'Quantitative Research Methods', 'content': 'Understanding surveys, experiments, and statistical analysis.', 'order': 3, 'duration': 35},
        {'title': 'Data Collection Techniques', 'content': 'How to collect reliable and valid data for appraisal.', 'order': 4, 'duration': 30},
        {'title': 'Data Analysis and Interpretation', 'content': 'Analyzing data and drawing meaningful conclusions.', 'order': 5, 'duration': 35},
        {'title': 'Making Evidence-Based Decisions', 'content': 'Using appraisal results to make informed decisions.', 'order': 6, 'duration': 30},
        {'title': 'Reporting and Presenting Findings', 'content': 'How to communicate appraisal results effectively.', 'order': 7, 'duration': 35},
    ],
}

total_added = 0
for course_title, lessons in core_lessons.items():
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
                    'is_free_preview': True if lesson_data['order'] == 1 else False,
                }
            )
            if created:
                total_added += 1
                print(f"  ✅ Added: {lesson.title}")
            else:
                print(f"  📚 Already exists: {lesson.title}")
    except Course.DoesNotExist:
        print(f"⚠️ Course '{course_title}' not found - skipping")

print(f"\n" + "="*50)
print(f"📊 Total Core Lessons Added: {total_added}")
print(f"📚 Total Lessons in Database: {Lesson.objects.count()}")
print("🎉 Core lesson addition complete!")