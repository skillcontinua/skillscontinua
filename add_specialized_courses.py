import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from courses.models import Category, Course

print("🚀 Adding SPECIALIZED COURSES to SkillsContinua...")
print("="*60)

# Get all categories
categories = {}
for cat in Category.objects.all():
    categories[cat.pillar] = cat
    categories[cat.name] = cat  # Also index by name

print(f"Found {len(categories)} categories")

# Specialized courses by category
specialized_courses = [
    # ===== TECHNOLOGY & IT =====
    {
        'title': 'CCTV Installation and Maintenance',
        'category': 'technology',
        'description': 'Complete CCTV installation - camera selection, wiring, recording systems, remote monitoring, and maintenance.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 25,
        'objectives': 'Master professional CCTV installation and security systems'
    },
    {
        'title': 'Drone Piloting and Operations',
        'category': 'technology',
        'description': 'Professional drone piloting - flight operations, regulations, aerial photography, and drone maintenance.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 20,
        'objectives': 'Become a certified drone pilot and operator'
    },
    {
        'title': 'Robotics and Automation',
        'category': 'technology',
        'description': 'Robotics fundamentals - robot design, programming, sensors, actuators, and automation systems.',
        'level': 'advanced', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 30,
        'objectives': 'Master robotics design and automation programming'
    },
    {
        'title': 'Cybersecurity Fundamentals',
        'category': 'technology',
        'description': 'Comprehensive cybersecurity - threat detection, network security, ethical hacking, and security protocols.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 25,
        'objectives': 'Master cybersecurity fundamentals and threat protection'
    },
    {
        'title': 'Cloud Computing and AWS',
        'category': 'technology',
        'description': 'Cloud computing fundamentals - AWS, Azure, cloud architecture, and cloud services deployment.',
        'level': 'advanced', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 30,
        'objectives': 'Master cloud computing and AWS services'
    },
    {
        'title': 'Artificial Intelligence and Machine Learning',
        'category': 'technology',
        'description': 'AI and ML fundamentals - algorithms, neural networks, data science, and practical AI applications.',
        'level': 'advanced', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 35,
        'objectives': 'Master AI and machine learning concepts and applications'
    },
    {
        'title': 'Digital Forensics and Investigation',
        'category': 'technology',
        'description': 'Digital forensics - evidence collection, computer forensics, mobile forensics, and investigation techniques.',
        'level': 'advanced', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 25,
        'objectives': 'Master digital forensics and investigation skills'
    },
    
    # ===== COMPUTER LITERACY =====
    {
        'title': 'Network Administration and Management',
        'category': 'computer',
        'description': 'Network administration - routing, switching, network security, and enterprise network management.',
        'level': 'advanced', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 30,
        'objectives': 'Master enterprise network administration'
    },
    {
        'title': 'Database Management and SQL',
        'category': 'computer',
        'description': 'Database management - SQL, database design, administration, and data optimization.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 25,
        'objectives': 'Master database management and SQL'
    },
    {
        'title': 'Web Development - Full Stack',
        'category': 'computer',
        'description': 'Full stack web development - HTML, CSS, JavaScript, Python, React, and modern web frameworks.',
        'level': 'advanced', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 40,
        'objectives': 'Become a full stack web developer'
    },
    {
        'title': 'Mobile App Development',
        'category': 'computer',
        'description': 'Mobile app development - Android, iOS, cross-platform development, and app deployment.',
        'level': 'advanced', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 35,
        'objectives': 'Master mobile app development for Android and iOS'
    },
    
    # ===== CERTIFICATIONS =====
    {
        'title': 'CompTIA Security+ Certification',
        'category': 'certification',
        'description': 'CompTIA Security+ - cybersecurity certification preparation, security concepts, and exam preparation.',
        'level': 'advanced', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 35,
        'objectives': 'Prepare for CompTIA Security+ certification'
    },
    {
        'title': 'CISSP Certification Preparation',
        'category': 'certification',
        'description': 'CISSP certification - security management, risk assessment, and professional certification exam prep.',
        'level': 'advanced', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 40,
        'objectives': 'Prepare for CISSP professional certification'
    },
    {
        'title': 'Cisco CCNA Certification',
        'category': 'certification',
        'description': 'Cisco CCNA - networking fundamentals, routing, switching, and CCNA certification preparation.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 30,
        'objectives': 'Prepare for Cisco CCNA certification'
    },
    {
        'title': 'AWS Cloud Practitioner Certification',
        'category': 'certification',
        'description': 'AWS Cloud Practitioner - cloud computing, AWS services, and cloud certification preparation.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 25,
        'objectives': 'Prepare for AWS Cloud Practitioner certification'
    },
    {
        'title': 'Project Management Professional (PMP)',
        'category': 'certification',
        'description': 'PMP certification - project management framework, methodologies, and professional certification.',
        'level': 'advanced', 'age_group': 'adult', 'approach': 'heutagogic', 'duration': 35,
        'objectives': 'Prepare for PMP professional certification'
    },
    
    # ===== VOCATIONAL TRADES =====
    {
        'title': 'Advanced Carpentry and Furniture Design',
        'category': 'vocational',
        'description': 'Advanced carpentry - furniture design, cabinetry, custom woodworking, and finishing techniques.',
        'level': 'advanced', 'age_group': 'adult', 'approach': 'andragogic', 'duration': 35,
        'objectives': 'Master advanced carpentry and furniture design'
    },
    {
        'title': 'Advanced Welding and Fabrication',
        'category': 'vocational',
        'description': 'Advanced welding - TIG, MIG, arc welding, metal fabrication, and structural welding.',
        'level': 'advanced', 'age_group': 'adult', 'approach': 'andragogic', 'duration': 35,
        'objectives': 'Master advanced welding and metal fabrication'
    },
    {
        'title': 'Electrical Installation and Solar Systems',
        'category': 'vocational',
        'description': 'Electrical installation - wiring, solar systems, renewable energy, and smart home technology.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 30,
        'objectives': 'Master electrical installation and solar systems'
    },
    
    # ===== BUILDING & CONSTRUCTION =====
    {
        'title': 'Advanced Masonry and Stone Work',
        'category': 'building',
        'description': 'Advanced masonry - stone work, decorative bricklaying, and high-end construction techniques.',
        'level': 'advanced', 'age_group': 'adult', 'approach': 'andragogic', 'duration': 30,
        'objectives': 'Master advanced masonry and stone construction'
    },
    {
        'title': 'Interior Design and Decoration',
        'category': 'building',
        'description': 'Interior design - space planning, color theory, furniture selection, and home decoration.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'andragogic', 'duration': 25,
        'objectives': 'Master interior design and home decoration'
    },
    {
        'title': 'Green Building and Sustainable Construction',
        'category': 'building',
        'description': 'Green building - sustainable materials, energy efficiency, and eco-friendly construction practices.',
        'level': 'advanced', 'age_group': 'adult', 'approach': 'heutagogic', 'duration': 25,
        'objectives': 'Master sustainable and green building construction'
    },
    
    # ===== AUTOMOTIVE =====
    {
        'title': 'Advanced Auto Diagnostics and Repair',
        'category': 'automotive',
        'description': 'Advanced auto diagnostics - computer systems, engine diagnostics, and modern vehicle repair.',
        'level': 'advanced', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 35,
        'objectives': 'Master advanced automotive diagnostics and repair'
    },
    {
        'title': 'Electric Vehicle (EV) Technology',
        'category': 'automotive',
        'description': 'Electric vehicle technology - EV systems, battery technology, charging stations, and EV maintenance.',
        'level': 'advanced', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 30,
        'objectives': 'Master electric vehicle technology and maintenance'
    },
    {
        'title': 'Generator and Plant Maintenance',
        'category': 'automotive',
        'description': 'Generator and plant maintenance - diesel generators, power plants, and industrial equipment maintenance.',
        'level': 'advanced', 'age_group': 'adult', 'approach': 'andragogic', 'duration': 30,
        'objectives': 'Master generator and industrial plant maintenance'
    },
    
    # ===== HOUSING & APPLIANCES =====
    {
        'title': 'Air Conditioning and Refrigeration Systems',
        'category': 'housing',
        'description': 'AC and refrigeration - cooling systems, refrigerants, and commercial refrigeration maintenance.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'andragogic', 'duration': 25,
        'objectives': 'Master air conditioning and refrigeration systems'
    },
    {
        'title': 'Smart Home Technology',
        'category': 'housing',
        'description': 'Smart home technology - home automation, security systems, and IoT device integration.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 20,
        'objectives': 'Master smart home technology and automation'
    },
    
    # ===== BEAUTY & PERSONAL CARE =====
    {
        'title': 'Advanced Hair Styling and Salon Management',
        'category': 'beauty',
        'description': 'Advanced hair styling - professional techniques, salon management, and beauty business operations.',
        'level': 'advanced', 'age_group': 'adult', 'approach': 'andragogic', 'duration': 25,
        'objectives': 'Master advanced hair styling and salon management'
    },
    {
        'title': 'Professional Makeup and Beauty Artistry',
        'category': 'beauty',
        'description': 'Professional makeup artistry - wedding makeup, fashion, and beauty industry techniques.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'andragogic', 'duration': 25,
        'objectives': 'Master professional makeup artistry and beauty skills'
    },
    
    # ===== SECONDARY EDUCATION =====
    {
        'title': 'Advanced Mathematics - Secondary',
        'category': 'secondary',
        'description': 'Advanced mathematics - algebra, calculus, statistics, and problem solving for secondary students.',
        'level': 'advanced', 'age_group': 'teen', 'approach': 'pedagogic', 'duration': 40,
        'objectives': 'Master advanced secondary mathematics'
    },
    {
        'title': 'Advanced Physics - Secondary',
        'category': 'secondary',
        'description': 'Advanced physics - mechanics, thermodynamics, quantum physics, and scientific methodology.',
        'level': 'advanced', 'age_group': 'teen', 'approach': 'pedagogic', 'duration': 40,
        'objectives': 'Master advanced secondary physics'
    },
    
    # ===== DIGITAL SKILLS =====
    {
        'title': 'Digital Marketing and SEO',
        'category': 'digital',
        'description': 'Digital marketing - SEO, social media marketing, content marketing, and online advertising.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 25,
        'objectives': 'Master digital marketing and SEO strategies'
    },
    {
        'title': 'Graphic Design and Visual Communication',
        'category': 'digital',
        'description': 'Graphic design - Photoshop, Illustrator, visual branding, and digital communication.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 25,
        'objectives': 'Master graphic design and visual communication'
    },
    {
        'title': 'Video Production and Editing',
        'category': 'digital',
        'description': 'Video production - filming, editing, content creation, and professional video techniques.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 25,
        'objectives': 'Master video production and editing skills'
    },
    
    # ===== LIFE SKILLS =====
    {
        'title': 'Advanced Leadership and Management',
        'category': 'life_skills',
        'description': 'Advanced leadership - strategic leadership, organizational management, and executive development.',
        'level': 'advanced', 'age_group': 'adult', 'approach': 'heutagogic', 'duration': 30,
        'objectives': 'Master advanced leadership and management skills'
    },
    {
        'title': 'International Relations and Diplomacy',
        'category': 'life_skills',
        'description': 'International relations - diplomacy, global politics, conflict resolution, and international cooperation.',
        'level': 'advanced', 'age_group': 'adult', 'approach': 'heutagogic', 'duration': 25,
        'objectives': 'Master international relations and diplomacy'
    },
]

# Add specialized courses
total_added = 0
for course_data in specialized_courses:
    # Try to find category by pillar or name
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
        print(f"⚠️ Category '{course_data['category']}' not found - skipping {course_data['title']}")

print("\n" + "="*60)
print(f"📊 Total Specialized Courses Added: {total_added}")
print(f"📚 Total Courses in Database: {Course.objects.filter(is_active=True).count()}")

# Summary by approach
print("\n📊 Summary by Learning Approach:")
for approach in ['pedagogic', 'andragogic', 'heutagogic', 'cybergogic']:
    count = Course.objects.filter(learning_approach=approach, is_active=True).count()
    print(f"  📖 {approach.upper()}: {count} courses")

# Summary by category
print("\n📊 Summary by Category (with courses):")
for cat in Category.objects.all():
    count = Course.objects.filter(category=cat, is_active=True).count()
    if count > 0:
        print(f"  📁 {cat.name}: {count} courses")

print("\n🎉 Specialized course addition complete!")