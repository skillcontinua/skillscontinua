import os
import sys
import django

# Add project root to path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from courses.models import Category, Course

print("="*70)
print("🌍 ADDING ALL MISSING COURSES TO SKILLSCONTINUA")
print("="*70)

# Get all categories
categories = {}
for cat in Category.objects.all():
    categories[cat.pillar] = cat
    categories[cat.name.lower()] = cat

print(f"Found {len(categories)} categories")

# ============================================================
# SECTION 1: BASIC COMPUTING & OPERATING SYSTEMS
# ============================================================
print("\n" + "="*70)
print("📱 SECTION 1: BASIC COMPUTING & OPERATING SYSTEMS")
print("="*70)

basic_computing_courses = [
    {
        'title': 'Windows OS Complete - Installation and Configuration',
        'category': 'computer',
        'description': 'Complete Windows operating system training - installation, configuration, system settings, file management, troubleshooting, and optimization.',
        'level': 'beginner', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 30,
        'objectives': 'Master Windows OS from installation to advanced configuration'
    },
    {
        'title': 'Windows Advanced Administration and Security',
        'category': 'computer',
        'description': 'Advanced Windows administration - group policies, Active Directory, PowerShell scripting, security hardening, and enterprise management.',
        'level': 'advanced', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 35,
        'objectives': 'Master advanced Windows system administration and security'
    },
    {
        'title': 'macOS Fundamentals - Complete Guide',
        'category': 'computer',
        'description': 'Complete macOS training - navigation, productivity tools, system preferences, professional applications, and workflow optimization.',
        'level': 'beginner', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 25,
        'objectives': 'Master macOS operations and professional productivity'
    },
    {
        'title': 'Linux for Beginners - Ubuntu and Beyond',
        'category': 'computer',
        'description': 'Linux fundamentals - Ubuntu distribution, command line basics, file system, user management, software installation, and open-source ecosystem.',
        'level': 'beginner', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 25,
        'objectives': 'Master Linux fundamentals and open-source computing'
    },
    {
        'title': 'Linux System Administration Professional',
        'category': 'computer',
        'description': 'Professional Linux administration - server management, networking, security, system optimization, and enterprise Linux environments.',
        'level': 'advanced', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 35,
        'objectives': 'Master professional Linux system administration'
    },
    {
        'title': 'Linux Command Line and Shell Scripting',
        'category': 'computer',
        'description': 'Advanced Linux command-line operations - BASH scripting, automation, system tasks, and professional Linux administration techniques.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 25,
        'objectives': 'Master Linux command line and BASH scripting'
    },
    {
        'title': 'Chrome OS and Cloud Computing Basics',
        'category': 'computer',
        'description': 'Chrome OS fundamentals - cloud computing, Chromebook operations, Google services integration, and cloud-based workflow management.',
        'level': 'beginner', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 15,
        'objectives': 'Master Chrome OS and cloud computing basics'
    },
]

# ============================================================
# SECTION 2: OFFICE & PRODUCTIVITY SOFTWARE
# ============================================================
print("\n" + "="*70)
print("📝 SECTION 2: OFFICE & PRODUCTIVITY SOFTWARE")
print("="*70)

office_courses = [
    {
        'title': 'Microsoft Word - Professional Document Mastery',
        'category': 'computer',
        'description': 'Professional document creation with Microsoft Word - formatting, templates, mail merge, styles, tables, and advanced document features.',
        'level': 'beginner', 'age_group': 'adult', 'approach': 'andragogic', 'duration': 20,
        'objectives': 'Master Microsoft Word for professional document creation'
    },
    {
        'title': 'Microsoft Excel - Advanced Data Analysis',
        'category': 'computer',
        'description': 'Professional spreadsheet skills - formulas, functions, data analysis, charts, PivotTables, macros, and business intelligence in Excel.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 30,
        'objectives': 'Master Excel for advanced data analysis and reporting'
    },
    {
        'title': 'Microsoft PowerPoint - Professional Presentations',
        'category': 'computer',
        'description': 'Professional presentation design - animations, transitions, design principles, storytelling, and delivery techniques in PowerPoint.',
        'level': 'beginner', 'age_group': 'adult', 'approach': 'andragogic', 'duration': 15,
        'objectives': 'Master PowerPoint for professional presentations'
    },
    {
        'title': 'Google Workspace Complete - Cloud Productivity',
        'category': 'digital',
        'description': 'Complete Google Workspace - Gmail, Docs, Sheets, Slides, Drive, Calendar, Meet, and collaborative cloud productivity tools.',
        'level': 'beginner', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 20,
        'objectives': 'Master Google Workspace for cloud-based productivity'
    },
    {
        'title': 'LibreOffice - Open Source Office Suite',
        'category': 'computer',
        'description': 'Complete LibreOffice training - Writer (word processing), Calc (spreadsheets), Impress (presentations), and professional open-source productivity.',
        'level': 'beginner', 'age_group': 'adult', 'approach': 'andragogic', 'duration': 20,
        'objectives': 'Master LibreOffice for professional productivity'
    },
    {
        'title': 'Microsoft Outlook and Professional Email Management',
        'category': 'computer',
        'description': 'Professional email management - Outlook features, calendar management, contacts, tasks, and productivity tools for professional communication.',
        'level': 'beginner', 'age_group': 'adult', 'approach': 'andragogic', 'duration': 15,
        'objectives': 'Master Outlook for professional communication and productivity'
    },
]

