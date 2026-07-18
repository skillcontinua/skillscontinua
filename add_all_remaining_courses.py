import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from courses.models import Category, Course

print("🚀 Adding COMPLETE COURSE CATALOG to SkillsContinua...")
print("="*60)

# Get all categories
categories = {}
for cat in Category.objects.all():
    categories[cat.pillar] = cat
    categories[cat.name.lower()] = cat

print(f"Found {len(categories)} categories")

# Complete course catalog organized by category
complete_catalog = [
    # ===== BASIC COMPUTING & OPERATING SYSTEMS =====
    {
        'title': 'Windows Operating System Fundamentals',
        'category': 'computer',
        'description': 'Complete Windows OS training - installation, configuration, file management, system settings, and troubleshooting.',
        'level': 'beginner', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 25,
        'objectives': 'Master Windows OS operations and system management'
    },
    {
        'title': 'Windows Advanced Administration',
        'category': 'computer',
        'description': 'Advanced Windows administration - group policies, Active Directory, PowerShell, and enterprise management.',
        'level': 'advanced', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 30,
        'objectives': 'Master advanced Windows system administration'
    },
    {
        'title': 'macOS Fundamentals',
        'category': 'computer',
        'description': 'Complete macOS training - navigation, productivity tools, system preferences, and professional applications.',
        'level': 'beginner', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 20,
        'objectives': 'Master macOS operations and productivity tools'
    },
    {
        'title': 'Linux Essentials',
        'category': 'computer',
        'description': 'Linux fundamentals - distributions, command line, file system, user management, and basic system administration.',
        'level': 'beginner', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 25,
        'objectives': 'Master Linux fundamentals and command-line operations'
    },
    {
        'title': 'Linux System Administration',
        'category': 'computer',
        'description': 'Advanced Linux administration - server management, networking, security, and system optimization.',
        'level': 'advanced', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 30,
        'objectives': 'Master Linux system administration and server management'
    },
    {
        'title': 'Linux Command Line and Shell Scripting',
        'category': 'computer',
        'description': 'Advanced Linux command-line operations - BASH scripting, automation, and system administration tasks.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 25,
        'objectives': 'Master Linux command-line and BASH scripting'
    },
    
    # ===== MICROSOFT OFFICE & PRODUCTIVITY =====
    {
        'title': 'Microsoft Word - Document Mastery',
        'category': 'computer',
        'description': 'Professional document creation with Microsoft Word - formatting, templates, mail merge, and advanced features.',
        'level': 'beginner', 'age_group': 'adult', 'approach': 'andragogic', 'duration': 20,
        'objectives': 'Master Microsoft Word for professional document creation'
    },
    {
        'title': 'Microsoft Excel - Data Analysis',
        'category': 'computer',
        'description': 'Professional spreadsheet skills - formulas, functions, data analysis, charts, and macros in Excel.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 25,
        'objectives': 'Master Excel for data analysis and reporting'
    },
    {
        'title': 'Microsoft PowerPoint - Presentations',
        'category': 'computer',
        'description': 'Professional presentation design - animations, transitions, design principles, and delivery techniques.',
        'level': 'beginner', 'age_group': 'adult', 'approach': 'andragogic', 'duration': 15,
        'objectives': 'Master PowerPoint for professional presentations'
    },
    {
        'title': 'Microsoft Outlook and Email Management',
        'category': 'computer',
        'description': 'Professional email management - Outlook features, calendar management, contacts, and productivity tools.',
        'level': 'beginner', 'age_group': 'adult', 'approach': 'andragogic', 'duration': 15,
        'objectives': 'Master Outlook for professional communication'
    },
    {
        'title': 'Google Workspace Complete',
        'category': 'digital',
        'description': 'Google Workspace tools - Gmail, Docs, Sheets, Slides, Drive, Calendar, and collaborative workflows.',
        'level': 'beginner', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 20,
        'objectives': 'Master Google Workspace for collaborative work'
    },
    {
        'title': 'LibreOffice - Open Source Office Suite',
        'category': 'computer',
        'description': 'Complete LibreOffice training - Writer, Calc, Impress, and professional open-source productivity.',
        'level': 'beginner', 'age_group': 'adult', 'approach': 'andragogic', 'duration': 20,
        'objectives': 'Master LibreOffice for professional productivity'
    },
    
    # ===== INTERNET & DIGITAL SKILLS =====
    {
        'title': 'Internet Fundamentals and Research',
        'category': 'digital',
        'description': 'Internet basics - browsing, searching, online safety, digital research skills, and evaluating information.',
        'level': 'beginner', 'age_group': 'all', 'approach': 'andragogic', 'duration': 15,
        'objectives': 'Master internet fundamentals and research skills'
    },
    {
        'title': 'Social Media Management Professional',
        'category': 'digital',
        'description': 'Professional social media management - Facebook, Twitter, LinkedIn, Instagram, content strategy, and analytics.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 25,
        'objectives': 'Master professional social media management'
    },
    {
        'title': 'Digital Citizenship and Online Safety',
        'category': 'digital',
        'description': 'Digital citizenship - online safety, privacy protection, digital footprint, and responsible online behavior.',
        'level': 'beginner', 'age_group': 'all', 'approach': 'andragogic', 'duration': 12,
        'objectives': 'Master digital citizenship and online safety'
    },
    {
        'title': 'E-Commerce and Online Business',
        'category': 'digital',
        'description': 'E-commerce fundamentals - online stores, payment systems, digital marketing, and e-commerce management.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 25,
        'objectives': 'Master e-commerce and online business operations'
    },
    
    # ===== OPEN SOURCE GRAPHICS & DESIGN =====
    {
        'title': 'GIMP - Image Editing Fundamentals',
        'category': 'computer',
        'description': 'GIMP (GNU Image Manipulation Program) - image editing, photo retouching, and graphic design with open-source tools.',
        'level': 'beginner', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 20,
        'objectives': 'Master GIMP for professional image editing'
    },
    {
        'title': 'GIMP - Advanced Photo Manipulation',
        'category': 'computer',
        'description': 'Advanced GIMP techniques - masks, filters, layers, compositing, and professional photo editing.',
        'level': 'advanced', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 25,
        'objectives': 'Master advanced GIMP for professional design'
    },
    {
        'title': 'Inkscape - Vector Graphics Design',
        'category': 'computer',
        'description': 'Inkscape - vector graphics, logo design, illustrations, and professional design with open-source tools.',
        'level': 'beginner', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 20,
        'objectives': 'Master Inkscape for professional vector design'
    },
    {
        'title': 'Inkscape - Logo and Illustration Mastery',
        'category': 'computer',
        'description': 'Advanced Inkscape - logo design, complex illustrations, and professional vector art creation.',
        'level': 'advanced', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 25,
        'objectives': 'Master advanced Inkscape for professional illustration'
    },
    {
        'title': 'Blender - 3D Modeling and Animation',
        'category': 'computer',
        'description': 'Blender - 3D modeling, animation, rendering, and professional 3D design with open-source tools.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 30,
        'objectives': 'Master Blender for 3D design and animation'
    },
    {
        'title': 'Scribus - Desktop Publishing',
        'category': 'computer',
        'description': 'Scribus - professional desktop publishing, layout design, brochures, and print-ready documents with open-source tools.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 20,
        'objectives': 'Master Scribus for professional publishing'
    },
    
    # ===== PHOTOGRAPHY & VIDEOGRAPHY =====
    {
        'title': 'Digital Photography Fundamentals',
        'category': 'vocational',
        'description': 'Digital photography - camera types, exposure triangle, composition, lighting, and professional photography techniques.',
        'level': 'beginner', 'age_group': 'adult', 'approach': 'andragogic', 'duration': 20,
        'objectives': 'Master digital photography fundamentals'
    },
    {
        'title': 'Smartphone Photography and Mobile Editing',
        'category': 'vocational',
        'description': 'Mobile photography - smartphone cameras, editing apps, social media content, and professional mobile photography.',
        'level': 'beginner', 'age_group': 'adult', 'approach': 'andragogic', 'duration': 15,
        'objectives': 'Master smartphone photography and mobile editing'
    },
    {
        'title': 'Video Production and Filming Techniques',
        'category': 'vocational',
        'description': 'Video production - filming techniques, shot composition, equipment, and professional video production.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'andragogic', 'duration': 25,
        'objectives': 'Master video production and filming techniques'
    },
    {
        'title': 'OpenShot Video Editing',
        'category': 'vocational',
        'description': 'OpenShot - professional video editing with open-source tools, transitions, effects, and production workflows.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 20,
        'objectives': 'Master OpenShot for professional video editing'
    },
    {
        'title': 'Kdenlive Video Editing Professional',
        'category': 'vocational',
        'description': 'Kdenlive - advanced video editing with open-source tools, color grading, effects, and professional production.',
        'level': 'advanced', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 25,
        'objectives': 'Master Kdenlive for professional video production'
    },
    {
        'title': 'Audacity - Audio Production',
        'category': 'vocational',
        'description': 'Audacity - audio recording, editing, mixing, and professional audio production with open-source tools.',
        'level': 'beginner', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 15,
        'objectives': 'Master Audacity for professional audio production'
    },
    
    # ===== WEB DEVELOPMENT & PROGRAMMING =====
    {
        'title': 'HTML and CSS Fundamentals',
        'category': 'computer',
        'description': 'Web development basics - HTML structure, CSS styling, responsive design, and modern web standards.',
        'level': 'beginner', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 25,
        'objectives': 'Master HTML and CSS for web development'
    },
    {
        'title': 'JavaScript Essentials',
        'category': 'computer',
        'description': 'JavaScript programming - DOM manipulation, events, ES6+, and interactive web development.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 30,
        'objectives': 'Master JavaScript for interactive web development'
    },
    {
        'title': 'Python Programming Fundamentals',
        'category': 'computer',
        'description': 'Python programming - syntax, data structures, functions, and practical Python applications.',
        'level': 'beginner', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 30,
        'objectives': 'Master Python programming fundamentals'
    },
    {
        'title': 'WordPress Development and Management',
        'category': 'digital',
        'description': 'WordPress - installation, themes, plugins, content management, and professional website development.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 25,
        'objectives': 'Master WordPress for professional website development'
    },
    {
        'title': 'E-Commerce Development',
        'category': 'digital',
        'description': 'E-commerce development - online stores, payment gateways, shopping carts, and secure e-commerce platforms.',
        'level': 'advanced', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 30,
        'objectives': 'Master e-commerce website development'
    },
    
    # ===== ADVANCED TECHNOLOGY =====
    {
        'title': 'Artificial Intelligence and ChatGPT Essentials',
        'category': 'computer',
        'description': 'AI fundamentals - ChatGPT, prompt engineering, AI tools, and practical AI applications for productivity.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 20,
        'objectives': 'Master AI and ChatGPT for professional productivity'
    },
    {
        'title': 'Cloud Computing Fundamentals',
        'category': 'computer',
        'description': 'Cloud computing - AWS, Google Cloud, Azure, cloud architecture, and cloud services deployment.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 25,
        'objectives': 'Master cloud computing fundamentals and services'
    },
    {
        'title': 'Cybersecurity Professional',
        'category': 'computer',
        'description': 'Comprehensive cybersecurity - network security, threat detection, risk management, and security protocols.',
        'level': 'advanced', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 30,
        'objectives': 'Master professional cybersecurity practices'
    },
    {
        'title': 'Internet of Things (IoT) Fundamentals',
        'category': 'computer',
        'description': 'IoT - smart devices, sensors, connectivity, and IoT application development.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 20,
        'objectives': 'Master IoT fundamentals and applications'
    },
    {
        'title': 'Drone Technology and Operations',
        'category': 'technology',
        'description': 'Drone technology - operations, regulations, aerial photography, and drone maintenance.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 20,
        'objectives': 'Master drone operations and technology'
    },
    {
        'title': 'Robotics and Automation',
        'category': 'technology',
        'description': 'Robotics - design, programming, sensors, actuators, and automation systems.',
        'level': 'advanced', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 25,
        'objectives': 'Master robotics and automation systems'
    },
    
    # ===== CREATIVE ARTS & MEDIA =====
    {
        'title': 'Digital Art and Animation',
        'category': 'vocational',
        'description': 'Digital art - 2D/3D art, animation techniques, and creative digital media production.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'andragogic', 'duration': 25,
        'objectives': 'Master digital art and animation creation'
    },
    {
        'title': 'Music Production with Open-Source Tools',
        'category': 'vocational',
        'description': 'Music production - digital audio workstations, composition, and professional music creation with free tools.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 25,
        'objectives': 'Master music production with open-source tools'
    },
    {
        'title': 'Podcast Production and Publishing',
        'category': 'vocational',
        'description': 'Podcast production - recording, editing, publishing, and professional podcast creation.',
        'level': 'beginner', 'age_group': 'adult', 'approach': 'andragogic', 'duration': 15,
        'objectives': 'Master podcast production and publishing'
    },
    {
        'title': 'Content Creation for Social Media',
        'category': 'digital',
        'description': 'Content creation - YouTube, TikTok, Instagram, and professional social media content strategy.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 20,
        'objectives': 'Master content creation for social media'
    },
    
    # ===== BUSINESS & ENTREPRENEURSHIP =====
    {
        'title': 'Small Business Management',
        'category': 'financial',
        'description': 'Small business management - business planning, operations, marketing, and business growth strategies.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'heutagogic', 'duration': 25,
        'objectives': 'Master small business management and growth'
    },
    {
        'title': 'Freelancing and Gig Economy',
        'category': 'financial',
        'description': 'Freelancing - finding work, managing clients, pricing, and building a successful freelance career.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'heutagogic', 'duration': 20,
        'objectives': 'Master freelancing and gig economy success'
    },
    {
        'title': 'Digital Marketing Strategy',
        'category': 'digital',
        'description': 'Digital marketing strategy - SEO, content marketing, email marketing, and comprehensive marketing planning.',
        'level': 'advanced', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 25,
        'objectives': 'Master digital marketing strategy and planning'
    },
    {
        'title': 'E-Commerce Business Management',
        'category': 'digital',
        'description': 'E-commerce business - store management, customer service, logistics, and e-commerce operations.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'heutagogic', 'duration': 20,
        'objectives': 'Master e-commerce business management'
    },
]

