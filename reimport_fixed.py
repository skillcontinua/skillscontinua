"""
FIXED RE-IMPORT SCRIPT
Save as: reimport_fixed.py
Run with: python reimport_fixed.py
"""

import os
import sys
import django

# Set up Django environment - FIXED
sys.path.insert(0, 'C:\\skillscontinua')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from courses.models import Course, Category, Lesson
from django.db import transaction

COURSES_DATA = [
    {
        'id': 307,
        'title': 'Advanced AI and Machine Learning Applications',
        'level': 'intermediate',
        'age_group': 'adult',
        'learning_approach': 'andragogic',
        'duration_hours': 40,
        'featured': True,
        'description': 'Master AI and ML with practical Python, neural networks, deep learning, and real-world deployment in healthcare, finance, and autonomous systems. Hands-on labs included.',
        'learning_objectives': 'Build, train and deploy ML models. Master neural networks, NLP, transformers, and reinforcement learning with real datasets.',
        'lessons': [
            ('Introduction to Artificial Intelligence - History, Ethics, Real World Impact', 'Theory: What is AI vs ML vs DL, history from 1956, current applications in Nigeria (fintech, health). Ethics, bias, job impact. Practical: Identify 10 AI uses in your daily life in Aba. Real Scenario: Client wants to automate customer service. Common Mistakes: Confusing AI with automation.', 1, True),
            ('Machine Learning Fundamentals - Supervised, Unsupervised, Reinforcement', 'Theory: Types of ML, data labeling, training/test split, overfitting. Practical: Use scikit-learn to train first classifier on Iris dataset. Tools: Python, Jupyter, pandas. Assessment: Build spam detector.', 2, False),
            ('Neural Networks and Deep Learning - Build Your First Neural Net', 'Theory: Perceptron, backpropagation, activation functions. Practical: Build neural network from scratch in Python, then with TensorFlow. Real Scenario: Predict customer churn for MTN. Duration: 4 hours hands-on.', 3, False),
            ('Natural Language Processing - Chatbots and LLMs', 'Theory: Tokenization, embeddings, transformers, GPT architecture. Practical: Build FAQ chatbot for SkillsContinua using HuggingFace. Tools: Transformers library. Assessment: Deploy chatbot.', 4, False),
            ('Reinforcement Learning and Deployment - From Model to Production', 'Theory: Q-learning, reward systems. Practical: Train model to play game, then deploy model with FastAPI + Docker. Real Scenario: Optimize delivery routes in Aba. Final Project: End-to-end AI product.', 5, False),
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
        'description': 'Explore nanotechnology covering nanomaterials, molecular engineering, and applications in medicine, electronics, energy.',
        'learning_objectives': 'Master nanomaterials synthesis, characterization, and real applications.',
        'lessons': [
            ('Introduction to Nanotechnology - What is Nano and Why It Matters', 'Theory: Scale 1-100nm, surface area to volume, quantum effects. Practical: Calculate surface area changes. Real Scenario: Why nano-silver in water filters.', 1, True),
            ('Nanomaterials Synthesis - Lab Techniques', 'Theory: Top-down vs bottom-up, sol-gel, CVD. Practical: Simulate synthesis process, safety protocols. Tools: Gloves, fume hood, SEM.', 2, False),
            ('Molecular Engineering and Self-Assembly', 'Theory: Self-assembly, molecular machines. Practical: Design molecular structure using software.', 3, False),
            ('Nano-Electronics and Quantum Dots', 'Theory: Quantum dots, transistors at nano scale. Practical: Build simple circuit model.', 4, False),
            ('Nano-Medicine - Drug Delivery and Diagnostics', 'Theory: Targeted drug delivery, diagnostics. Real Scenario: Design nano-carrier for malaria drug in Nigeria. Assessment: Proposal paper.', 5, False),
        ]
    },
]

def reimport():
    print("="*70)
    print("RE-IMPORTING COURSES 307 & 314 WITH COMPREHENSIVE CONTENT")
    print("="*70)
    try:
        with transaction.atomic():
            cat = Category.objects.get(id=11)
            print(f"Found category: {cat.name}")

            print("Deleting 307-314 if exists...")
            Course.objects.filter(id__in=[307,314]).delete()

            for data in COURSES_DATA:
                course = Course.objects.create(
                    id=data['id'],
                    title=data['title'],
                    category=cat,
                    level=data['level'],
                    age_group=data['age_group'],
                    learning_approach=data['learning_approach'],
                    duration_hours=data['duration_hours'],
                    featured=data['featured'],
                    description=data['description'],
                    learning_objectives=data['learning_objectives'],
                    is_active=True,
                )
                print(f"Created course {course.id}: {course.title}")
                
                for title, content, order, is_free in data['lessons']:
                    Lesson.objects.create(
                        course=course,
                        title=title,
                        content=content,
                        order=order,
                        duration_minutes=60,
                        is_free_preview=is_free,
                    )
                print(f"  -> {len(data['lessons'])} comprehensive lessons added")
            print("SUCCESS! Courses restored with detailed real-life content")
    except Exception as e:
        print(f"ERROR: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    reimport()