# ============================================================
# SECTION 3: GRAPHICS, PHOTOGRAPHY, AUDIO & VIDEO
# ============================================================
print("\n" + "="*70)
print("🎨 SECTION 3: GRAPHICS, PHOTOGRAPHY, AUDIO & VIDEO")
print("="*70)

media_courses = [
    {
        'title': 'GIMP - Professional Image Editing (Open Source)',
        'category': 'computer',
        'description': 'Complete GIMP training - image editing, photo retouching, graphic design, layers, masks, and professional design with open-source tools.',
        'level': 'beginner', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 25,
        'objectives': 'Master GIMP for professional image editing and design'
    },
    {
        'title': 'GIMP - Advanced Photo Manipulation and Design',
        'category': 'computer',
        'description': 'Advanced GIMP techniques - photo manipulation, compositing, advanced masking, filters, and professional graphic design workflows.',
        'level': 'advanced', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 25,
        'objectives': 'Master advanced GIMP techniques for professional design'
    },
    {
        'title': 'Inkscape - Vector Graphics Design (Open Source)',
        'category': 'computer',
        'description': 'Complete Inkscape training - vector graphics, logo design, illustrations, icons, and professional design with open-source tools.',
        'level': 'beginner', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 20,
        'objectives': 'Master Inkscape for professional vector design'
    },
    {
        'title': 'Inkscape - Logo and Illustration Mastery',
        'category': 'computer',
        'description': 'Advanced Inkscape - logo design, complex illustrations, branding, and professional vector art creation with open-source tools.',
        'level': 'advanced', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 25,
        'objectives': 'Master advanced Inkscape for professional illustration'
    },
    {
        'title': 'Blender - 3D Modeling and Animation (Open Source)',
        'category': 'computer',
        'description': 'Complete Blender training - 3D modeling, animation, rendering, texturing, and professional 3D design with open-source tools.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 35,
        'objectives': 'Master Blender for 3D design and animation'
    },
    {
        'title': 'Scribus - Desktop Publishing (Open Source)',
        'category': 'computer',
        'description': 'Professional desktop publishing with Scribus - layout design, brochures, magazines, books, and print-ready documents with open-source tools.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 20,
        'objectives': 'Master Scribus for professional desktop publishing'
    },
    {
        'title': 'Digital Photography Fundamentals',
        'category': 'vocational',
        'description': 'Complete digital photography - camera types, exposure triangle, composition, lighting, and professional photography techniques.',
        'level': 'beginner', 'age_group': 'adult', 'approach': 'andragogic', 'duration': 20,
        'objectives': 'Master digital photography fundamentals'
    },
    {
        'title': 'Smartphone Photography and Mobile Editing',
        'category': 'vocational',
        'description': 'Mobile photography mastery - smartphone cameras, composition, mobile editing apps, social media content, and professional mobile photography.',
        'level': 'beginner', 'age_group': 'adult', 'approach': 'andragogic', 'duration': 15,
        'objectives': 'Master smartphone photography and mobile editing'
    },
    {
        'title': 'Video Production and Filming Techniques',
        'category': 'vocational',
        'description': 'Professional video production - filming techniques, shot composition, camera operation, lighting, and storytelling.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'andragogic', 'duration': 25,
        'objectives': 'Master video production and filming techniques'
    },
    {
        'title': 'OpenShot Video Editing (Open Source)',
        'category': 'vocational',
        'description': 'Professional video editing with OpenShot - timeline editing, transitions, effects, and video production with open-source tools.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 20,
        'objectives': 'Master OpenShot for professional video editing'
    },
    {
        'title': 'Kdenlive - Advanced Video Editing (Open Source)',
        'category': 'vocational',
        'description': 'Advanced video editing with Kdenlive - color grading, advanced effects, professional workflows, and production with open-source tools.',
        'level': 'advanced', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 25,
        'objectives': 'Master Kdenlive for professional video production'
    },
    {
        'title': 'Audacity - Audio Production (Open Source)',
        'category': 'vocational',
        'description': 'Professional audio production with Audacity - recording, editing, mixing, effects, and audio engineering with open-source tools.',
        'level': 'beginner', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 15,
        'objectives': 'Master Audacity for professional audio production'
    },
]

