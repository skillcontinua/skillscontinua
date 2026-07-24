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
print("📚 ADDING LESSONS TO TECHNOLOGY COURSES")
print("="*70)

tech_lessons = {
    'Blockchain Technology - Complete Guide': [
        {'title': 'Introduction to Blockchain', 'content': 'What is blockchain? History, evolution, and the revolutionary impact of blockchain technology.', 'order': 1, 'duration': 30},
        {'title': 'How Blockchain Works', 'content': 'Blockchain fundamentals - blocks, chains, hashing, consensus mechanisms, and distributed ledgers.', 'order': 2, 'duration': 35},
        {'title': 'Blockchain Types', 'content': 'Public, private, and consortium blockchains. Comparing different blockchain platforms.', 'order': 3, 'duration': 30},
        {'title': 'Cryptocurrency Basics', 'content': 'Cryptocurrency - Bitcoin, Ethereum, and other digital currencies. Wallets, transactions, and security.', 'order': 4, 'duration': 30},
        {'title': 'Smart Contracts', 'content': 'Smart contracts - creation, deployment, and management on blockchain platforms.', 'order': 5, 'duration': 35},
        {'title': 'Decentralized Applications (DApps)', 'content': 'DApps - development, deployment, and use of decentralized applications.', 'order': 6, 'duration': 30},
        {'title': 'Blockchain Security', 'content': 'Blockchain security - cryptography, consensus, and protecting blockchain systems.', 'order': 7, 'duration': 25},
        {'title': 'Blockchain in Business', 'content': 'Blockchain applications in business - supply chain, finance, healthcare, and government.', 'order': 8, 'duration': 30},
        {'title': 'Blockchain Development Tools', 'content': 'Blockchain development - Solidity, Ethereum, Hyperledger, and development tools.', 'order': 9, 'duration': 35},
        {'title': 'Future of Blockchain', 'content': 'Emerging trends - DeFi, NFTs, Web3, and the future of blockchain technology.', 'order': 10, 'duration': 25},
    ],
    'Artificial Intelligence Fundamentals': [
        {'title': 'Introduction to AI', 'content': 'What is AI? History, evolution, and the impact of artificial intelligence.', 'order': 1, 'duration': 30},
        {'title': 'AI Types and Approaches', 'content': 'Types of AI - narrow AI, general AI, and superintelligence. Different approaches to AI.', 'order': 2, 'duration': 30},
        {'title': 'Machine Learning Basics', 'content': 'Machine learning - supervised, unsupervised, and reinforcement learning.', 'order': 3, 'duration': 35},
        {'title': 'Deep Learning Fundamentals', 'content': 'Deep learning - neural networks, architectures, and applications.', 'order': 4, 'duration': 35},
        {'title': 'Natural Language Processing', 'content': 'NLP - text processing, sentiment analysis, and language models.', 'order': 5, 'duration': 30},
        {'title': 'Computer Vision', 'content': 'Computer vision - image recognition, object detection, and vision applications.', 'order': 6, 'duration': 30},
        {'title': 'AI Applications', 'content': 'AI applications - healthcare, finance, transportation, and education.', 'order': 7, 'duration': 25},
        {'title': 'AI Ethics and Bias', 'content': 'AI ethics - bias, fairness, transparency, and responsible AI development.', 'order': 8, 'duration': 25},
        {'title': 'AI Development Tools', 'content': 'AI tools - TensorFlow, PyTorch, and AI development platforms.', 'order': 9, 'duration': 35},
        {'title': 'Future of AI', 'content': 'Emerging trends - AGI, AI safety, and the future of artificial intelligence.', 'order': 10, 'duration': 30},
    ],
    'ChatGPT and Generative AI': [
        {'title': 'Introduction to Generative AI', 'content': 'What is generative AI? History, evolution, and impact on content creation.', 'order': 1, 'duration': 30},
        {'title': 'ChatGPT and LLMs', 'content': 'ChatGPT - how it works, capabilities, and limitations of large language models.', 'order': 2, 'duration': 35},
        {'title': 'Prompt Engineering', 'content': 'Prompt engineering - techniques for getting the best results from AI models.', 'order': 3, 'duration': 30},
        {'title': 'Content Creation with AI', 'content': 'Creating content - writing, images, video, and audio with generative AI.', 'order': 4, 'duration': 35},
        {'title': 'AI for Business', 'content': 'Using AI in business - automation, customer service, and productivity.', 'order': 5, 'duration': 30},
        {'title': 'AI for Education', 'content': 'Using AI in education - personalized learning, tutoring, and educational content.', 'order': 6, 'duration': 25},
        {'title': 'AI Ethics and Safety', 'content': 'AI safety - risks, ethics, and responsible use of generative AI.', 'order': 7, 'duration': 25},
        {'title': 'AI Tools and Platforms', 'content': 'AI platforms - ChatGPT, Claude, Gemini, and other AI tools.', 'order': 8, 'duration': 30},
        {'title': 'Building AI Applications', 'content': 'Building applications with AI - APIs, integrations, and custom solutions.', 'order': 9, 'duration': 35},
        {'title': 'Future of Generative AI', 'content': 'Emerging trends - multi-modal AI, agentic AI, and the future of generative technology.', 'order': 10, 'duration': 30},
    ],
}

# Add lessons
total_added = 0
total_courses = 0

for course_title, lessons in tech_lessons.items():
    try:
        course = Course.objects.get(title=course_title)
        print(f"\n📖 Adding lessons to: {course_title}")
        course_count = 0
        
        for lesson_info in lessons:
            exists = Lesson.objects.filter(course=course, title=lesson_info['title']).exists()
            if not exists:
                lesson = Lesson.objects.create(
                    course=course,
                    title=lesson_info['title'],
                    content=lesson_info['content'],
                    order=lesson_info['order'],
                    duration_minutes=lesson_info['duration'],
                    is_free_preview=True if lesson_info['order'] == 1 else False,
                )
                course_count += 1
                total_added += 1
                print(f"  ✅ Added: {lesson.title}")
        
        if course_count > 0:
            total_courses += 1
            print(f"  📊 Added {course_count} lessons to {course_title}")
            
    except Course.DoesNotExist:
        print(f"⚠️ Course '{course_title}' not found - skipping")

print("\n" + "="*70)
print(f"📊 Courses Updated: {total_courses}")
print(f"📚 Total Lessons Added: {total_added}")
print(f"📚 Total Lessons in Database: {Lesson.objects.count()}")
print("🎉 Technology lesson addition complete!")