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
print("📚 ENRICHING COURSE CONTENT - ADDING DETAILED LESSONS")
print("="*70)

# Detailed lesson templates for different course types
lesson_templates = {
    # ===== COMPUTER & OPERATING SYSTEMS =====
    'windows': {
        'title': 'Windows OS Complete',
        'lessons': [
            {'title': 'Introduction to Windows OS', 'content': 'Windows is the world\'s most popular operating system. This lesson covers the history, versions, and basic navigation of Windows. You\'ll learn about the desktop, taskbar, start menu, and file explorer.', 'duration': 30},
            {'title': 'Windows Installation and Setup', 'content': 'Learn to install Windows from scratch. This includes creating a bootable USB, partitioning drives, and completing the initial setup. System requirements and troubleshooting covered.', 'duration': 45},
            {'title': 'Windows File Management', 'content': 'Master file management in Windows. Learn about File Explorer, creating folders, copying/moving files, and understanding file permissions.', 'duration': 35},
            {'title': 'Windows System Settings', 'content': 'Configure Windows system settings including display, network, privacy, and security. Learn about Control Panel vs Settings app.', 'duration': 40},
            {'title': 'Windows Security and Maintenance', 'content': 'Keep your Windows system secure. Learn about Windows Defender, firewall settings, regular maintenance, backups, and troubleshooting.', 'duration': 35},
            {'title': 'Windows Networking and Internet', 'content': 'Configure network settings, connect to Wi-Fi, set up sharing, and troubleshoot network issues. Understand IP addresses, DNS, and basic network concepts.', 'duration': 30},
            {'title': 'Windows Troubleshooting and Recovery', 'content': 'Learn to troubleshoot common Windows problems, use recovery tools, system restore, and advanced recovery options.', 'duration': 35},
            {'title': 'Windows Performance Optimization', 'content': 'Optimize Windows performance - managing startup programs, cleaning disk space, defragmentation, and performance monitoring tools.', 'duration': 30},
            {'title': 'Windows Command Line and PowerShell', 'content': 'Master Windows command-line tools and PowerShell scripting for system administration and automation.', 'duration': 40},
            {'title': 'Windows Advanced Administration', 'content': 'Advanced Windows administration - group policies, Active Directory, user management, and enterprise Windows environments.', 'duration': 45},
        ]
    },
    # ===== GRAPHICS & DESIGN =====
    'gimp': {
        'title': 'GIMP Professional',
        'lessons': [
            {'title': 'Introduction to GIMP', 'content': 'GIMP is a free and open-source image editor. This lesson covers the interface, tools, and basic image editing concepts. You\'ll learn about layers, selections, and basic adjustments.', 'duration': 30},
            {'title': 'Basic Image Editing', 'content': 'Learn to crop, resize, rotate, and adjust colors. You\'ll also learn about layers, selection tools, and working with different file formats (JPEG, PNG, GIF).', 'duration': 35},
            {'title': 'Working with Layers', 'content': 'Master layers in GIMP - layer masks, blending modes, layer groups, and advanced layer techniques for professional editing.', 'duration': 40},
            {'title': 'Photo Retouching', 'content': 'Professional photo retouching techniques - removing blemishes, restoring old photos, color correction, and skin smoothing.', 'duration': 45},
            {'title': 'Creating Graphics for Web and Print', 'content': 'Create graphics for web design, social media, and print. Includes designing banners, social media posts, and understanding resolution and DPI.', 'duration': 40},
            {'title': 'GIMP Advanced Techniques', 'content': 'Master advanced GIMP techniques including filters, effects, text tools, and creating professional designs. Learn about paths, text effects, and advanced color manipulation.', 'duration': 45},
            {'title': 'Photo Manipulation and Compositing', 'content': 'Create complex image compositions using multiple images, masks, and advanced blending techniques.', 'duration': 50},
            {'title': 'GIMP for Graphic Design', 'content': 'Apply GIMP skills to real-world graphic design projects - logos, posters, flyers, and marketing materials.', 'duration': 40},
            {'title': 'GIMP for Photography', 'content': 'Professional photo editing workflow using GIMP - RAW processing, color grading, and photo enhancement techniques.', 'duration': 35},
            {'title': 'GIMP Projects and Portfolio', 'content': 'Complete a professional portfolio using GIMP. Create a series of images for your portfolio and learn to present your work.', 'duration': 45},
        ]
    },
    # ===== MUSIC =====
    'music': {
        'title': 'Music Complete',
        'lessons': [
            {'title': 'Music Theory Fundamentals', 'content': 'Learn the basics of music theory - notes, scales, chords, rhythm, harmony, and musical notation. Essential knowledge for all musicians.', 'duration': 35},
            {'title': 'Reading Music Notation', 'content': 'Learn to read and write music notation - clefs, time signatures, key signatures, and all musical symbols needed for performance.', 'duration': 40},
            {'title': 'Rhythm and Timing', 'content': 'Master rhythm and timing - note values, rests, time signatures, syncopation, and rhythm patterns for different musical styles.', 'duration': 30},
            {'title': 'Harmony and Chord Progressions', 'content': 'Understand harmony - chord construction, chord progressions, and harmonic analysis for creating rich musical arrangements.', 'duration': 35},
            {'title': 'Ear Training and Aural Skills', 'content': 'Develop your ear - interval recognition, chord identification, rhythmic dictation, and melodic transcription.', 'duration': 30},
            {'title': 'Instrument Technique', 'content': 'Learn proper technique for your instrument - posture, hand position, breath control, and practice strategies for improvement.', 'duration': 35},
            {'title': 'Music Composition and Arranging', 'content': 'Learn to compose and arrange music - creating melodies, writing harmonies, and arranging for different instruments and voices.', 'duration': 40},
            {'title': 'Music Production Fundamentals', 'content': 'Introduction to music production - DAWs, MIDI, audio recording, mixing, and modern music production techniques.', 'duration': 35},
            {'title': 'Music History and Appreciation', 'content': 'Explore music history - from ancient music to modern styles. Learn to appreciate different genres and cultural music traditions.', 'duration': 30},
            {'title': 'Performance and Presentation', 'content': 'Master performance skills - stage presence, overcoming performance anxiety, and presenting yourself as a professional musician.', 'duration': 30},
        ]
    },
    # ===== GENERIC (for any course without specific template) =====
    'generic': {
        'title': 'Complete Course',
        'lessons': [
            {'title': 'Introduction to the Course', 'content': 'Welcome to this comprehensive course. This introduction covers what you\'ll learn, how to succeed, and the resources available to you.', 'duration': 25},
            {'title': 'Core Concepts and Fundamentals', 'content': 'Master the essential concepts and foundational knowledge. This is the building block for everything else in this course.', 'duration': 30},
            {'title': 'Practical Applications', 'content': 'Learn to apply what you\'ve learned to real-world situations. This lesson covers practical examples and hands-on exercises.', 'duration': 35},
            {'title': 'Advanced Techniques and Tools', 'content': 'Explore advanced techniques and tools used by professionals. Learn to use industry-standard practices and workflows.', 'duration': 35},
            {'title': 'Case Studies and Examples', 'content': 'Study real-world case studies and examples. Learn from the experiences of others and see how these skills are applied professionally.', 'duration': 30},
            {'title': 'Common Challenges and Solutions', 'content': 'Identify common challenges and learn proven solutions. This lesson prepares you to handle real situations confidently.', 'duration': 30},
            {'title': 'Professional Development', 'content': 'Take your skills to the next level. Learn how to advance in your career and achieve your professional goals.', 'duration': 30},
            {'title': 'Networking and Collaboration', 'content': 'Build professional relationships and learn to collaborate effectively. Success often comes from working well with others.', 'duration': 25},
            {'title': 'Continuous Learning', 'content': 'Discover strategies for ongoing growth. Learning is a lifelong journey, and this lesson will help you continue improving.', 'duration': 30},
            {'title': 'Final Project and Portfolio', 'content': 'Complete a comprehensive project that demonstrates your skills. Build your portfolio and prepare to showcase your work.', 'duration': 40},
        ]
    }
}

