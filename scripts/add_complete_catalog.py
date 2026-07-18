import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from courses.models import Category, Course

print("🌍 Adding COMPLETE SKILLSCONTINUA COURSE CATALOG...")
print("="*60)

# Create/Update Categories with proper grouping
categories_data = [
    # FOUNDATIONAL (Pedagogic focus)
    {'name': 'Primary Education', 'pillar': 'primary', 
     'description': 'Complete primary school curriculum - Literacy, Numeracy, Science, Social Studies, and Creative Arts'},
    
    {'name': 'Secondary Education - Arts', 'pillar': 'secondary_arts', 
     'description': 'Secondary education in Arts - Literature, History, Geography, Languages, and Creative Arts'},
    
    {'name': 'Secondary Education - Commercial', 'pillar': 'secondary_commercial', 
     'description': 'Secondary education in Commerce - Business Studies, Accounting, Economics, and Entrepreneurship'},
    
    {'name': 'Secondary Education - Science', 'pillar': 'secondary_science', 
     'description': 'Secondary education in Science - Biology, Chemistry, Physics, and Mathematics'},
    
    {'name': 'Secondary Education - Technical', 'pillar': 'secondary_technical', 
     'description': 'Secondary education in Technical - Engineering, Design, and Technology'},
    
    {'name': 'Secondary Education - Trade', 'pillar': 'secondary_trade', 
     'description': 'Secondary education in Trade - Vocational skills and practical trades'},
    
    # BUILDING & CONSTRUCTION (Andragogic/Heutagogic focus)
    {'name': 'Building Construction', 'pillar': 'building', 
     'description': 'Complete building construction skills - Masonry, Roofing, Tiling, Plumbing, Painting, and more'},
    
    {'name': 'Housing and Appliances', 'pillar': 'housing', 
     'description': 'Housing maintenance and appliance repair - Fridge, Air Conditioning, TV, Radio, and home systems'},
    
    {'name': 'Electrical Installation', 'pillar': 'electrical', 
     'description': 'Electrical skills - Wiring, Solar installation, Generator repair, and power systems'},
    
    # AUTOMOTIVE (Andragogic/Heutagogic focus)
    {'name': 'Automotive - Motorcycles', 'pillar': 'auto_motorcycle', 
     'description': 'Motorcycle and tricycle mechanics - Repair, maintenance, and diagnostics'},
    
    {'name': 'Automotive - Cars and Vans', 'pillar': 'auto_cars', 
     'description': 'Car and van mechanics - Engine repair, transmission, brakes, and electrical systems'},
    
    {'name': 'Automotive - Heavy Vehicles', 'pillar': 'auto_heavy', 
     'description': 'Heavy vehicle mechanics - Buses, Trucks, Plants, and Generators'},
    
    # BEAUTY & PERSONAL CARE (Andragogic focus)
    {'name': 'Hair Care and Styling', 'pillar': 'beauty_hair', 
     'description': 'Hair care services - Cutting, Braiding, Weaving, Hair treatment, and styling'},
    
    {'name': 'Makeup and Beauty', 'pillar': 'beauty_makeup', 
     'description': 'Makeup artistry - Face and body beauty care, makeup techniques, and personal grooming'},
    
    # COMPUTER & TECHNOLOGY (Cybergogic focus)
    {'name': 'Computer Literacy', 'pillar': 'computer', 
     'description': 'Basic to advanced IT skills - Hardware, Software, Cybersecurity, AI, and emerging tech'},
    
    {'name': 'Information Technology', 'pillar': 'it', 
     'description': 'IT professional skills - Programming, Networking, Database, Cloud Computing, and DevOps'},
    
    {'name': 'Digital Skills', 'pillar': 'digital', 
     'description': 'Digital literacy - Social media, Digital marketing, Content creation, and online business'},
    
    # VOCATIONAL & TRADES (Andragogic focus)
    {'name': 'Carpentry and Woodwork', 'pillar': 'carpentry', 
     'description': 'Carpentry skills - Furniture making, Woodwork, Joinery, and finishing'},
    
    {'name': 'Welding and Metalwork', 'pillar': 'welding', 
     'description': 'Welding skills - Arc welding, MIG, TIG, Metal fabrication, and blacksmithing'},
    
    {'name': 'Agriculture and Farming', 'pillar': 'agriculture', 
     'description': 'Modern farming - Crop cultivation, Animal husbandry, Agribusiness, and sustainable practices'},
    
    {'name': 'Tailoring and Fashion', 'pillar': 'tailoring', 
     'description': 'Fashion and tailoring - Sewing, Pattern making, African textile design, and fashion business'},
    
    # LIFE SKILLS (All approaches)
    {'name': 'Financial Literacy', 'pillar': 'financial', 
     'description': 'Financial skills - Budgeting, Saving, Investing, Entrepreneurship, and wealth creation'},
    
    {'name': 'Life Skills', 'pillar': 'life_skills', 
     'description': 'Essential life skills - Communication, Leadership, Emotional intelligence, and personal development'},
    
    # CERTIFICATIONS (Cybergogic/Andragogic focus)
    {'name': 'Professional Certifications', 'pillar': 'certification', 
     'description': 'International certifications - CompTIA, Cisco, AWS, PMP, and professional credentials'},
]

