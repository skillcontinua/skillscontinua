import os
import sys
import django

# Fix: Add project root to path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from courses.models import Course, Lesson

print("📝 Adding QUIZZES to all courses...")
print("="*60)

quiz_templates = {
    'windows': {
        'questions': [
            {'question': 'What is the default file system for Windows 10?', 
             'options': ['FAT32', 'NTFS', 'exFAT', 'EXT4'], 
             'correct': 1, 'explanation': 'NTFS is the default file system for Windows.'},
            {'question': 'What is the shortcut for Task Manager?', 
             'options': ['Ctrl+Alt+Del', 'Ctrl+Shift+Esc', 'Alt+F4', 'Ctrl+Esc'], 
             'correct': 1, 'explanation': 'Ctrl+Shift+Esc opens Task Manager directly.'},
        ]
    },
    'linux': {
        'questions': [
            {'question': 'What command is used to list files in Linux?', 
             'options': ['ls', 'dir', 'list', 'll'], 
             'correct': 0, 'explanation': 'ls is the command to list files in Linux.'},
            {'question': 'What is the root user in Linux called?', 
             'options': ['admin', 'root', 'superuser', 'master'], 
             'correct': 1, 'explanation': 'root is the superuser in Linux systems.'},
        ]
    },
    'gimp': {
        'questions': [
            {'question': 'What does GIMP stand for?', 
             'options': ['GNU Image Manipulation Program', 'General Image Processing', 'Graphic Interface for Media', 'Global Image Management'], 
             'correct': 0, 'explanation': 'GIMP stands for GNU Image Manipulation Program.'},
            {'question': 'Which tool is used for selecting areas in GIMP?', 
             'options': ['Brush', 'Rectangle Select', 'Color Picker', 'Zoom'], 
             'correct': 1, 'explanation': 'Rectangle Select tool is used for selecting areas.'},
        ]
    },
    'web': {
        'questions': [
            {'question': 'What does HTML stand for?', 
             'options': ['Hyper Text Markup Language', 'High Tech Modern Language', 'Hyper Transfer Markup Language', 'Home Tool Markup Language'], 
             'correct': 0, 'explanation': 'HTML stands for Hyper Text Markup Language.'},
            {'question': 'Which language is used for styling web pages?', 
             'options': ['HTML', 'JavaScript', 'CSS', 'Python'], 
             'correct': 2, 'explanation': 'CSS is used for styling web pages.'},
        ]
    },
    'marine': {
        'questions': [
            {'question': 'What type of engine is commonly used in outboard motors?', 
             'options': ['Two-stroke', 'Four-stroke', 'Diesel', 'Rotary'], 
             'correct': 0, 'explanation': 'Two-stroke engines are common in outboard motors.'},
            {'question': 'What is used to cool marine engines?', 
             'options': ['Air', 'Water', 'Oil', 'Coolant'], 
             'correct': 1, 'explanation': 'Water is used to cool marine engines.'},
        ]
    },
}

generic_quiz = {
    'questions': [
        {'question': 'What is the main objective of this course?', 
         'options': ['To learn new skills', 'To get a certificate', 'To have fun', 'All of the above'], 
         'correct': 0, 'explanation': 'The main objective is to learn new skills.'},
        {'question': 'What is the best way to practice what you learn?', 
         'options': ['Reading more', 'Watching videos', 'Hands-on practice', 'Taking notes'], 
         'correct': 2, 'explanation': 'Hands-on practice is the best way to learn.'},
    ]
}

total_quizzes_added = 0
course_count = 0

for course in Course.objects.filter(is_active=True):
    course_title_lower = course.title.lower()
    matched = False
    
    for key, template in quiz_templates.items():
        if key in course_title_lower:
            print(f"\n📝 Adding quiz to: {course.title}")
            lessons = course.lessons.all()
            if lessons:
                last_lesson = lessons.last()
                quiz_content = "📝 **QUIZ: Test Your Knowledge**\n\n"
                for i, q in enumerate(template['questions'], 1):
                    quiz_content += f"**Question {i}:** {q['question']}\n"
                    quiz_content += "Options:\n"
                    for j, opt in enumerate(q['options']):
                        quiz_content += f"{chr(65+j)}. {opt}\n"
                    quiz_content += f"\n✅ **Answer:** {chr(65+q['correct'])}\n"
                    quiz_content += f"**Explanation:** {q['explanation']}\n\n"
                last_lesson.content += f"\n\n---\n\n{quiz_content}"
                last_lesson.save()
                total_quizzes_added += 1
                print(f"  ✅ Added quiz")
                matched = True
                course_count += 1
            break
    
    if not matched:
        lessons = course.lessons.all()
        if lessons:
            last_lesson = lessons.last()
            quiz_content = "📝 **QUIZ: Test Your Understanding**\n\n"
            for i, q in enumerate(generic_quiz['questions'], 1):
                quiz_content += f"**Question {i}:** {q['question']}\n"
                quiz_content += "Options:\n"
                for j, opt in enumerate(q['options']):
                    quiz_content += f"{chr(65+j)}. {opt}\n"
                quiz_content += f"\n✅ **Answer:** {chr(65+q['correct'])}\n"
                quiz_content += f"**Explanation:** {q['explanation']}\n\n"
            last_lesson.content += f"\n\n---\n\n{quiz_content}"
            last_lesson.save()
            total_quizzes_added += 1
            print(f"✅ Added generic quiz to: {course.title}")
            course_count += 1

print("\n" + "="*60)
print(f"📊 Courses with Quizzes Added: {course_count}")
print(f"📊 Total Quizzes Added: {total_quizzes_added}")
print("🎉 Quiz content addition complete!")