# Add all courses
total_added = 0
for course_data in complete_catalog:
    # Try to find category
    category = None
    
    # First try by pillar
    if course_data['category'] in categories:
        category = categories[course_data['category']]
    else:
        # Try to find by name matching
        for cat in Category.objects.all():
            if course_data['category'].lower() in cat.name.lower():
                category = cat
                break
    
    if category:
        course, created = Course.objects.get_or_create(
            title=course_data['title'],
            category=category,
            defaults={
                'description': course_data['description'],
                'level': course_data['level'],
                'age_group': course_data['age_group'],
                'learning_approach': course_data['approach'],
                'duration_hours': course_data['duration'],
                'learning_objectives': course_data.get('objectives', ''),
                'is_active': True,
                'featured': True,
            }
        )
        if created:
            total_added += 1
            print(f"✅ Added: {course.title} ({course_data['approach'].upper()})")
        else:
            print(f"📚 Already exists: {course.title}")
    else:
        print(f"⚠️ Category '{course_data['category']}' not found - skipping")

print("\n" + "="*60)
print(f"📊 Total New Courses Added: {total_added}")
print(f"📚 Total Courses in Database: {Course.objects.filter(is_active=True).count()}")

# Summary by approach
print("\n📊 Summary by Learning Approach:")
for approach in ['pedagogic', 'andragogic', 'heutagogic', 'cybergogic']:
    count = Course.objects.filter(learning_approach=approach, is_active=True).count()
    print(f"  📖 {approach.upper()}: {count} courses")

print("\n🎉 Complete course catalog addition complete!")