# Create categories
category_objects = {}
for cat_data in categories_data:
    cat, created = Category.objects.get_or_create(
        pillar=cat_data['pillar'],
        defaults={
            'name': cat_data['name'],
            'description': cat_data['description']
        }
    )
    category_objects[cat.pillar] = cat
    print(f"{'✅' if created else '📚'} Category: {cat.name}")

print("\n" + "="*60)
print("📚 Adding Courses...")
print("="*60)

# Define courses by category with approach, level, and age group
courses_data = [
    # ===== PEDAGOGIC - PRIMARY EDUCATION =====
    {
        'title': 'Primary English - Reading and Writing',
        'category': 'primary',
        'description': 'Complete primary English curriculum - literacy, grammar, reading comprehension, and writing skills.',
        'level': 'beginner', 'age_group': 'child', 'approach': 'pedagogic', 'duration': 40,
        'objectives': 'Master reading, writing, and communication skills at primary level'
    },
    {
        'title': 'Primary Mathematics - Complete',
        'category': 'primary',
        'description': 'Complete primary mathematics - numbers, operations, geometry, measurements, and problem solving.',
        'level': 'beginner', 'age_group': 'child', 'approach': 'pedagogic', 'duration': 40,
        'objectives': 'Build strong mathematical foundations for lifelong learning'
    },
    {
        'title': 'Primary Science - Basic Concepts',
        'category': 'primary',
        'description': 'Primary science - life sciences, physical sciences, earth sciences, and environmental awareness.',
        'level': 'beginner', 'age_group': 'child', 'approach': 'pedagogic', 'duration': 35,
        'objectives': 'Develop curiosity and understanding of the natural world'
    },
    {
        'title': 'Primary Social Studies - Africa Focus',
        'category': 'primary',
        'description': 'Social studies with African focus - geography, history, civics, and cultural heritage.',
        'level': 'beginner', 'age_group': 'child', 'approach': 'pedagogic', 'duration': 30,
        'objectives': 'Understand African history, geography, and civic responsibility'
    },
    {
        'title': 'Primary Health and Life Skills',
        'category': 'primary',
        'description': 'Personal health, hygiene, nutrition, safety, and life skills for children.',
        'level': 'beginner', 'age_group': 'child', 'approach': 'pedagogic', 'duration': 25,
        'objectives': 'Develop healthy habits and essential life skills'
    },
    
    # ===== PEDAGOGIC - SECONDARY EDUCATION =====
    # Arts
    {
        'title': 'Secondary English Literature',
        'category': 'secondary_arts',
        'description': 'Advanced English literature - poetry, prose, drama, and literary analysis.',
        'level': 'intermediate', 'age_group': 'teen', 'approach': 'pedagogic', 'duration': 45,
        'objectives': 'Develop literary analysis and critical thinking through literature'
    },
    {
        'title': 'Secondary History and Geography',
        'category': 'secondary_arts',
        'description': 'Comprehensive history and geography - world history, African history, and geographical studies.',
        'level': 'intermediate', 'age_group': 'teen', 'approach': 'pedagogic', 'duration': 40,
        'objectives': 'Understand historical events and geographical concepts'
    },
    # Commercial
    {
        'title': 'Secondary Commerce and Business',
        'category': 'secondary_commercial',
        'description': 'Commerce, accounting, entrepreneurship, and business management fundamentals.',
        'level': 'intermediate', 'age_group': 'teen', 'approach': 'pedagogic', 'duration': 40,
        'objectives': 'Build business acumen and entrepreneurial skills'
    },
    {
        'title': 'Secondary Economics',
        'category': 'secondary_commercial',
        'description': 'Microeconomics, macroeconomics, and economic principles for business.',
        'level': 'intermediate', 'age_group': 'teen', 'approach': 'pedagogic', 'duration': 35,
        'objectives': 'Understand economic principles and their applications'
    },
    # Science
    {
        'title': 'Secondary Biology',
        'category': 'secondary_science',
        'description': 'Comprehensive biology - cell biology, genetics, ecology, and human biology.',
        'level': 'intermediate', 'age_group': 'teen', 'approach': 'pedagogic', 'duration': 45,
        'objectives': 'Master biological concepts and scientific methodology'
    },
    {
        'title': 'Secondary Chemistry',
        'category': 'secondary_science',
        'description': 'Comprehensive chemistry - organic, inorganic, physical chemistry, and chemical reactions.',
        'level': 'intermediate', 'age_group': 'teen', 'approach': 'pedagogic', 'duration': 45,
        'objectives': 'Understand chemical principles and laboratory techniques'
    },
    {
        'title': 'Secondary Physics',
        'category': 'secondary_science',
        'description': 'Comprehensive physics - mechanics, energy, waves, electricity, and modern physics.',
        'level': 'intermediate', 'age_group': 'teen', 'approach': 'pedagogic', 'duration': 45,
        'objectives': 'Master physical principles and scientific problem solving'
    },
    # Technical
    {
        'title': 'Secondary Technical Design',
        'category': 'secondary_technical',
        'description': 'Technical drawing, design principles, and engineering fundamentals.',
        'level': 'intermediate', 'age_group': 'teen', 'approach': 'pedagogic', 'duration': 40,
        'objectives': 'Develop technical design and engineering skills'
    },
    # Trade
    {
        'title': 'Secondary Vocational Skills',
        'category': 'secondary_trade',
        'description': 'Practical vocational skills - woodwork, metalwork, and trade fundamentals.',
        'level': 'intermediate', 'age_group': 'teen', 'approach': 'pedagogic', 'duration': 40,
        'objectives': 'Build practical trade skills for career readiness'
    },
    
    # ===== ANDRAGOGIC - BUILDING & CONSTRUCTION =====
    {
        'title': 'Masonry and Bricklaying',
        'category': 'building',
        'description': 'Professional masonry skills - bricklaying, concrete work, block laying, and stone masonry.',
        'level': 'beginner', 'age_group': 'adult', 'approach': 'andragogic', 'duration': 30,
        'objectives': 'Master professional masonry techniques for building construction'
    },
    {
        'title': 'Roofing and Tiling',
        'category': 'building',
        'description': 'Complete roofing and tiling skills - roof construction, tiling techniques, and finishing.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'andragogic', 'duration': 25,
        'objectives': 'Develop professional roofing and tiling expertise'
    },
    {
        'title': 'Plumbing and Sanitation',
        'category': 'building',
        'description': 'Professional plumbing - pipe fitting, water systems, sanitation, and solar water heating.',
        'level': 'beginner', 'age_group': 'adult', 'approach': 'andragogic', 'duration': 25,
        'objectives': 'Master residential and commercial plumbing systems'
    },
    {
        'title': 'Painting and Decorating',
        'category': 'building',
        'description': 'Professional painting techniques - interior, exterior, and decorative painting.',
        'level': 'beginner', 'age_group': 'adult', 'approach': 'andragogic', 'duration': 20,
        'objectives': 'Develop professional painting and decorating skills'
    },
    {
        'title': 'Construction Project Management',
        'category': 'building',
        'description': 'Project management for construction - planning, budgeting, and supervising building projects.',
        'level': 'advanced', 'age_group': 'adult', 'approach': 'heutagogic', 'duration': 35,
        'objectives': 'Master construction project management and leadership'
    },
    
    # ===== ANDRAGOGIC/HEUTAGOGIC - HOUSING & APPLIANCES =====
    {
        'title': 'Refrigerator and AC Repair',
        'category': 'housing',
        'description': 'Complete refrigeration and air conditioning repair - diagnosis, maintenance, and repair.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'andragogic', 'duration': 30,
        'objectives': 'Master refrigeration and AC repair techniques'
    },
    {
        'title': 'TV and Radio Repair',
        'category': 'housing',
        'description': 'Television and radio repair - troubleshooting, component repair, and maintenance.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'andragogic', 'duration': 25,
        'objectives': 'Develop professional TV and radio repair skills'
    },
    {
        'title': 'Home Appliance Repair',
        'category': 'housing',
        'description': 'Complete home appliance repair - washing machines, ovens, and household appliances.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'andragogic', 'duration': 28,
        'objectives': 'Master home appliance diagnosis and repair'
    },
    {
        'title': 'Home Electrical Systems',
        'category': 'housing',
        'description': 'Home electrical systems - wiring, circuits, safety, and smart home technology.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'andragogic', 'duration': 30,
        'objectives': 'Master residential electrical systems and safety'
    },
    {
        'title': 'Solar Installation and Maintenance',
        'category': 'housing',
        'description': 'Solar energy systems - installation, maintenance, and troubleshooting of solar panels and inverters.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 25,
        'objectives': 'Master solar energy installation and maintenance'
    },
    
    # ===== ANDRAGOGIC/HEUTAGOGIC - AUTOMOTIVE =====
    {
        'title': 'Motorcycle and Tricycle Mechanics',
        'category': 'auto_motorcycle',
        'description': 'Complete motorcycle and tricycle mechanics - engine repair, transmission, and maintenance.',
        'level': 'beginner', 'age_group': 'adult', 'approach': 'andragogic', 'duration': 30,
        'objectives': 'Master motorcycle and tricycle mechanics'
    },
    {
        'title': 'Car and Van Mechanics',
        'category': 'auto_cars',
        'description': 'Professional car and van mechanics - engines, transmissions, brakes, and electrical systems.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'andragogic', 'duration': 40,
        'objectives': 'Master professional automotive repair and maintenance'
    },
    {
        'title': 'Heavy Vehicle Mechanics',
        'category': 'auto_heavy',
        'description': 'Heavy vehicle mechanics - trucks, buses, plant machinery, and generator repair.',
        'level': 'advanced', 'age_group': 'adult', 'approach': 'andragogic', 'duration': 45,
        'objectives': 'Master heavy vehicle and industrial equipment mechanics'
    },
    {
        'title': 'Automotive Electrical Systems',
        'category': 'auto_cars',
        'description': 'Advanced automotive electrical systems - diagnostics, repair, and computer systems.',
        'level': 'advanced', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 35,
        'objectives': 'Master automotive electrical and computer diagnostics'
    },
    
    # ===== ANDRAGOGIC - BEAUTY & PERSONAL CARE =====
    {
        'title': 'Hair Cutting and Styling',
        'category': 'beauty_hair',
        'description': 'Professional hair cutting and styling - techniques, tools, and trends.',
        'level': 'beginner', 'age_group': 'adult', 'approach': 'andragogic', 'duration': 25,
        'objectives': 'Master professional hair cutting and styling techniques'
    },
    {
        'title': 'Braiding and Weaving',
        'category': 'beauty_hair',
        'description': 'Professional braiding, weaving, and hair treatment - African hair care and styling.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'andragogic', 'duration': 25,
        'objectives': 'Master traditional and modern braiding and weaving techniques'
    },
    {
        'title': 'Hair Treatment and Care',
        'category': 'beauty_hair',
        'description': 'Professional hair treatment and care - hair health, scalp treatments, and natural hair care.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'andragogic', 'duration': 20,
        'objectives': 'Master hair treatment and healthy hair practices'
    },
    {
        'title': 'Makeup Artistry',
        'category': 'beauty_makeup',
        'description': 'Professional makeup artistry - face and body beauty care, makeup techniques, and products.',
        'level': 'beginner', 'age_group': 'adult', 'approach': 'andragogic', 'duration': 25,
        'objectives': 'Master professional makeup artistry and beauty techniques'
    },
    {
        'title': 'Face and Body Beauty Care',
        'category': 'beauty_makeup',
        'description': 'Complete face and body beauty care - skincare, facials, body treatments, and wellness.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'andragogic', 'duration': 25,
        'objectives': 'Master professional beauty care and wellness practices'
    },
    
    # ===== CYBERGOGIC - COMPUTER & TECHNOLOGY =====
    {
        'title': 'Introduction to Computers',
        'category': 'computer',
        'description': 'Basic computer literacy - hardware, software, operating systems, and internet basics.',
        'level': 'beginner', 'age_group': 'all', 'approach': 'cybergogic', 'duration': 15,
        'objectives': 'Build foundational computer literacy skills'
    },
    {
        'title': 'Computer Hardware and Repair',
        'category': 'computer',
        'description': 'Professional computer hardware - installation, repair, and maintenance of computer components.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 25,
        'objectives': 'Master computer hardware repair and maintenance'
    },
    {
        'title': 'Cybersecurity Fundamentals',
        'category': 'computer',
        'description': 'Cybersecurity principles - threat protection, security protocols, and digital safety.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 20,
        'objectives': 'Master cybersecurity fundamentals and digital protection'
    },
    {
        'title': 'Web Development Fundamentals',
        'category': 'it',
        'description': 'Web development - HTML, CSS, JavaScript, and responsive web design.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 30,
        'objectives': 'Build modern web development skills'
    },
    {
        'title': 'Database Management',
        'category': 'it',
        'description': 'Database systems - SQL, NoSQL, database design, and management.',
        'level': 'advanced', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 30,
        'objectives': 'Master database management and design'
    },
    {
        'title': 'Digital Marketing',
        'category': 'digital',
        'description': 'Digital marketing - social media, SEO, content marketing, and online advertising.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 25,
        'objectives': 'Master digital marketing strategies and tools'
    },
    {
        'title': 'Artificial Intelligence and Machine Learning',
        'category': 'it',
        'description': 'AI and ML fundamentals - algorithms, applications, and practical implementations.',
        'level': 'advanced', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 35,
        'objectives': 'Master AI and machine learning concepts and applications'
    },
    
    # ===== ANDRAGOGIC - VOCATIONAL & TRADES =====
    {
        'title': 'Carpentry and Furniture Making',
        'category': 'carpentry',
        'description': 'Professional carpentry - furniture making, joinery, and woodworking techniques.',
        'level': 'beginner', 'age_group': 'adult', 'approach': 'andragogic', 'duration': 30,
        'objectives': 'Master professional carpentry and furniture making'
    },
    {
        'title': 'Advanced Woodworking',
        'category': 'carpentry',
        'description': 'Advanced woodworking - cabinetry, intricate joinery, and fine furniture making.',
        'level': 'advanced', 'age_group': 'adult', 'approach': 'heutagogic', 'duration': 35,
        'objectives': 'Master advanced woodworking and fine furniture making'
    },
    {
        'title': 'Welding and Metal Fabrication',
        'category': 'welding',
        'description': 'Professional welding - MIG, TIG, arc welding, and metal fabrication.',
        'level': 'beginner', 'age_group': 'adult', 'approach': 'andragogic', 'duration': 30,
        'objectives': 'Master professional welding and metal fabrication'
    },
    {
        'title': 'Advanced Metalwork',
        'category': 'welding',
        'description': 'Advanced metalwork - blacksmithing, ornamental metalwork, and structural fabrication.',
        'level': 'advanced', 'age_group': 'adult', 'approach': 'heutagogic', 'duration': 35,
        'objectives': 'Master advanced metalwork and fabrication techniques'
    },
    {
        'title': 'Agriculture and Agribusiness',
        'category': 'agriculture',
        'description': 'Modern agriculture - crop cultivation, animal husbandry, and agribusiness management.',
        'level': 'beginner', 'age_group': 'adult', 'approach': 'andragogic', 'duration': 30,
        'objectives': 'Master modern agriculture and agribusiness skills'
    },
    {
        'title': 'Sustainable Farming Practices',
        'category': 'agriculture',
        'description': 'Sustainable agriculture - organic farming, water conservation, and environmental stewardship.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'heutagogic', 'duration': 25,
        'objectives': 'Master sustainable farming and environmental practices'
    },
    {
        'title': 'Tailoring and Fashion Design',
        'category': 'tailoring',
        'description': 'Professional tailoring - sewing, pattern making, and fashion design.',
        'level': 'beginner', 'age_group': 'adult', 'approach': 'andragogic', 'duration': 25,
        'objectives': 'Master professional tailoring and fashion design'
    },
    {
        'title': 'African Textile Design',
        'category': 'tailoring',
        'description': 'African textile design - traditional fabrics, batik, tie-dye, and contemporary fashion.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'andragogic', 'duration': 25,
        'objectives': 'Master African textile design and production'
    },
    
    # ===== LIFE SKILLS (All approaches) =====
    {
        'title': 'Financial Management and Planning',
        'category': 'financial',
        'description': 'Personal and business finance - budgeting, saving, investing, and financial planning.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'andragogic', 'duration': 25,
        'objectives': 'Master personal and business financial management'
    },
    {
        'title': 'Business Planning and Entrepreneurship',
        'category': 'financial',
        'description': 'Entrepreneurship - business planning, startup management, and business growth.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'heutagogic', 'duration': 25,
        'objectives': 'Master entrepreneurship and business planning'
    },
    {
        'title': 'Leadership and Management',
        'category': 'life_skills',
        'description': 'Leadership skills - team management, organizational leadership, and personal development.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'heutagogic', 'duration': 20,
        'objectives': 'Master leadership and management skills'
    },
    {
        'title': 'Communication and Interpersonal Skills',
        'category': 'life_skills',
        'description': 'Essential communication - public speaking, interpersonal skills, and professional communication.',
        'level': 'beginner', 'age_group': 'all', 'approach': 'andragogic', 'duration': 15,
        'objectives': 'Master effective communication and interpersonal skills'
    },
    {
        'title': 'Critical Thinking and Problem Solving',
        'category': 'life_skills',
        'description': 'Critical thinking - problem-solving frameworks, decision making, and analytical skills.',
        'level': 'intermediate', 'age_group': 'all', 'approach': 'heutagogic', 'duration': 20,
        'objectives': 'Master critical thinking and problem-solving skills'
    },
    {
        'title': 'Emotional Intelligence and Mental Health',
        'category': 'life_skills',
        'description': 'Emotional intelligence - self-awareness, mental health, resilience, and personal well-being.',
        'level': 'beginner', 'age_group': 'all', 'approach': 'andragogic', 'duration': 15,
        'objectives': 'Develop emotional intelligence and mental health awareness'
    },
    
    # ===== PROFESSIONAL CERTIFICATIONS (Cybergogic/Andragogic) =====
    {
        'title': 'CompTIA IT Fundamentals',
        'category': 'certification',
        'description': 'CompTIA IT Fundamentals certification - prepare for international IT certification.',
        'level': 'intermediate', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 30,
        'objectives': 'Prepare for CompTIA IT Fundamentals certification'
    },
    {
        'title': 'CompTIA Security+ Certification',
        'category': 'certification',
        'description': 'CompTIA Security+ - cybersecurity certification preparation and security fundamentals.',
        'level': 'advanced', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 35,
        'objectives': 'Master cybersecurity concepts and prepare for Security+ certification'
    },
    {
        'title': 'AWS Cloud Computing Certification',
        'category': 'certification',
        'description': 'AWS Cloud computing - cloud architecture, services, and certification preparation.',
        'level': 'advanced', 'age_group': 'adult', 'approach': 'cybergogic', 'duration': 35,
        'objectives': 'Master AWS cloud computing and prepare for certification'
    },
    {
        'title': 'PMP Project Management Certification',
        'category': 'certification',
        'description': 'Project Management Professional (PMP) - project management framework and certification prep.',
        'level': 'advanced', 'age_group': 'adult', 'approach': 'heutagogic', 'duration': 30,
        'objectives': 'Master project management and prepare for PMP certification'
    },
]

# Add courses
total_courses = 0
for course_data in courses_data:
    category = category_objects.get(course_data['category'])
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
                'featured': course_data.get('approach') in ['pedagogic', 'andragogic'] and course_data.get('level') == 'beginner',
            }
        )
        if created:
            total_courses += 1
            print(f"✅ Added: {course.title} ({course_data['approach'].upper()})")
    else:
        print(f"⚠️ Category '{course_data['category']}' not found")

print("\n" + "="*60)
print(f"📊 Total Courses Added: {total_courses}")
print(f"📚 Total Courses in Database: {Course.objects.filter(is_active=True).count()}")

# Summary by approach
print("\n📊 Summary by Learning Approach:")
for approach in ['pedagogic', 'andragogic', 'heutagogic', 'cybergogic']:
    count = Course.objects.filter(learning_approach=approach, is_active=True).count()
    print(f"  📖 {approach.upper()}: {count} courses")

# Summary by category
print("\n📊 Summary by Category:")
for cat in Category.objects.all():
    count = Course.objects.filter(category=cat, is_active=True).count()
    if count > 0:
        print(f"  📁 {cat.name}: {count} courses")

print("\n🎉 Complete catalog addition complete!")