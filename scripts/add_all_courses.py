import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from courses.models import Category, Course

print("🌍 Adding complete African SkillsContinua curriculum...")

# Get or create all 7 categories (pillars)
categories = {}
pillars = [
    {'name': 'Foundational Literacy', 'pillar': 'literacy', 
     'description': 'From complete illiteracy to confident reading, writing and numeracy - in English and local languages'},
    
    {'name': 'Computer Literacy', 'pillar': 'computer', 
     'description': 'Basic to advanced IT skills - hardware, software, cybersecurity, AI, and emerging technologies'},
    
    {'name': 'Vocational Trades', 'pillar': 'vocational', 
     'description': 'Practical skills for self-employment - construction, repair, agriculture, and artisan trades'},
    
    {'name': 'Certifications', 'pillar': 'certification', 
     'description': 'Professional certifications - CompTIA, Cisco, AWS, and international credentials'},
    
    {'name': 'Life Skills', 'pillar': 'life_skills', 
     'description': 'Essential life competencies - financial literacy, emotional intelligence, entrepreneurship'},
    
    {'name': 'Primary Education', 'pillar': 'primary', 
     'description': 'Complete primary curriculum - literacy, numeracy, science, social studies'},
    
    {'name': 'Secondary Education', 'pillar': 'secondary', 
     'description': 'Advanced secondary education - STEM, commerce, arts, and technical tracks'},
]

for pillar_data in pillars:
    cat, created = Category.objects.get_or_create(
        name=pillar_data['name'],
        defaults={
            'pillar': pillar_data['pillar'],
            'description': pillar_data['description']
        }
    )
    categories[cat.pillar] = cat
    print(f"{'✅' if created else '📚'} Category: {cat.name}")

