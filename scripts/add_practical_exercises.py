import os
import sys
import django

# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from courses.models import Course, Lesson

print("🛠️ Adding PRACTICAL EXERCISES to all courses...")
print("="*60)

# Practical exercise templates
exercise_templates = {
    # ===== OPERATING SYSTEMS =====
    'windows': {
        'exercises': [
            {'title': 'Exercise 1: File Management', 
             'description': 'Create a folder structure for your personal documents. Include subfolders for Work, Personal, and Projects. Practice copying, moving, and renaming files.'},
            {'title': 'Exercise 2: System Configuration', 
             'description': 'Customize your Windows settings. Change the desktop background, theme, and display settings. Practice using the Control Panel.'},
            {'title': 'Exercise 3: Security Setup', 
             'description': 'Set up Windows Defender, create a system restore point, and configure user accounts with passwords.'},
        ]
    },
    'linux': {
        'exercises': [
            {'title': 'Exercise 1: Command Line Navigation', 
             'description': 'Practice navigating the Linux file system using cd, ls, pwd, and other commands. Create and delete directories and files.'},
            {'title': 'Exercise 2: File Permissions', 
             'description': 'Practice setting file permissions using chmod and chown. Create different user accounts and practice user management.'},
            {'title': 'Exercise 3: Installing Software', 
             'description': 'Install software using apt-get. Update the system and practice uninstalling packages.'},
        ]
    },
    'gimp': {
        'exercises': [
            {'title': 'Exercise 1: Basic Photo Editing', 
             'description': 'Take a photo and practice cropping, resizing, and adjusting colors. Save the image in different formats (JPEG, PNG).'},
            {'title': 'Exercise 2: Layer Work', 
             'description': 'Create a composite image using multiple layers. Practice using layer masks and blending modes.'},
            {'title': 'Exercise 3: Logo Design', 
             'description': 'Design a simple logo using GIMP\'s text and shape tools. Apply different filters and effects.'},
        ]
    },
    'web': {
        'exercises': [
            {'title': 'Exercise 1: Build a Simple Web Page', 
             'description': 'Create a simple HTML page with headings, paragraphs, lists, and images. Practice using different HTML tags.'},
            {'title': 'Exercise 2: Style Your Page', 
             'description': 'Add CSS to style your HTML page. Practice using selectors, properties, and layouts.'},
            {'title': 'Exercise 3: Add Interactivity', 
             'description': 'Add JavaScript to your page for interactivity. Create a button that changes text or displays an alert.'},
        ]
    },
    'digital marketing': {
        'exercises': [
            {'title': 'Exercise 1: SEO Analysis', 
             'description': 'Choose a website and conduct an SEO audit. Identify areas for improvement and create an action plan.'},
            {'title': 'Exercise 2: Social Media Strategy', 
             'description': 'Create a social media content calendar for one week. Include different types of content and engagement strategies.'},
            {'title': 'Exercise 3: Content Creation', 
             'description': 'Write a blog post on a topic of your choice. Include images, headings, and optimize for SEO.'},
        ]
    },
    'marine': {
        'exercises': [
            {'title': 'Exercise 1: Engine Inspection', 
             'description': 'Inspect a marine engine and identify all major components. Create a checklist of items to check during maintenance.'},
            {'title': 'Exercise 2: Troubleshooting', 
             'description': 'Practice diagnosing common marine engine problems. Create a troubleshooting flowchart for common issues.'},
            {'title': 'Exercise 3: Maintenance Schedule', 
             'description': 'Create a comprehensive maintenance schedule for a boat engine. Include daily, weekly, monthly, and yearly tasks.'},
        ]
    },
}

# Generic exercises for any course
generic_exercises = [
    {'title': 'Exercise 1: Research Assignment', 
     'description': 'Research the key topics covered in this course. Prepare a summary of the most important concepts you learned.'},
    {'title': 'Exercise 2: Practical Application', 
     'description': 'Apply what you have learned to a real-world situation. Create a project or plan that demonstrates your understanding.'},
    {'title': 'Exercise 3: Peer Review', 
     'description': 'Share your work with a peer and provide constructive feedback. Review someone else\'s work and offer suggestions for improvement.'},
]

total_exercises_added = 0
course_count = 0

for course in Course.objects.filter(is_active=True):
    course_title_lower = course.title.lower()
    matched = False
    
    # Find matching exercise template
    for key, template in exercise_templates.items():
        if key in course_title_lower:
            print(f"\n🛠️ Adding practical exercises to: {course.title}")
            
            # Add exercises as new lessons or append to existing
            lessons = course.lessons.all()
            exercise_count = 0
            
            for exercise in template['exercises']:
                # Check if exercise already exists as a lesson
                exists = course.lessons.filter(title=exercise['title']).exists()
                if not exists:
                    # Add as a new lesson
                    new_lesson = Lesson.objects.create(
                        course=course,
                        title=exercise['title'],
                        content=f"## 🛠️ {exercise['title']}\n\n{exercise['description']}\n\n### 📝 Instructions:\n1. Read the exercise description carefully\n2. Gather necessary materials\n3. Complete the exercise step by step\n4. Document your results\n5. Review your work\n\n### ✅ Checklist:\n- [ ] Understood the exercise\n- [ ] Completed the exercise\n- [ ] Documented the results\n- [ ] Reviewed the work\n\n### 📚 Resources:\n- Course materials\n- Online tutorials\n- Community support",
                        order=course.lessons.count() + 1,
                        duration_minutes=30,
                        is_free_preview=False,
                    )
                    total_exercises_added += 1
                    exercise_count += 1
                    print(f"  ✅ Added exercise: {exercise['title']}")
                else:
                    print(f"  📚 Exercise already exists: {exercise['title']}")
            
            matched = True
            course_count += 1
            break
    
    # If no specific template found, add generic exercises
    if not matched:
        print(f"\n🛠️ Adding generic exercises to: {course.title}")
        for exercise in generic_exercises:
            exists = course.lessons.filter(title=exercise['title']).exists()
            if not exists:
                new_lesson = Lesson.objects.create(
                    course=course,
                    title=exercise['title'],
                    content=f"## 🛠️ {exercise['title']}\n\n{exercise['description']}\n\n### 📝 Instructions:\n1. Review the exercise carefully\n2. Plan your approach\n3. Execute the task\n4. Document your findings\n5. Reflect on your learning\n\n### ✅ Checklist:\n- [ ] Understood the exercise\n- [ ] Completed the exercise\n- [ ] Documented the results\n- [ ] Reflected on learning\n\n### 📚 Additional Resources:\n- Course materials\n- Online research\n- Peer support",
                    order=course.lessons.count() + 1,
                    duration_minutes=25,
                    is_free_preview=False,
                )
                total_exercises_added += 1
                print(f"  ✅ Added exercise: {exercise['title']}")
        course_count += 1

print("\n" + "="*60)
print(f"📊 Courses with Exercises Added: {course_count}")
print(f"📊 Total Exercises Added: {total_exercises_added}")
print(f"📚 Total Lessons in Database: {Lesson.objects.count()}")
print("🎉 Practical exercise addition complete!")