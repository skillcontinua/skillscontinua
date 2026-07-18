import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from courses.models import Course, Lesson

print("📚 Adding DETAILED LESSON CONTENT to all courses...")
print("="*60)

# Comprehensive lesson templates for different course types
lesson_templates = {
    # ===== OPERATING SYSTEMS =====
    'windows': {
        'lessons': [
            {'title': 'Introduction to Windows OS', 
             'content': 'Windows is the world\'s most popular operating system. In this lesson, you\'ll learn about the history of Windows, different versions (Windows 10, 11), and basic navigation. You\'ll understand the desktop environment, taskbar, start menu, and how to customize your workspace.\n\n📚 **Resources:**\n• Microsoft Support: https://support.microsoft.com/windows\n• Windows 11 Tutorial: https://support.microsoft.com/en-us/windows\n\n📝 **Exercise:** Explore your Windows desktop and identify all the elements you can see.',
             'order': 1, 'duration': 30, 'free': True},
            
            {'title': 'Windows Installation and Setup', 
             'content': 'Learn to install Windows from scratch. This covers creating a bootable USB drive, system requirements, partitioning, and completing the installation. You\'ll also learn about initial configuration and driver installation.\n\n📚 **Resources:**\n• Windows Installation Guide: https://support.microsoft.com/windows/install\n• Rufus (Bootable USB): https://rufus.ie/\n\n📝 **Exercise:** Create a Windows installation USB using Rufus.',
             'order': 2, 'duration': 45, 'free': False},
            
            {'title': 'Windows File Management', 
             'content': 'Master file management in Windows. You\'ll learn about File Explorer, creating and organizing folders, copying, moving, and deleting files. Understand file permissions, properties, and how to search for files effectively.\n\n📚 **Resources:**\n• File Explorer Tutorial: https://support.microsoft.com/file-explorer\n\n📝 **Exercise:** Create a folder structure for your documents with proper organization.',
             'order': 3, 'duration': 35, 'free': False},
            
            {'title': 'Windows System Settings and Control Panel', 
             'content': 'Learn to configure Windows system settings. This covers display settings, network configuration, user accounts, privacy settings, and understanding the Control Panel vs Settings app.\n\n📚 **Resources:**\n• Windows Settings Guide: https://support.microsoft.com/settings\n\n📝 **Exercise:** Customize your display settings and configure a new user account.',
             'order': 4, 'duration': 40, 'free': False},
            
            {'title': 'Windows Security and Maintenance', 
             'content': 'Keep your Windows system secure. Learn about Windows Defender, firewall configuration, regular maintenance tasks, backup strategies, and troubleshooting common issues.\n\n📚 **Resources:**\n• Windows Security: https://support.microsoft.com/security\n• Windows Update: https://support.microsoft.com/update\n\n📝 **Exercise:** Run a full system scan and check for Windows updates.',
             'order': 5, 'duration': 35, 'free': False},
            
            {'title': 'Windows Networking and Internet', 
             'content': 'Learn to configure network settings, connect to Wi-Fi, set up sharing, and troubleshoot network issues. Understand IP addresses, DNS, and basic network concepts.\n\n📚 **Resources:**\n• Windows Networking Guide\n\n📝 **Exercise:** Connect to a Wi-Fi network and share a folder on your network.',
             'order': 6, 'duration': 30, 'free': False},
            
            {'title': 'Windows Troubleshooting and Recovery', 
             'content': 'Learn to troubleshoot common Windows problems, use recovery tools, system restore, and advanced recovery options. Understand when to use Safe Mode and how to reset your PC.\n\n📚 **Resources:**\n• Windows Recovery Options: https://support.microsoft.com/recovery\n\n📝 **Exercise:** Create a system restore point and learn to boot into Safe Mode.',
             'order': 7, 'duration': 35, 'free': False},
        ]
    },
    
    'linux': {
        'lessons': [
            {'title': 'Introduction to Linux and Open Source', 
             'content': 'Linux is a free and open-source operating system. This lesson covers the history, philosophy of open source, different Linux distributions (Ubuntu, Fedora, Linux Mint), and why Linux is important for developing nations.\n\n📚 **Resources:**\n• Ubuntu Tutorials: https://ubuntu.com/tutorials\n• Linux Foundation: https://linuxfoundation.org\n\n📝 **Exercise:** Research and choose a Linux distribution to try.',
             'order': 1, 'duration': 30, 'free': True},
            
            {'title': 'Installing Ubuntu Linux', 
             'content': 'Learn to install Ubuntu Linux. This covers creating a live USB, partitioning for dual-boot, and completing the installation. You\'ll also set up the GNOME desktop environment.\n\n📚 **Resources:**\n• Ubuntu Installation Guide: https://ubuntu.com/tutorials/install-ubuntu-desktop\n\n📝 **Exercise:** Create a Ubuntu live USB and boot from it.',
             'order': 2, 'duration': 45, 'free': False},
            
            {'title': 'Linux Command Line Basics', 
             'content': 'Master essential Linux commands: ls, cd, cp, mv, rm, mkdir, sudo, apt, and more. You\'ll navigate the terminal, manage files, and install software using the command line.\n\n📚 **Resources:**\n• Linux Command Line Tutorial: https://linuxcommand.org\n• Ubuntu CLI Guide\n\n📝 **Exercise:** Practice navigating directories and creating/deleting files from the terminal.',
             'order': 3, 'duration': 35, 'free': False},
            
            {'title': 'Linux File System and Permissions', 
             'content': 'Understand the Linux file system structure (/, /home, /etc, /var). Learn about file permissions (chmod, chown), user management, and the importance of the root directory.\n\n📚 **Resources:**\n• Linux File System: https://tldp.org/LDP/intro-linux\n\n📝 **Exercise:** Change file permissions and create a new user account.',
             'order': 4, 'duration': 40, 'free': False},
            
            {'title': 'Linux System Administration', 
             'content': 'Learn to manage Linux systems including user accounts, services (systemd), networking configuration, and basic security. You\'ll also learn about cron jobs and system monitoring.\n\n📚 **Resources:**\n• Linux Administration Guide\n\n📝 **Exercise:** Start and stop a service and schedule a simple cron job.',
             'order': 5, 'duration': 45, 'free': False},
        ]
    },
    
    # ===== OPEN SOURCE GRAPHICS =====
    'gimp': {
        'lessons': [
            {'title': 'Introduction to GIMP - Free Image Editor', 
             'content': 'GIMP (GNU Image Manipulation Program) is a powerful free and open-source image editor. This lesson covers the interface, tools, and basic image editing concepts that can be used for professional work without cost.\n\n📚 **Resources:**\n• GIMP Official Tutorials: https://www.gimp.org/tutorials/\n• GIMP Documentation\n\n📝 **Exercise:** Open GIMP and identify all the tools in the toolbox.',
             'order': 1, 'duration': 30, 'free': True},
            
            {'title': 'Basic Image Editing with GIMP', 
             'content': 'Learn to crop, resize, rotate, and adjust colors. You\'ll also learn about layers, selection tools, and working with different file formats (JPEG, PNG, GIF).\n\n📚 **Resources:**\n• GIMP Quick Reference Guide\n\n📝 **Exercise:** Edit a photo - crop it, adjust colors, and save in different formats.',
             'order': 2, 'duration': 40, 'free': False},
            
            {'title': 'Working with Layers and Selections', 
             'content': 'Master layers and selection tools in GIMP. Learn about layer masks, blending modes, and advanced selection techniques for professional photo editing.\n\n📚 **Resources:**\n• GIMP Layers Tutorial\n\n📝 **Exercise:** Combine two images using layers and create a composite image.',
             'order': 3, 'duration': 45, 'free': False},
            
            {'title': 'Photo Retouching and Restoration', 
             'content': 'Learn professional photo retouching techniques including removing blemishes, restoring old photos, color correction, and skin smoothing.\n\n📚 **Resources:**\n• GIMP Photo Retouching Guide\n\n📝 **Exercise:** Retouch a portrait photo and restore an old photo.',
             'order': 4, 'duration': 50, 'free': False},
            
            {'title': 'Creating Graphics for Web and Print', 
             'content': 'Learn to create graphics for web design, social media, and print. Includes designing banners, social media posts, and understanding resolution and DPI.\n\n📚 **Resources:**\n• GIMP Web Design Tutorials\n\n📝 **Exercise:** Create a social media graphic and a business card design.',
             'order': 5, 'duration': 45, 'free': False},
            
            {'title': 'GIMP Advanced Techniques', 
             'content': 'Master advanced GIMP techniques including filters, effects, text tools, and creating professional designs. Learn about paths, text effects, and advanced color manipulation.\n\n📚 **Resources:**\n• Advanced GIMP Tutorials\n\n📝 **Exercise:** Create a professional logo design and apply advanced effects.',
             'order': 6, 'duration': 50, 'free': False},
        ]
    },
    
    'inkscape': {
        'lessons': [
            {'title': 'Introduction to Inkscape - Vector Graphics', 
             'content': 'Inkscape is a free and open-source vector graphics editor. This lesson covers vector graphics concepts, the Inkscape interface, and basic tools for creating scalable designs.\n\n📚 **Resources:**\n• Inkscape Tutorials: https://inkscape.org/learn/\n\n📝 **Exercise:** Open Inkscape and experiment with basic shapes and tools.',
             'order': 1, 'duration': 30, 'free': True},
            
            {'title': 'Basic Vector Design and Shapes', 
             'content': 'Learn to create shapes, paths, and basic vector illustrations. Understand fills, strokes, gradients, and working with text in vector designs.\n\n📚 **Resources:**\n• Inkscape Basic Tutorials\n\n📝 **Exercise:** Create a simple vector illustration using basic shapes.',
             'order': 2, 'duration': 40, 'free': False},
            
            {'title': 'Logo Design with Inkscape', 
             'content': 'Learn professional logo design techniques. Create scalable vector logos for businesses and brands using Inkscape\'s powerful tools.\n\n📚 **Resources:**\n• Logo Design Tutorials: https://logosbynick.com/inkscape/\n\n📝 **Exercise:** Design a logo for a fictional business.',
             'order': 3, 'duration': 45, 'free': False},
            
            {'title': 'Advanced Inkscape Techniques', 
             'content': 'Master advanced features including layers, filters, cloning, and tracing bitmaps. Learn to create complex vector illustrations and designs.\n\n📚 **Resources:**\n• Advanced Inkscape Tutorials\n\n📝 **Exercise:** Create a complex vector illustration with multiple elements.',
             'order': 4, 'duration': 50, 'free': False},
            
            {'title': 'Creating Icons and Illustrations', 
             'content': 'Learn to create professional icons and illustrations. Understand icon design principles and create a complete icon set.\n\n📚 **Resources:**\n• Icon Design with Inkscape\n\n📝 **Exercise:** Create a set of 5 icons for a mobile app.',
             'order': 5, 'duration': 45, 'free': False},
        ]
    },
    
    # ===== PHOTOGRAPHY =====
    'photography': {
        'lessons': [
            {'title': 'Digital Photography Fundamentals', 
             'content': 'Learn the basics of digital photography. This includes camera types, understanding the exposure triangle (aperture, shutter speed, ISO), and composition techniques.\n\n📚 **Resources:**\n• Digital Photography School: https://digital-photography-school.com\n• National Geographic Photography: https://www.nationalgeographic.com/photography/\n\n📝 **Exercise:** Practice taking photos with different exposure settings.',
             'order': 1, 'duration': 35, 'free': True},
            
            {'title': 'Smartphone Photography Mastery', 
             'content': 'Master mobile photography techniques. Learn to use your phone camera effectively, composition tips, and editing apps for professional-looking photos.\n\n📚 **Resources:**\n• Smartphone Photography Tips: https://www.photographytalk.com/smartphone-photography-tips\n\n📝 **Exercise:** Take a series of photos using only your smartphone with different composition techniques.',
             'order': 2, 'duration': 30, 'free': False},
            
            {'title': 'Lighting and Composition', 
             'content': 'Understand light and composition for stunning photos. Learn about natural light, artificial light, rule of thirds, leading lines, and framing techniques.\n\n📚 **Resources:**\n• National Geographic Photography Guide\n\n📝 **Exercise:** Practice using the rule of thirds and leading lines in your photos.',
             'order': 3, 'duration': 40, 'free': False},
            
            {'title': 'Photo Editing with GIMP', 
             'content': 'Learn to edit your photos using GIMP. Topics include color correction, retouching, creative effects, and preparing images for social media and print.\n\n📚 **Resources:**\n• GIMP Photo Editing Tutorials\n\n📝 **Exercise:** Edit a set of photos using different editing techniques.',
             'order': 4, 'duration': 45, 'free': False},
            
            {'title': 'Building a Photography Portfolio', 
             'content': 'Learn to create a professional photography portfolio. Understand how to select and present your best work, and how to find clients and opportunities.\n\n📚 **Resources:**\n• Photography Business Tips\n\n📝 **Exercise:** Create a portfolio of your best 10 photos.',
             'order': 5, 'duration': 40, 'free': False},
        ]
    },
    
    # ===== VIDEOGRAPHY =====
    'videography': {
        'lessons': [
            {'title': 'Video Production Fundamentals', 
             'content': 'Learn the basics of video production including equipment, shooting techniques, and pre-production planning. Understand storyboarding and scriptwriting.\n\n📚 **Resources:**\n• Video Production Guide\n\n📝 **Exercise:** Create a storyboard for a short video project.',
             'order': 1, 'duration': 35, 'free': True},
            
            {'title': 'Filming Techniques and Equipment', 
             'content': 'Master filming techniques including shot types, camera movement, framing, and storytelling through video. Learn about different equipment options for different budgets.\n\n📚 **Resources:**\n• Filmmaking Techniques Guide\n\n📝 **Exercise:** Film a short scene using different shot types.',
             'order': 2, 'duration': 45, 'free': False},
            
            {'title': 'Audio Recording and Production', 
             'content': 'Learn to capture and edit high-quality audio. Topics include microphones, recording techniques, and audio editing with Audacity.\n\n📚 **Resources:**\n• Audacity Tutorials: https://www.audacityteam.org/tutorials/\n\n📝 **Exercise:** Record and edit a voiceover using Audacity.',
             'order': 3, 'duration': 40, 'free': False},
            
            {'title': 'Video Editing with OpenShot/Kdenlive', 
             'content': 'Learn professional video editing using free open-source tools. Topics include timeline editing, transitions, effects, and color grading.\n\n📚 **Resources:**\n• OpenShot Tutorials: https://www.openshot.org\n• Kdenlive Documentation\n\n📝 **Exercise:** Edit a short video with transitions and effects.',
             'order': 4, 'duration': 50, 'free': False},
            
            {'title': 'Video Production Projects', 
             'content': 'Complete video production projects. Create promotional videos, tutorials, documentaries, and social media content.\n\n📚 **Resources:**\n• Video Production Case Studies\n\n📝 **Exercise:** Create a 2-minute promotional video for a product or service.',
             'order': 5, 'duration': 55, 'free': False},
        ]
    },
    
    # ===== WEB DEVELOPMENT =====
    'web': {
        'lessons': [
            {'title': 'HTML Fundamentals - Building Web Pages', 
             'content': 'Learn the basics of HTML - the structure of web pages. Understand tags, elements, attributes, and how to build a simple web page structure.\n\n📚 **Resources:**\n• MDN HTML Guide: https://developer.mozilla.org/en-US/docs/Web/HTML\n• W3Schools HTML Tutorial: https://www.w3schools.com/html/\n\n📝 **Exercise:** Create a simple HTML page with headings, paragraphs, and images.',
             'order': 1, 'duration': 35, 'free': True},
            
            {'title': 'CSS Styling and Design', 
             'content': 'Learn CSS for styling web pages. Understand selectors, properties, layouts, and responsive design principles. Create beautiful, professional web designs.\n\n📚 **Resources:**\n• MDN CSS Guide: https://developer.mozilla.org/en-US/docs/Web/CSS\n• CSS-Tricks: https://css-tricks.com\n\n📝 **Exercise:** Style your HTML page with CSS including layouts and responsive design.',
             'order': 2, 'duration': 45, 'free': False},
            
            {'title': 'JavaScript Interactivity', 
             'content': 'Learn JavaScript to add interactivity to web pages. Understand variables, functions, events, and DOM manipulation for dynamic content.\n\n📚 **Resources:**\n• JavaScript Guide: https://developer.mozilla.org/en-US/docs/Web/JavaScript\n\n📝 **Exercise:** Add interactive elements to your web page using JavaScript.',
             'order': 3, 'duration': 50, 'free': False},
            
            {'title': 'WordPress Development', 
             'content': 'Learn to build websites with WordPress. Understand installation, themes, plugins, and content management for professional websites.\n\n📚 **Resources:**\n• WordPress Documentation: https://wordpress.org/documentation/\n\n📝 **Exercise:** Install WordPress and create a basic website.',
             'order': 4, 'duration': 45, 'free': False},
            
            {'title': 'Responsive Web Design', 
             'content': 'Learn to create websites that work on all devices. Understand media queries, flexible layouts, and mobile-first design principles.\n\n📚 **Resources:**\n• Responsive Web Design Guide\n\n📝 **Exercise:** Make your website responsive for mobile and desktop devices.',
             'order': 5, 'duration': 40, 'free': False},
        ]
    },
    
    # ===== DIGITAL MARKETING =====
    'digital marketing': {
        'lessons': [
            {'title': 'Digital Marketing Fundamentals', 
             'content': 'Learn the basics of digital marketing including SEO, social media, content marketing, and email marketing. Understand the digital marketing landscape and strategies.\n\n📚 **Resources:**\n• Google Digital Marketing Course\n• HubSpot Academy\n\n📝 **Exercise:** Create a digital marketing plan for a small business.',
             'order': 1, 'duration': 35, 'free': True},
            
            {'title': 'Search Engine Optimization (SEO)', 
             'content': 'Master SEO techniques to improve website visibility. Learn about keyword research, on-page optimization, off-page optimization, and technical SEO.\n\n📚 **Resources:**\n• Google SEO Starter Guide\n• Moz SEO Guide\n\n📝 **Exercise:** Conduct keyword research and optimize a web page for SEO.',
             'order': 2, 'duration': 45, 'free': False},
            
            {'title': 'Social Media Marketing', 
             'content': 'Learn to use social media platforms for business. Understand Facebook, Instagram, LinkedIn, Twitter, and TikTok marketing strategies.\n\n📚 **Resources:**\n• Social Media Marketing Guide\n\n📝 **Exercise:** Create a social media content calendar for a business.',
             'order': 3, 'duration': 40, 'free': False},
            
            {'title': 'Content Marketing', 
             'content': 'Master content marketing including creating valuable content, content strategy, and content distribution across platforms.\n\n📚 **Resources:**\n• Content Marketing Institute\n\n📝 **Exercise:** Create a blog post and develop a content strategy.',
             'order': 4, 'duration': 40, 'free': False},
            
            {'title': 'Email Marketing and Automation', 
             'content': 'Learn email marketing strategies, creating email campaigns, automation, and building email lists for business growth.\n\n📚 **Resources:**\n• Email Marketing Guide\n\n📝 **Exercise:** Create an email marketing campaign and automation sequence.',
             'order': 5, 'duration': 35, 'free': False},
        ]
    },
    
    # ===== BUSINESS & ENTREPRENEURSHIP =====
    'business': {
        'lessons': [
            {'title': 'Introduction to Entrepreneurship', 
             'content': 'Learn the fundamentals of entrepreneurship. Understand what it takes to start a business, identify opportunities, and develop an entrepreneurial mindset.\n\n📚 **Resources:**\n• Entrepreneurship Guide\n• Business Model Canvas\n\n📝 **Exercise:** Identify a business opportunity and create a business model canvas.',
             'order': 1, 'duration': 35, 'free': True},
            
            {'title': 'Business Planning and Strategy', 
             'content': 'Learn to create a comprehensive business plan. Cover all aspects including market analysis, financial planning, marketing strategy, and operations.\n\n📚 **Resources:**\n• Business Plan Guide\n\n📝 **Exercise:** Write a business plan for your business idea.',
             'order': 2, 'duration': 50, 'free': False},
            
            {'title': 'Financial Management for Entrepreneurs', 
             'content': 'Learn to manage business finances including budgeting, cash flow management, and basic accounting. Understand financial statements and business metrics.\n\n📚 **Resources:**\n• Small Business Finance Guide\n\n📝 **Exercise:** Create a budget and cash flow projection for your business.',
             'order': 3, 'duration': 45, 'free': False},
            
            {'title': 'Marketing and Sales for Small Business', 
             'content': 'Learn to market and sell your products or services. Cover marketing strategies, sales techniques, and building customer relationships.\n\n📚 **Resources:**\n• Small Business Marketing Guide\n\n📝 **Exercise:** Create a marketing plan and sales pitch for your business.',
             'order': 4, 'duration': 40, 'free': False},
            
            {'title': 'Business Growth and Scaling', 
             'content': 'Learn strategies for growing your business. Cover scaling operations, team building, and expansion strategies for sustainable growth.\n\n📚 **Resources:**\n• Business Growth Strategies\n\n📝 **Exercise:** Develop a growth plan for your business for the next 12 months.',
             'order': 5, 'duration': 45, 'free': False},
        ]
    },
}