# Process all courses
total_lessons_added = 0
course_count = 0

for course in Course.objects.filter(is_active=True):
    course_title_lower = course.title.lower()
    matched_template = None
    
    # Find matching template
    for key, template in lesson_templates.items():
        if key in course_title_lower:
            matched_template = template
            break
    
    # Use generic if no match
    if not matched_template:
        matched_template = lesson_templates['generic']
    
    # Check if course already has lessons
    existing_count = course.lessons.count()
    if existing_count >= 10:
        print(f"📚 {course.title}: Already has {existing_count} lessons (skipping)")
        continue
    
    print(f"\n📖 Adding lessons to: {course.title}")
    
    # Add lessons
    added_count = 0
    for lesson_data in matched_template['lessons'][:10]:  # Max 10 lessons
        # Check if lesson already exists
        exists = Lesson.objects.filter(course=course, title=lesson_data['title']).exists()
        if not exists:
            lesson = Lesson.objects.create(
                course=course,
                title=lesson_data['title'],
                content=lesson_data['content'] + "\n\n📚 **Learning Resources:**\n• Course materials\n• Online resources\n• Practice exercises\n\n📝 **Exercise:** Practice the concepts covered in this lesson.",
                order=lesson_data.get('order', existing_count + added_count + 1),
                duration_minutes=lesson_data['duration'],
                is_free_preview=added_count == 0,
            )
            added_count += 1
            total_lessons_added += 1
            print(f"  ✅ Added: {lesson.title}")
    
    if added_count > 0:
        course_count += 1
        print(f"  📊 Added {added_count} lessons to {course.title}")

print("\n" + "="*70)
print("📊 SUMMARY")
print("="*70)
print(f"✅ Courses Updated: {course_count}")
print(f"📚 Total Lessons Added: {total_lessons_added}")
print(f"📚 Total Lessons in Database: {Lesson.objects.count()}")
print("="*70)
print("🎉 Course content enrichment complete!")