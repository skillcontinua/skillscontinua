"""
RE-IMPORT SCRIPT FOR COURSES 307-314
Run this script to completely re-import courses 307-314 with correct data.
Save as: reimport_courses.py in C:\skillscontinua\
Run with: python reimport_courses.py
"""

import os
import sys
import django
from django.db import transaction
from django.core.cache import cache

# Set up Django environment
sys.path.append('C:\\skillscontinua')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skillscontinua.settings')
django.setup()

from courses.models import Course, Category, Lesson

# Define the 8 courses with complete data
COURSES_DATA = [
    {
        'id': 307,
        'title': 'Advanced AI and Machine Learning Applications',
        'level': 'intermediate',
        'age_group': 'adult',
        'learning_approach': 'andragogic',
        'duration_hours': 40,
        'featured': True,
        'description': 'Master artificial intelligence and machine learning with practical applications in Python, neural networks, deep learning, and real-world AI deployment across industries like healthcare, finance, and autonomous systems.',
        'learning_objectives': 'Master the fundamentals and advanced concepts of AI, including neural networks, deep learning, natural language processing, and reinforcement learning.',
        'lessons': [
            ('Introduction to Artificial Intelligence', 'This lesson introduces the fundamental concepts of AI, including its history, applications, and ethical considerations.', 1, True),
            ('Machine Learning Fundamentals', 'Learn the core principles of machine learning, including supervised, unsupervised, and reinforcement learning.', 2, False),
            ('Neural Networks and Deep Learning', 'Explore neural network architectures, backpropagation, and deep learning frameworks.', 3, False),
            ('Natural Language Processing', 'Understand NLP techniques, transformers, and large language models.', 4, False),
            ('Reinforcement Learning', 'Master RL algorithms, Q-learning, and practical AI applications.', 5, False),
        ]
    },
    {
        'id': 308,
        'title': 'Quantum Computing Fundamentals',
        'level': 'intermediate',
        'age_group': 'adult',
        'learning_approach': 'andragogic',
        'duration_hours': 40,
        'featured': True,
        'description': 'Explore the revolutionary field of quantum computing, covering qubits, quantum gates, superposition, entanglement, and practical algorithms that will transform computing power beyond classical limits.',
        'learning_objectives': 'Master quantum computing principles, algorithms, and applications, including quantum gates, superposition, entanglement, and quantum error correction.',
        'lessons': [
            ('Introduction to Quantum Computing', 'This lesson introduces the fundamental concepts of quantum computing, including qubits, superposition, and entanglement.', 1, True),
            ('Quantum Gates and Circuits', 'Learn about quantum gates, quantum circuits, and how they differ from classical computing.', 2, False),
            ('Quantum Algorithms', 'Explore Shor\'s algorithm, Grover\'s search, and other quantum algorithms.', 3, False),
            ('Quantum Error Correction', 'Understand techniques for protecting quantum information from decoherence.', 4, False),
            ('Quantum Computing Applications', 'Explore practical applications in cryptography, optimization, and simulation.', 5, False),
        ]
    },
    {
        'id': 309,
        'title': 'Biotechnology and Genetic Engineering',
        'level': 'intermediate',
        'age_group': 'adult',
        'learning_approach': 'andragogic',
        'duration_hours': 40,
        'featured': True,
        'description': 'Dive into biotechnology and genetic engineering, covering DNA manipulation, CRISPR technology, bioinformatics, and practical applications in medicine, agriculture, and environmental science.',
        'learning_objectives': 'Master biotechnology principles, genetic engineering techniques, CRISPR technology, and bioinformatics tools.',
        'lessons': [
            ('Introduction to Biotechnology', 'This lesson introduces the fundamental concepts of biotechnology and its applications.', 1, True),
            ('Genetic Engineering Techniques', 'Learn about DNA manipulation, gene editing, and CRISPR technology.', 2, False),
            ('Bioinformatics and Genomics', 'Explore DNA sequencing, genome analysis, and bioinformatics tools.', 3, False),
            ('Synthetic Biology', 'Understand synthetic gene circuits and biological engineering applications.', 4, False),
            ('Biopharmaceuticals', 'Explore biopharmaceutical development, vaccines, and therapeutic applications.', 5, False),
        ]
    },
    {
        'id': 310,
        'title': 'Renewable Energy Systems Engineering',
        'level': 'intermediate',
        'age_group': 'adult',
        'learning_approach': 'andragogic',
        'duration_hours': 40,
        'featured': True,
        'description': 'Master renewable energy systems including solar, wind, hydro, biomass, and geothermal energy. Learn system design, implementation, efficiency optimization, and sustainable energy management.',
        'learning_objectives': 'Master renewable energy technologies, system design, implementation, and efficiency optimization.',
        'lessons': [
            ('Introduction to Renewable Energy', 'This lesson introduces the fundamental concepts of renewable energy sources and their importance.', 1, True),
            ('Solar Energy Systems', 'Learn about photovoltaic technologies, solar system design, and installation.', 2, False),
            ('Wind Energy Technology', 'Explore wind turbine design, aerodynamics, and wind farm planning.', 3, False),
            ('Energy Storage Solutions', 'Understand battery technologies, storage systems, and grid integration.', 4, False),
            ('Smart Grid Technologies', 'Explore smart grid infrastructure and efficient power distribution.', 5, False),
        ]
    },
    {
        'id': 311,
        'title': 'Robotics and Automation Advanced',
        'level': 'intermediate',
        'age_group': 'adult',
        'learning_approach': 'andragogic',
        'duration_hours': 40,
        'featured': True,
        'description': 'Explore advanced robotics and automation covering robotic kinematics, control systems, machine vision, industrial automation, and applications in manufacturing, logistics, and service industries.',
        'learning_objectives': 'Master robotics principles, control systems, machine vision, and industrial automation.',
        'lessons': [
            ('Introduction to Robotics', 'This lesson introduces the fundamental concepts of robotics and automation.', 1, True),
            ('Robotic Kinematics and Dynamics', 'Learn about forward and inverse kinematics, dynamic modeling, and control strategies.', 2, False),
            ('Industrial Automation', 'Explore PLC programming, SCADA systems, and automated manufacturing processes.', 3, False),
            ('Computer Vision for Robotics', 'Understand object detection, image processing, and vision-guided robotics.', 4, False),
            ('Humanoid and Swarm Robotics', 'Explore bipedal locomotion, multi-robot systems, and swarm intelligence.', 5, False),
        ]
    },
    {
        'id': 312,
        'title': 'Space Technology and Exploration',
        'level': 'intermediate',
        'age_group': 'adult',
        'learning_approach': 'andragogic',
        'duration_hours': 40,
        'featured': True,
        'description': 'Discover space technology and exploration covering rocket science, satellite technology, space systems, orbital mechanics, and the future of human space exploration and colonization.',
        'learning_objectives': 'Master space technology, rocket science, satellite systems, and exploration principles.',
        'lessons': [
            ('Introduction to Space Technology', 'This lesson introduces the fundamental concepts of space technology and exploration.', 1, True),
            ('Rocket Propulsion Systems', 'Learn about rocket engines, propulsion systems, and space launch vehicles.', 2, False),
            ('Satellite Systems', 'Explore satellite design, orbit mechanics, and communication systems.', 3, False),
            ('Space Habitation', 'Understand space station design, life support, and human spaceflight.', 4, False),
            ('Deep Space Exploration', 'Explore interplanetary missions, navigation, and future challenges.', 5, False),
        ]
    },
    {
        'id': 313,
        'title': 'Virtual and Augmented Reality Development',
        'level': 'intermediate',
        'age_group': 'adult',
        'learning_approach': 'andragogic',
        'duration_hours': 40,
        'featured': True,
        'description': 'Learn virtual and augmented reality development covering 3D modeling, interactive experiences, game engines, and practical applications in education, healthcare, entertainment, and enterprise.',
        'learning_objectives': 'Master VR/AR development, 3D modeling, interactive experiences, and application development.',
        'lessons': [
            ('Introduction to VR/AR', 'This lesson introduces the fundamental concepts of virtual and augmented reality.', 1, True),
            ('3D Modeling and Design', 'Learn 3D modeling techniques and interactive design principles.', 2, False),
            ('Game Engine Development', 'Explore game engines, real-time rendering, and interactive experiences.', 3, False),
            ('Interaction Design', 'Understand user interaction, gesture recognition, and haptic feedback.', 4, False),
            ('VR/AR Applications', 'Explore practical applications in education, healthcare, and enterprise.', 5, False),
        ]
    },
    {
        'id': 314,
        'title': 'Nano Technology and Materials Science',
        'level': 'intermediate',
        'age_group': 'adult',
        'learning_approach': 'andragogic',
        'duration_hours': 40,
        'featured': True,
        'description': 'Explore nanotechnology and materials science covering nanomaterials, molecular engineering, surface science, and practical applications in medicine, electronics, energy, and manufacturing.',
        'learning_objectives': 'Master nanotechnology principles, materials science, molecular engineering, and applications.',
        'lessons': [
            ('Introduction to Nanotechnology', 'This lesson introduces the fundamental concepts of nanotechnology and materials science.', 1, True),
            ('Nanomaterials Synthesis', 'Learn about synthesis techniques, characterization, and quality control.', 2, False),
            ('Molecular Engineering', 'Explore design at the molecular level and self-assembly.', 3, False),
            ('Nano-Electronics', 'Understand nanoscale electronics, quantum dots, and semiconductor applications.', 4, False),
            ('Nano-Medicine', 'Explore drug delivery, diagnostics, and biomedical applications.', 5, False),
        ]
    }
]