# ============================================================
# SECTION 4: MUSIC - COMPLETE
# ============================================================
print("\n" + "="*70)
print("🎵 SECTION 4: MUSIC - COMPLETE")
print("="*70)

music_courses = [
    {
        'title': 'Music Theory Fundamentals - Complete Guide',
        'category': 'life_skills',
        'description': 'Complete music theory - notes, scales, chords, rhythm, harmony, and musical notation. Essential knowledge for all musicians.',
        'level': 'beginner', 'age_group': 'all', 'approach': 'pedagogic', 'duration': 25,
        'objectives': 'Master music theory fundamentals for all instruments'
    },
    {
        'title': 'Keyboard and Piano Basics',
        'category': 'life_skills',
        'description': 'Complete piano/keyboard training - technique, music reading, chord progressions, and playing skills for beginners and intermediate learners.',
        'level': 'beginner', 'age_group': 'all', 'approach': 'pedagogic', 'duration': 30,
        'objectives': 'Master keyboard and piano playing fundamentals'
    },
    {
        'title': 'Acoustic Guitar - Complete Beginner to Intermediate',
        'category': 'life_skills',
        'description': 'Complete guitar training - chords, strumming, fingerpicking, music reading, and playing techniques for acoustic guitar.',
        'level': 'beginner', 'age_group': 'all', 'approach': 'pedagogic', 'duration': 30,
        'objectives': 'Master acoustic guitar playing and technique'
    },
    {
        'title': 'African Music and Traditional Instruments',
        'category': 'life_skills',
        'description': 'African music - Djembe, Kora, Mbira, African rhythms, traditional music, and the rich musical heritage of Africa.',
        'level': 'beginner', 'age_group': 'all', 'approach': 'pedagogic', 'duration': 20,
        'objectives': 'Master African music and traditional instruments'
    },
    {
        'title': 'Wind Instruments - Flute, Saxophone, Trumpet',
        'category': 'life_skills',
        'description': 'Complete wind instruments training - flute, saxophone, trumpet, breath control, technique, and music reading.',
        'level': 'beginner', 'age_group': 'all', 'approach': 'pedagogic', 'duration': 25,
        'objectives': 'Master wind instruments and technique'
    },
    {
        'title': 'String Instruments - Violin, Cello, Bass',
        'category': 'life_skills',
        'description': 'Complete string instruments training - violin, cello, bass, technique, bowing, fingering, and orchestral playing.',
        'level': 'beginner', 'age_group': 'all', 'approach': 'pedagogic', 'duration': 25,
        'objectives': 'Master string instruments and technique'
    },
    {
        'title': 'Percussion Instruments - Drums and Rhythm',
        'category': 'life_skills',
        'description': 'Complete percussion training - drum set, hand percussion, rhythm, timing, and world percussion instruments.',
        'level': 'beginner', 'age_group': 'all', 'approach': 'pedagogic', 'duration': 20,
        'objectives': 'Master percussion and rhythm techniques'
    },
    {
        'title': 'Music Production and Digital Audio Workstations',
        'category': 'life_skills',
        'description': 'Professional music production - digital audio workstations, MIDI, recording, mixing, and modern music production techniques.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 30,
        'objectives': 'Master music production and digital audio'
    },
    {
        'title': 'Audio Engineering and Sound Design',
        'category': 'life_skills',
        'description': 'Professional audio engineering - sound design, mixing, mastering, studio techniques, and professional audio production.',
        'level': 'advanced', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 30,
        'objectives': 'Master audio engineering and sound design'
    },
]