# Add lessons to courses
total_lessons_added = 0
course_count = 0

for course in Course.objects.filter(is_active=True):
    # Check which template matches
    matched_template = None
    course_title_lower = course.title.lower()
    
    for template_key, template_data in lesson_templates.items():
        if template_key in course_title_lower:
            matched_template = template_data
            break
    
    if matched_template:
        print(f"\n📖 Adding lessons to: {course.title}")
        for lesson_data in matched_template['lessons']:
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
                total_lessons_added += 1
                print(f"  ✅ Added: {lesson.title}")
        course_count += 1
    else:
        # For courses without specific template, add generic content
        if course.lessons.count() == 0:
            print(f"\n📖 Adding generic lessons to: {course.title}")
            generic_lessons = [
                {'title': f'Introduction to {course.title}', 
                 'content': f'Welcome to {course.title}. This comprehensive course will help you develop essential skills in this field. You\'ll learn from practical examples and hands-on exercises.', 
                 'order': 1, 'duration': 30, 'free': True},
                {'title': f'Core Concepts of {course.title}', 
                 'content': f'Learn the fundamental concepts and principles of {course.title}. Understand the key theories and practical applications that form the foundation of this field.', 
                 'order': 2, 'duration': 35, 'free': False},
                {'title': 'Practical Applications', 
                 'content': 'Apply what you\'ve learned to real-world situations. This lesson covers practical examples and hands-on exercises to reinforce your learning.', 
                 'order': 3, 'duration': 40, 'free': False},
                {'title': 'Advanced Techniques and Tools', 
                 'content': 'Explore advanced techniques and tools in this field. Learn professional practices and discover resources for further development.', 
                 'order': 4, 'duration': 40, 'free': False},
                {'title': 'Project and Portfolio Development', 
                 'content': 'Create a project or portfolio that showcases your skills. This practical exercise will help you demonstrate your knowledge and abilities.', 
                 'order': 5, 'duration': 45, 'free': False},
                {'title': 'Next Steps and Career Pathways', 
                 'content': 'Plan your continued learning and career development. Explore opportunities, certifications, and pathways for professional growth.', 
                 'order': 6, 'duration': 30, 'free': False},
            ]
            for lesson_data in generic_lessons:
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
                    total_lessons_added += 1
                    print(f"  ✅ Added: {lesson.title}")
            course_count += 1

print("\n" + "="*60)
print(f"📊 Courses Updated: {course_count}")
print(f"📊 Total Lessons Added: {total_lessons_added}")
print(f"📚 Total Lessons in Database: {Lesson.objects.count()}")

# Show summary by approach
print("\n📊 Courses with Lessons by Learning Approach:")
for approach in ['pedagogic', 'andragogic', 'heutagogic', 'cybergogic']:
    courses_with_lessons = Course.objects.filter(learning_approach=approach, is_active=True).filter(lessons__isnull=False).distinct().count()
    print(f"  📖 {approach.upper()}: {courses_with_lessons} courses have lessons")

print("\n🎉 Detailed lesson content addition complete!")