# Complete course list - African focused
courses_data = [
    # FOUNDATIONAL LITERACY (15 courses)
    {
        'title': 'Alphabet and Phonics - English',
        'category': categories['literacy'],
        'description': 'Master English alphabet, letter sounds, and phonics to begin reading confidently',
        'level': 'beginner', 'age_group': 'all', 'learning_approach': 'pedagogic', 'duration_hours': 15
    },
    {
        'title': 'Reading for Beginners - English',
        'category': categories['literacy'],
        'description': 'Learn to read English words, sentences, and simple stories with comprehension',
        'level': 'beginner', 'age_group': 'all', 'learning_approach': 'pedagogic', 'duration_hours': 20
    },
    {
        'title': 'Writing Skills - English',
        'category': categories['literacy'],
        'description': 'Develop clear handwriting, spelling, and sentence construction in English',
        'level': 'beginner', 'age_group': 'all', 'learning_approach': 'pedagogic', 'duration_hours': 18
    },
    {
        'title': 'Basic Numeracy - Numbers and Counting',
        'category': categories['literacy'],
        'description': 'Build foundational math - number recognition, counting, and basic operations',
        'level': 'beginner', 'age_group': 'all', 'learning_approach': 'pedagogic', 'duration_hours': 15
    },
    {
        'title': 'Addition and Subtraction Skills',
        'category': categories['literacy'],
        'description': 'Master addition and subtraction with real-world African market scenarios',
        'level': 'beginner', 'age_group': 'all', 'learning_approach': 'pedagogic', 'duration_hours': 12
    },
    {
        'title': 'Multiplication and Division Basics',
        'category': categories['literacy'],
        'description': 'Learn multiplication tables and division with practical applications',
        'level': 'intermediate', 'age_group': 'all', 'learning_approach': 'pedagogic', 'duration_hours': 14
    },
    {
        'title': 'Fractions and Decimals',
        'category': categories['literacy'],
        'description': 'Understand fractions, decimals, and percentages in everyday life',
        'level': 'intermediate', 'age_group': 'all', 'learning_approach': 'pedagogic', 'duration_hours': 15
    },
    {
        'title': 'Reading Comprehension and Vocabulary',
        'category': categories['literacy'],
        'description': 'Build vocabulary and understand written texts in English',
        'level': 'intermediate', 'age_group': 'all', 'learning_approach': 'pedagogic', 'duration_hours': 20
    },
    {
        'title': 'Grammar and Sentence Structure',
        'category': categories['literacy'],
        'description': 'Learn English grammar rules and construct correct sentences',
        'level': 'intermediate', 'age_group': 'all', 'learning_approach': 'pedagogic', 'duration_hours': 18
    },
    {
        'title': 'Advanced Reading and Critical Thinking',
        'category': categories['literacy'],
        'description': 'Analyze texts, identify main ideas, and develop critical thinking skills',
        'level': 'advanced', 'age_group': 'all', 'learning_approach': 'pedagogic', 'duration_hours': 20
    },
    {
        'title': 'Advanced Writing - Essays and Reports',
        'category': categories['literacy'],
        'description': 'Write structured essays, reports, and formal documents in English',
        'level': 'advanced', 'age_group': 'adult', 'learning_approach': 'pedagogic', 'duration_hours': 20
    },
    {
        'title': 'Financial Mathematics - African Context',
        'category': categories['literacy'],
        'description': 'Apply math to money - interest, profit, loss, and financial planning',
        'level': 'intermediate', 'age_group': 'adult', 'learning_approach': 'andragogic', 'duration_hours': 18
    },
    {
        'title': 'Numeracy for Marketplace Trading',
        'category': categories['literacy'],
        'description': 'Practical numeracy skills for African markets and small business',
        'level': 'intermediate', 'age_group': 'adult', 'learning_approach': 'andragogic', 'duration_hours': 15
    },
    {
        'title': 'Local Language Literacy - African Languages',
        'category': categories['literacy'],
        'description': 'Read and write in your local African language',
        'level': 'beginner', 'age_group': 'all', 'learning_approach': 'pedagogic', 'duration_hours': 20
    },
    {
        'title': 'English for Professional Communication',
        'category': categories['literacy'],
        'description': 'Develop professional English skills for work and business',
        'level': 'advanced', 'age_group': 'adult', 'learning_approach': 'andragogic', 'duration_hours': 22
    },

    # COMPUTER LITERACY (14 courses)
    {
        'title': 'Introduction to Computers',
        'category': categories['computer'],
        'description': 'Basic computer components, hardware, and operating systems',
        'level': 'beginner', 'age_group': 'all', 'learning_approach': 'andragogic', 'duration_hours': 15
    },
    {
        'title': 'Microsoft Windows Operating System',
        'category': categories['computer'],
        'description': 'Navigate Windows, manage files, and use system settings',
        'level': 'beginner', 'age_group': 'all', 'learning_approach': 'andragogic', 'duration_hours': 12
    },
    {
        'title': 'Microsoft Word - Document Creation',
        'category': categories['computer'],
        'description': 'Create professional documents, resumes, and letters with Word',
        'level': 'beginner', 'age_group': 'all', 'learning_approach': 'andragogic', 'duration_hours': 15
    },
    {
        'title': 'Microsoft Excel - Spreadsheets',
        'category': categories['computer'],
        'description': 'Master Excel for calculations, budgets, and data analysis',
        'level': 'intermediate', 'age_group': 'adult', 'learning_approach': 'andragogic', 'duration_hours': 20
    },
    {
        'title': 'Microsoft PowerPoint - Presentations',
        'category': categories['computer'],
        'description': 'Create impactful presentations for business and education',
        'level': 'intermediate', 'age_group': 'all', 'learning_approach': 'andragogic', 'duration_hours': 12
    },
    {
        'title': 'Internet and Email Basics',
        'category': categories['computer'],
        'description': 'Browse the web, use search engines, and manage email effectively',
        'level': 'beginner', 'age_group': 'all', 'learning_approach': 'andragogic', 'duration_hours': 12
    },
    {
        'title': 'Computer Hardware Repair',
        'category': categories['computer'],
        'description': 'Identify, install, and repair computer hardware components',
        'level': 'intermediate', 'age_group': 'adult', 'learning_approach': 'andragogic', 'duration_hours': 25
    },
    {
        'title': 'Computer Networking Basics',
        'category': categories['computer'],
        'description': 'Understand networks, IP addresses, and basic network setup',
        'level': 'intermediate', 'age_group': 'adult', 'learning_approach': 'andragogic', 'duration_hours': 20
    },
    {
        'title': 'Cybersecurity Fundamentals',
        'category': categories['computer'],
        'description': 'Protect computers from viruses, hackers, and online threats',
        'level': 'intermediate', 'age_group': 'adult', 'learning_approach': 'andragogic', 'duration_hours': 18
    },
    {
        'title': 'Introduction to Web Development',
        'category': categories['computer'],
        'description': 'Build basic websites with HTML, CSS, and JavaScript',
        'level': 'advanced', 'age_group': 'adult', 'learning_approach': 'andragogic', 'duration_hours': 30
    },
    {
        'title': 'Introduction to Drones and Robotics',
        'category': categories['computer'],
        'description': 'Understand drone technology, robotics basics, and African applications',
        'level': 'intermediate', 'age_group': 'adult', 'learning_approach': 'andragogic', 'duration_hours': 20
    },
    {
        'title': 'Artificial Intelligence Basics',
        'category': categories['computer'],
        'description': 'Introduction to AI, machine learning, and real-world applications',
        'level': 'advanced', 'age_group': 'adult', 'learning_approach': 'andragogic', 'duration_hours': 25
    },
    {
        'title': 'Data Entry and Management',
        'category': categories['computer'],
        'description': 'Master data entry skills using spreadsheets and databases',
        'level': 'beginner', 'age_group': 'adult', 'learning_approach': 'andragogic', 'duration_hours': 15
    },
    {
        'title': 'ICT for Business and Entrepreneurship',
        'category': categories['computer'],
        'description': 'Leverage technology for African business growth and innovation',
        'level': 'intermediate', 'age_group': 'adult', 'learning_approach': 'andragogic', 'duration_hours': 20
    },

    # VOCATIONAL TRADES (16 courses)
    {
        'title': 'Introduction to Carpentry',
        'category': categories['vocational'],
        'description': 'Learn woodworking - measurement, cutting, joining, and building furniture',
        'level': 'beginner', 'age_group': 'adult', 'learning_approach': 'andragogic', 'duration_hours': 30
    },
    {
        'title': 'Advanced Carpentry and Furniture Making',
        'category': categories['vocational'],
        'description': 'Master complex furniture, cabinet making, and finishing techniques',
        'level': 'advanced', 'age_group': 'adult', 'learning_approach': 'andragogic', 'duration_hours': 35
    },
    {
        'title': 'Introduction to Welding',
        'category': categories['vocational'],
        'description': 'Basic welding techniques, safety, and metalwork skills',
        'level': 'beginner', 'age_group': 'adult', 'learning_approach': 'andragogic', 'duration_hours': 30
    },
    {
        'title': 'Advanced Welding and Metal Fabrication',
        'category': categories['vocational'],
        'description': 'Master arc welding, MIG, TIG, and metal structure fabrication',
        'level': 'advanced', 'age_group': 'adult', 'learning_approach': 'andragogic', 'duration_hours': 35
    },
    {
        'title': 'Introduction to Plumbing',
        'category': categories['vocational'],
        'description': 'Learn plumbing basics - pipes, fittings, water systems, and repairs',
        'level': 'beginner', 'age_group': 'adult', 'learning_approach': 'andragogic', 'duration_hours': 25
    },
    {
        'title': 'Advanced Plumbing and Sanitation',
        'category': categories['vocational'],
        'description': 'Complex plumbing systems, water pumps, and sanitation solutions',
        'level': 'advanced', 'age_group': 'adult', 'learning_approach': 'andragogic', 'duration_hours': 30
    },
    {
        'title': 'Introduction to Masonry and Bricklaying',
        'category': categories['vocational'],
        'description': 'Learn bricklaying, concrete work, and building construction basics',
        'level': 'beginner', 'age_group': 'adult', 'learning_approach': 'andragogic', 'duration_hours': 25
    },
    {
        'title': 'Advanced Masonry and Construction',
        'category': categories['vocational'],
        'description': 'Master construction techniques, foundations, and building design',
        'level': 'advanced', 'age_group': 'adult', 'learning_approach': 'andragogic', 'duration_hours': 30
    },
    {
        'title': 'Introduction to Auto Mechanics',
        'category': categories['vocational'],
        'description': 'Basic vehicle maintenance, engine repair, and diagnostics',
        'level': 'beginner', 'age_group': 'adult', 'learning_approach': 'andragogic', 'duration_hours': 30
    },
    {
        'title': 'Advanced Auto Mechanics',
        'category': categories['vocational'],
        'description': 'Advanced engine repair, transmission, electrical systems, and diagnostics',
        'level': 'advanced', 'age_group': 'adult', 'learning_approach': 'andragogic', 'duration_hours': 40
    },
    {
        'title': 'Introduction to Tailoring and Fashion',
        'category': categories['vocational'],
        'description': 'Learn sewing, pattern making, and garment construction',
        'level': 'beginner', 'age_group': 'adult', 'learning_approach': 'andragogic', 'duration_hours': 25
    },
    {
        'title': 'Advanced Tailoring and Design',
        'category': categories['vocational'],
        'description': 'Master fashion design, embroidery, and African textile techniques',
        'level': 'advanced', 'age_group': 'adult', 'learning_approach': 'andragogic', 'duration_hours': 30
    },
    {
        'title': 'Introduction to Agriculture and Farming',
        'category': categories['vocational'],
        'description': 'Modern farming techniques, crop cultivation, and sustainable agriculture',
        'level': 'beginner', 'age_group': 'adult', 'learning_approach': 'andragogic', 'duration_hours': 25
    },
    {
        'title': 'Advanced Agriculture and Agribusiness',
        'category': categories['vocational'],
        'description': 'Agribusiness management, value addition, and agricultural innovation',
        'level': 'advanced', 'age_group': 'adult', 'learning_approach': 'andragogic', 'duration_hours': 30
    },
    {
        'title': 'Introduction to Electrical Installation',
        'category': categories['vocational'],
        'description': 'Basic electrical wiring, safety, and home installation',
        'level': 'beginner', 'age_group': 'adult', 'learning_approach': 'andragogic', 'duration_hours': 25
    },
    {
        'title': 'Advanced Electrical and Solar Installation',
        'category': categories['vocational'],
        'description': 'Master electrical systems, solar installations, and green energy',
        'level': 'advanced', 'age_group': 'adult', 'learning_approach': 'andragogic', 'duration_hours': 30
    },

    # CERTIFICATIONS (12 courses)
    {
        'title': 'CompTIA IT Fundamentals',
        'category': categories['certification'],
        'description': 'Earn CompTIA IT Fundamentals certification - start your IT career',
        'level': 'beginner', 'age_group': 'adult', 'learning_approach': 'andragogic', 'duration_hours': 30
    },
    {
        'title': 'CompTIA A+ Certification',
        'category': categories['certification'],
        'description': 'Complete CompTIA A+ certification for IT support professionals',
        'level': 'intermediate', 'age_group': 'adult', 'learning_approach': 'andragogic', 'duration_hours': 40
    },
    {
        'title': 'CompTIA Network+ Certification',
        'category': categories['certification'],
        'description': 'Network+ certification - networking concepts, infrastructure, and operations',
        'level': 'intermediate', 'age_group': 'adult', 'learning_approach': 'andragogic', 'duration_hours': 35
    },
    {
        'title': 'CompTIA Security+ Certification',
        'category': categories['certification'],
        'description': 'Security+ certification - cybersecurity fundamentals and practice',
        'level': 'advanced', 'age_group': 'adult', 'learning_approach': 'andragogic', 'duration_hours': 40
    },
    {
        'title': 'Ethical Hacking and Penetration Testing',
        'category': categories['certification'],
        'description': 'Ethical hacking skills and CEH certification preparation',
        'level': 'advanced', 'age_group': 'adult', 'learning_approach': 'andragogic', 'duration_hours': 45
    },
    {
        'title': 'CCTV Installation and Security Systems',
        'category': categories['certification'],
        'description': 'Install, configure, and maintain CCTV and security systems',
        'level': 'intermediate', 'age_group': 'adult', 'learning_approach': 'andragogic', 'duration_hours': 25
    },
    {
        'title': 'Drone Piloting and Maintenance',
        'category': categories['certification'],
        'description': 'Become a certified drone pilot - operation, maintenance, and safety',
        'level': 'intermediate', 'age_group': 'adult', 'learning_approach': 'andragogic', 'duration_hours': 30
    },
    {
        'title': 'AI and Robotics Certification',
        'category': categories['certification'],
        'description': 'Fundamentals of AI, robotics, and emerging technologies',
        'level': 'advanced', 'age_group': 'adult', 'learning_approach': 'andragogic', 'duration_hours': 35
    },
    {
        'title': 'Project Management Professional (PMP) Prep',
        'category': categories['certification'],
        'description': 'PMP certification preparation with real-world project examples',
        'level': 'advanced', 'age_group': 'adult', 'learning_approach': 'andragogic', 'duration_hours': 40
    },
    {
        'title': 'ICT Trainer Certification',
        'category': categories['certification'],
        'description': 'Become certified ICT trainer for community education',
        'level': 'intermediate', 'age_group': 'adult', 'learning_approach': 'andragogic', 'duration_hours': 30
    },
    {
        'title': 'Entrepreneurship and Business Certification',
        'category': categories['certification'],
        'description': 'Business management certification - start and grow your business',
        'level': 'intermediate', 'age_group': 'adult', 'learning_approach': 'andragogic', 'duration_hours': 25
    },
    {
        'title': 'International Digital Marketing Certification',
        'category': categories['certification'],
        'description': 'Digital marketing certification - SEO, social media, and online business',
        'level': 'intermediate', 'age_group': 'adult', 'learning_approach': 'andragogic', 'duration_hours': 25
    },

    # LIFE SKILLS (10 courses)
    {
        'title': 'Financial Literacy - Personal Finance',
        'category': categories['life_skills'],
        'description': 'Manage money, create budgets, and plan for financial freedom',
        'level': 'beginner', 'age_group': 'adult', 'learning_approach': 'andragogic', 'duration_hours': 15
    },
    {
        'title': 'Business Planning and Entrepreneurship',
        'category': categories['life_skills'],
        'description': 'Start, grow, and sustain a small business in Africa',
        'level': 'intermediate', 'age_group': 'adult', 'learning_approach': 'andragogic', 'duration_hours': 20
    },
    {
        'title': 'Emotional Intelligence and Mental Health',
        'category': categories['life_skills'],
        'description': 'Develop emotional intelligence, cope with stress, and build resilience',
        'level': 'beginner', 'age_group': 'all', 'learning_approach': 'andragogic', 'duration_hours': 15
    },
    {
        'title': 'Effective Communication Skills',
        'category': categories['life_skills'],
        'description': 'Master communication, public speaking, and interpersonal skills',
        'level': 'beginner', 'age_group': 'all', 'learning_approach': 'andragogic', 'duration_hours': 15
    },
    {
        'title': 'Leadership and Community Development',
        'category': categories['life_skills'],
        'description': 'Lead effectively, organize communities, and drive change',
        'level': 'intermediate', 'age_group': 'adult', 'learning_approach': 'andragogic', 'duration_hours': 18
    },
    {
        'title': 'Time Management and Productivity',
        'category': categories['life_skills'],
        'description': 'Manage time effectively, set goals, and increase productivity',
        'level': 'beginner', 'age_group': 'all', 'learning_approach': 'andragogic', 'duration_hours': 12
    },
    {
        'title': 'Critical Thinking and Problem Solving',
        'category': categories['life_skills'],
        'description': 'Analyze problems, think critically, and develop solutions',
        'level': 'intermediate', 'age_group': 'all', 'learning_approach': 'pedagogic', 'duration_hours': 15
    },
    {
        'title': 'Digital Literacy and Online Safety',
        'category': categories['life_skills'],
        'description': 'Stay safe online, manage privacy, and use digital resources wisely',
        'level': 'beginner', 'age_group': 'all', 'learning_approach': 'andragogic', 'duration_hours': 12
    },
    {
        'title': 'Environmental Awareness and Sustainability',
        'category': categories['life_skills'],
        'description': 'Understand environmental issues and promote sustainable practices',
        'level': 'intermediate', 'age_group': 'all', 'learning_approach': 'pedagogic', 'duration_hours': 15
    },
    {
        'title': 'Interviewing and Job Preparation Skills',
        'category': categories['life_skills'],
        'description': 'Prepare for job interviews, write CVs, and build professional networks',
        'level': 'intermediate', 'age_group': 'adult', 'learning_approach': 'andragogic', 'duration_hours': 12
    },

    # PRIMARY EDUCATION (7 courses)
    {
        'title': 'Primary English - Reading and Writing',
        'category': categories['primary'],
        'description': 'Complete primary English curriculum - literacy, grammar, and literature',
        'level': 'beginner', 'age_group': 'child', 'learning_approach': 'pedagogic', 'duration_hours': 40
    },
    {
        'title': 'Primary Mathematics - Complete Curriculum',
        'category': categories['primary'],
        'description': 'Complete primary math - numbers, operations, geometry, and measurements',
        'level': 'beginner', 'age_group': 'child', 'learning_approach': 'pedagogic', 'duration_hours': 40
    },
    {
        'title': 'Primary Science - Basic Concepts',
        'category': categories['primary'],
        'description': 'Primary science - life sciences, physical sciences, and earth sciences',
        'level': 'beginner', 'age_group': 'child', 'learning_approach': 'pedagogic', 'duration_hours': 35
    },
    {
        'title': 'Primary Social Studies - Africa',
        'category': categories['primary'],
        'description': 'Social studies with African focus - geography, history, and civics',
        'level': 'beginner', 'age_group': 'child', 'learning_approach': 'pedagogic', 'duration_hours': 30
    },
    {
        'title': 'Primary Health and Life Skills',
        'category': categories['primary'],
        'description': 'Personal health, hygiene, nutrition, and safety for children',
        'level': 'beginner', 'age_group': 'child', 'learning_approach': 'pedagogic', 'duration_hours': 25
    },
    {
        'title': 'Primary Art and Creative Skills',
        'category': categories['primary'],
        'description': 'Art, music, drama, and creative expression for primary learners',
        'level': 'beginner', 'age_group': 'child', 'learning_approach': 'pedagogic', 'duration_hours': 20
    },
    {
        'title': 'Primary Technology and ICT',
        'category': categories['primary'],
        'description': 'Introduction to technology and ICT for primary school learners',
        'level': 'beginner', 'age_group': 'child', 'learning_approach': 'pedagogic', 'duration_hours': 25
    },

    # SECONDARY EDUCATION (7 courses)
    {
        'title': 'Secondary English - Advanced Studies',
        'category': categories['secondary'],
        'description': 'Advanced English - literature, composition, and communication',
        'level': 'advanced', 'age_group': 'teen', 'learning_approach': 'pedagogic', 'duration_hours': 50
    },
    {
        'title': 'Secondary Mathematics - Advanced',
        'category': categories['secondary'],
        'description': 'Advanced math - algebra, geometry, trigonometry, and calculus',
        'level': 'advanced', 'age_group': 'teen', 'learning_approach': 'pedagogic', 'duration_hours': 50
    },
    {
        'title': 'Secondary Science - Biology and Chemistry',
        'category': categories['secondary'],
        'description': 'Comprehensive biology and chemistry for secondary learners',
        'level': 'advanced', 'age_group': 'teen', 'learning_approach': 'pedagogic', 'duration_hours': 45
    },
    {
        'title': 'Secondary Science - Physics',
        'category': categories['secondary'],
        'description': 'Advanced physics - mechanics, energy, waves, and modern physics',
        'level': 'advanced', 'age_group': 'teen', 'learning_approach': 'pedagogic', 'duration_hours': 45
    },
    {
        'title': 'Secondary Commerce and Business',
        'category': categories['secondary'],
        'description': 'Commerce, accounting, entrepreneurship, and business management',
        'level': 'intermediate', 'age_group': 'teen', 'learning_approach': 'pedagogic', 'duration_hours': 40
    },
    {
        'title': 'Secondary ICT and Computer Science',
        'category': categories['secondary'],
        'description': 'Computer science, programming, and ICT for secondary students',
        'level': 'intermediate', 'age_group': 'teen', 'learning_approach': 'pedagogic', 'duration_hours': 40
    },
    {
        'title': 'Secondary History and Geography - Africa',
        'category': categories['secondary'],
        'description': 'African history, geography, and contemporary issues',
        'level': 'intermediate', 'age_group': 'teen', 'learning_approach': 'pedagogic', 'duration_hours': 35
    },
]

# Add all courses
count = 0
for course_data in courses_data:
    course, created = Course.objects.get_or_create(
        title=course_data['title'],
        category=course_data['category'],
        defaults={
            'description': course_data['description'],
            'level': course_data['level'],
            'age_group': course_data['age_group'],
            'learning_approach': course_data['learning_approach'],
            'duration_hours': course_data['duration_hours'],
            'is_active': True
        }
    )
    if created:
        count += 1
        print(f"✅ Added: {course.title}")
    else:
        print(f"📚 Already exists: {course.title}")

print(f"\n" + "="*50)
print(f"🌍 African SkillsContinua Platform")
print(f"📊 Total Courses Added: {count}")
print(f"📚 Total Courses in Database: {Course.objects.count()}")
print(f"🏛️  Total Categories: {Category.objects.count()}")
print(f"🎯 Learning Pillars: {Category.objects.count()}")
print(f"🌍 Target: Africa and Developing Nations")
print("="*50)
print("\n💡 Next Steps:")
print("1. Run: python manage.py runserver")
print("2. Visit: http://127.0.0.1:8000")
print("3. Create lessons and course content")
print("4. Add multi-language support (French, Spanish, Portuguese, Swahili, Arabic)")