# ============================================================
# SECTION 5: INTERNET RESEARCH & ADDITIONAL RESOURCES
# ============================================================
print("\n" + "="*70)
print("🌐 SECTION 5: INTERNET RESEARCH & ADDITIONAL RESOURCES")
print("="*70)

internet_courses = [
    {
        'title': 'Internet Fundamentals and Digital Research',
        'category': 'digital',
        'description': 'Complete internet skills - web browsing, search engines, digital literacy, online research, and evaluating information reliability.',
        'level': 'beginner', 'age_group': 'all', 'approach': 'andragogic', 'duration': 15,
        'objectives': 'Master internet fundamentals and digital research skills'
    },
    {
        'title': 'Social Media Management Professional',
        'category': 'digital',
        'description': 'Professional social media management - Facebook, Twitter, LinkedIn, Instagram, content strategy, analytics, and community engagement.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 25,
        'objectives': 'Master professional social media management'
    },
    {
        'title': 'E-Commerce and Online Business Management',
        'category': 'digital',
        'description': 'Complete e-commerce training - online stores, payment systems, digital marketing, order fulfillment, and e-commerce business management.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 25,
        'objectives': 'Master e-commerce and online business operations'
    },
    {
        'title': 'Digital Marketing and SEO Complete',
        'category': 'digital',
        'description': 'Complete digital marketing - SEO, content marketing, email marketing, social media advertising, and digital marketing strategy.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 25,
        'objectives': 'Master digital marketing and SEO strategies'
    },
    {
        'title': 'Content Creation for Digital Platforms',
        'category': 'digital',
        'description': 'Complete content creation - YouTube, TikTok, Instagram, blogging, podcasting, and professional content strategy for digital platforms.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 20,
        'objectives': 'Master content creation for digital platforms'
    },
    {
        'title': 'Cybersecurity and Digital Safety',
        'category': 'computer',
        'description': 'Complete cybersecurity training - online safety, threat protection, privacy, digital security, and protecting personal information online.',
        'level': 'beginner', 'age_group': 'all', 'approach': 'cybergogic', 'duration': 15,
        'objectives': 'Master cybersecurity and digital safety practices'
    },
]

# ============================================================
# ADD ALL COURSES
# ============================================================
print("\n" + "="*70)
print("📚 ADDING ALL COURSES TO DATABASE")
print("="*70)

all_courses = []
all_courses.extend(basic_computing_courses)
all_courses.extend(office_courses)
all_courses.extend(media_courses)
all_courses.extend(music_courses)
all_courses.extend(internet_courses)

total_added = 0
total_skipped = 0

for course_data in all_courses:
    # Find category
    category = None
    if course_data['category'] in categories:
        category = categories[course_data['category']]
    else:
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
            print(f"✅ Added: {course.title}")
        else:
            total_skipped += 1
            print(f"📚 Already exists: {course.title}")
    else:
        print(f"⚠️ Category '{course_data['category']}' not found - skipping")

# ============================================================
# SUMMARY
# ============================================================
print("\n" + "="*70)
print("📊 SUMMARY")
print("="*70)
print(f"✅ Total Courses Added: {total_added}")
print(f"📚 Total Courses Already Exist: {total_skipped}")
print(f"📚 Total Courses in Database: {Course.objects.filter(is_active=True).count()}")

print("\n📊 Summary by Section:")
print(f"  📱 Basic Computing & OS: {len(basic_computing_courses)} courses")
print(f"  📝 Office & Productivity: {len(office_courses)} courses")
print(f"  🎨 Graphics, Photography, Audio & Video: {len(media_courses)} courses")
print(f"  🎵 Music - Complete: {len(music_courses)} courses")
print(f"  🌐 Internet & Research: {len(internet_courses)} courses")
print(f"  📊 TOTAL: {len(all_courses)} courses")

print("\n📊 Summary by Learning Approach:")
for approach in ['pedagogic', 'andragogic', 'heutagogic', 'cybergogic']:
    count = Course.objects.filter(learning_approach=approach, is_active=True).count()
    print(f"  📖 {approach.upper()}: {count} courses")

print("\n🎉 MISSING COURSES ADDITION COMPLETE!")
print("="*70)