def reimport_courses():
    """Main function to re-import all courses with correct data"""
    print("=" * 70)
    print("RE-IMPORTING COURSES 307-314 WITH COMPLETE DATA")
    print("=" * 70)
    
    # Clear cache first
    cache.clear()
    print("? Cache cleared\n")
    
    try:
        with transaction.atomic():
            # Get categories
            tech_category = Category.objects.get(id=11)
            print(f"? Found category: {tech_category.name} (ID: 11)\n")
            
            # Delete existing courses
            print("Deleting existing courses (307-314)...")
            deleted_count = Course.objects.filter(id__in=range(307, 315)).delete()
            print(f"? Deleted {deleted_count[0]} courses\n")
            
            # Create new courses
            print("Creating new courses with complete data...")
            created_courses = []
            
            for course_data in COURSES_DATA:
                # Create the course
                course = Course.objects.create(
                    id=course_data['id'],
                    title=course_data['title'],
                    category=tech_category,
                    level=course_data['level'],
                    age_group=course_data['age_group'],
                    learning_approach=course_data['learning_approach'],
                    duration_hours=course_data['duration_hours'],
                    featured=course_data['featured'],
                    description=course_data['description'],
                    learning_objectives=course_data['learning_objectives'],
                    is_active=True,
                )
                
                # Set all translations
                for lang in ['_en', '_fr', '_es', '_pt', '_sw', '_ar']:
                    setattr(course, f"title{lang}", course.title)
                    setattr(course, f"description{lang}", course.description)
                    setattr(course, f"learning_objectives{lang}", course.learning_objectives)
                course.save()
                
                # Add lessons
                for lesson_title, lesson_content, order, is_free in course_data['lessons']:
                    lesson = Lesson.objects.create(
                        course=course,
                        title=lesson_title,
                        content=lesson_content,
                        order=order,
                        duration_minutes=30,
                        is_free_preview=is_free,
                    )
                    # Set lesson translations
                    for lang in ['_en', '_fr', '_es', '_pt', '_sw', '_ar']:
                        setattr(lesson, f"title{lang}", lesson.title)
                        setattr(lesson, f"content{lang}", lesson.content)
                    lesson.save()
                
                created_courses.append(course)
                print(f"  ? Created course {course.id}: {course.title} with {len(course_data['lessons'])} lessons")
            
            # Verification
            print("\n" + "=" * 70)
            print("VERIFICATION")
            print("=" * 70)
            
            # Check category 11
            tech_courses = Category.objects.get(id=11).courses.all()
            print(f"\nCategory 11 ({tech_category.name}) has {tech_courses.count()} courses:")
            for course in tech_courses.order_by('id'):
                print(f"  - ID {course.id}: {course.title} (Lessons: {course.lessons.count()})")
            
            # Check course 314 specifically
            course_314 = Course.objects.get(id=314)
            print(f"\nCourse 314: {course_314.title}")
            print(f"  - Category: {course_314.category.name}")
            print(f"  - Level: {course_314.level}")
            print(f"  - Age Group: {course_314.age_group}")
            print(f"  - Duration: {course_314.duration_hours}h")
            print(f"  - Lessons: {course_314.lessons.count()}")
            print(f"  - Learning Objectives: {course_314.learning_objectives[:60]}...")
            
            print("\n" + "=" * 70)
            print("? RE-IMPORT COMPLETE!")
            print("=" * 70)
            
            # Instructions
            print("\n?? NEXT STEPS:")
            print("1. Restart your Django server: Ctrl+C then python manage.py runserver")
            print("2. Hard refresh your browser: Ctrl+Shift+R")
            print("3. Check Category 11: https://skillscontinua.com/courses/?category=11")
            print("4. Check Course 314: https://skillscontinua.com/courses/314/")
            print("5. Check Course 307: https://skillscontinua.com/courses/307/")
            
    except Exception as e:
        print(f"\n? ERROR: {e}")
        print("Transaction will roll back automatically")

if __name__ == "__main__":
    reimport_courses()