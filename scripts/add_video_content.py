import os
import sys
import django

# Fix: Add project root to path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from courses.models import Course, Lesson

print("🎥 Adding VIDEO CONTENT to all courses...")
print("="*60)

# Video resources dictionary (simplified)
video_resources = {
    'windows': {
        'playlist': 'https://www.youtube.com/playlist?list=PL6oDA8S3RmtGp6m-3r7Fq8XfQ9p5XeVhN',
        'videos': [
            {'title': 'Windows 10/11 Complete Tutorial', 'url': 'https://www.youtube.com/watch?v=J6OyY-JI8jM'},
            {'title': 'Windows Installation Guide', 'url': 'https://www.youtube.com/watch?v=4z0FvDx0qSY'},
        ]
    },
    'linux': {
        'playlist': 'https://www.youtube.com/playlist?list=PLT98CRl2KxKHaKA9_4KgV4XjJx_Q5qMbK',
        'videos': [
            {'title': 'Linux for Beginners', 'url': 'https://www.youtube.com/watch?v=V1y-mbWM3B8'},
            {'title': 'Ubuntu Installation Guide', 'url': 'https://www.youtube.com/watch?v=Jp1wGdN0RqE'},
        ]
    },
    'gimp': {
        'playlist': 'https://www.youtube.com/playlist?list=PLHqvHhD8xkVbHwZ1vWbNn5TXVzclRfXlB',
        'videos': [
            {'title': 'GIMP Complete Tutorial for Beginners', 'url': 'https://www.youtube.com/watch?v=D0psu2vLW-M'},
            {'title': 'GIMP Photo Editing Mastery', 'url': 'https://www.youtube.com/watch?v=7vxr1H2fzN8'},
        ]
    },
    'web': {
        'playlist': 'https://www.youtube.com/playlist?list=PLoYCgNOIyGAB_8_iq1cL8MVeun7cB6eNc',
        'videos': [
            {'title': 'HTML & CSS Full Course', 'url': 'https://www.youtube.com/watch?v=G3e-cpL7ofc'},
            {'title': 'JavaScript Fundamentals', 'url': 'https://www.youtube.com/watch?v=PkZNo7MFNFg'},
        ]
    },
    'marine': {
        'playlist': 'https://www.youtube.com/playlist?list=PLvJ3T3Rk1Cza0kR7tZ-qm9-sds7dFkRjS',
        'videos': [
            {'title': 'Boat Engine Repair Basics', 'url': 'https://www.youtube.com/watch?v=zY9P7QvXeFc'},
            {'title': 'Outboard Motor Maintenance', 'url': 'https://www.youtube.com/watch?v=HwQ6TJu4Iw0'},
        ]
    },
}

total_videos_added = 0
course_count = 0

for course in Course.objects.filter(is_active=True):
    course_title_lower = course.title.lower()
    matched = False
    
    for key, resources in video_resources.items():
        if key in course_title_lower:
            print(f"\n📹 Adding videos to: {course.title}")
            
            first_lesson = course.lessons.first()
            if first_lesson:
                first_lesson.video_url = resources['playlist']
                first_lesson.save()
                print(f"  ✅ Added playlist")
            
            lesson_index = 0
            for video in resources['videos']:
                lessons = course.lessons.all()
                if lesson_index < len(lessons):
                    lesson = lessons[lesson_index]
                    if not lesson.video_url:
                        lesson.video_url = video['url']
                        lesson.save()
                        total_videos_added += 1
                        print(f"  ✅ Added video: {video['title']}")
                lesson_index += 1
            
            matched = True
            course_count += 1
            break

print("\n" + "="*60)
print(f"📊 Courses Updated with Videos: {course_count}")
print(f"📊 Total Videos Added: {total_videos_added}")
print("🎉 Video content addition complete!")