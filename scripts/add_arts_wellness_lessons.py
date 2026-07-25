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
print("📚 ADDING LESSONS TO ARTS & WELLNESS COURSES")
print("="*70)

# Lesson content for Arts courses
arts_lessons = {
    'Sculpture - Complete Guide': [
        {'title': 'Introduction to Sculpture', 'content': 'What is sculpture? History, evolution, materials, and the art of three-dimensional expression.', 'order': 1, 'duration': 30},
        {'title': 'Sculpture Materials and Tools', 'content': 'Materials for sculpture - clay, stone, wood, metal, and modern materials. Tools and equipment for sculpting.', 'order': 2, 'duration': 35},
        {'title': 'Clay Modeling Techniques', 'content': 'Working with clay - modeling, carving, adding, and finishing techniques for clay sculptures.', 'order': 3, 'duration': 35},
        {'title': 'Stone Carving Fundamentals', 'content': 'Stone carving - selecting stone, tools, carving techniques, and creating stone sculptures.', 'order': 4, 'duration': 40},
        {'title': 'Wood Carving Techniques', 'content': 'Wood carving - wood selection, carving tools, techniques, and creating wooden sculptures.', 'order': 5, 'duration': 35},
        {'title': 'Metal Sculpture', 'content': 'Metal sculpture - welding, forging, fabrication, and creating metal artworks.', 'order': 6, 'duration': 35},
        {'title': 'Mold Making and Casting', 'content': 'Creating molds and casting sculptures - plaster, silicone, bronze, and resin casting.', 'order': 7, 'duration': 30},
        {'title': 'Sculpture Finishing', 'content': 'Finishing sculptures - polishing, painting, patination, and protecting finished works.', 'order': 8, 'duration': 25},
        {'title': 'Sculpture Display and Installation', 'content': 'Displaying and installing sculptures - indoor, outdoor, lighting, and exhibition considerations.', 'order': 9, 'duration': 25},
        {'title': 'Professional Sculpture Practice', 'content': 'Building a career in sculpture - commissions, galleries, pricing, and marketing.', 'order': 10, 'duration': 30},
    ],
    'Painting - Complete Guide': [
        {'title': 'Introduction to Painting', 'content': 'What is painting? History, evolution, and the art of visual expression.', 'order': 1, 'duration': 30},
        {'title': 'Oil Painting Techniques', 'content': 'Oil painting - materials, techniques, glazing, impasto, and oil painting methods.', 'order': 2, 'duration': 35},
        {'title': 'Acrylic Painting', 'content': 'Acrylic painting - materials, techniques, and modern acrylic painting methods.', 'order': 3, 'duration': 30},
        {'title': 'Watercolor Painting', 'content': 'Watercolor painting - materials, techniques, washes, and watercolor methods.', 'order': 4, 'duration': 30},
        {'title': 'Color Theory for Artists', 'content': 'Color theory - color wheel, color mixing, color harmony, and using color effectively.', 'order': 5, 'duration': 30},
        {'title': 'Composition and Design', 'content': 'Composition in painting - arranging elements, creating visual interest, and design principles.', 'order': 6, 'duration': 25},
        {'title': 'Still Life Painting', 'content': 'Still life painting - setup, composition, and painting still life subjects.', 'order': 7, 'duration': 25},
        {'title': 'Portrait Painting', 'content': 'Portrait painting - anatomy, proportion, capturing likeness, and painting portraits.', 'order': 8, 'duration': 30},
        {'title': 'Landscape Painting', 'content': 'Landscape painting - outdoor painting, capturing light, and landscape techniques.', 'order': 9, 'duration': 25},
        {'title': 'Professional Painting Career', 'content': 'Building a career in painting - commissions, galleries, pricing, and marketing.', 'order': 10, 'duration': 30},
    ],
}

# Lesson content for Wellness courses
wellness_lessons = {
    'Tai Chi - Complete Guide': [
        {'title': 'Introduction to Tai Chi', 'content': 'What is Tai Chi? History, philosophy, health benefits, and the art of moving meditation.', 'order': 1, 'duration': 30},
        {'title': 'Tai Chi Principles', 'content': 'Core principles of Tai Chi - posture, breathing, relaxation, and mindful movement.', 'order': 2, 'duration': 30},
        {'title': 'Tai Chi Warm-up Exercises', 'content': 'Warm-up exercises - joint loosening, stretching, and preparing the body for Tai Chi.', 'order': 3, 'duration': 25},
        {'title': 'Tai Chi Basic Movements', 'content': 'Basic Tai Chi movements - foundational postures and transitions.', 'order': 4, 'duration': 30},
        {'title': 'Tai Chi Qigong', 'content': 'Qigong - energy cultivation, breathing techniques, and health exercises.', 'order': 5, 'duration': 25},
        {'title': 'Tai Chi Form - Beginner Level', 'content': 'Learning the beginner Tai Chi form - step-by-step instruction.', 'order': 6, 'duration': 30},
        {'title': 'Tai Chi Form - Intermediate Level', 'content': 'Intermediate Tai Chi form - more complex movements and transitions.', 'order': 7, 'duration': 30},
        {'title': 'Tai Chi for Health', 'content': 'Tai Chi for specific health conditions - arthritis, balance, stress, and general wellness.', 'order': 8, 'duration': 25},
        {'title': 'Tai Chi Meditation', 'content': 'Meditation in Tai Chi - mindfulness, standing meditation, and moving meditation.', 'order': 9, 'duration': 25},
        {'title': 'Tai Chi Practice and Lifestyle', 'content': 'Daily Tai Chi practice - integrating Tai Chi into your lifestyle and continuing development.', 'order': 10, 'duration': 25},
    ],
    'Yoga - Complete Guide': [
        {'title': 'Introduction to Yoga', 'content': 'What is yoga? History, philosophy, and the science of yoga.', 'order': 1, 'duration': 30},
        {'title': 'Yoga Breathing Techniques', 'content': 'Yoga breathing - pranayama techniques, breath control, and breath awareness.', 'order': 2, 'duration': 25},
        {'title': 'Yoga Postures - Beginner', 'content': 'Basic yoga postures - standing, seated, and balancing postures for beginners.', 'order': 3, 'duration': 30},
        {'title': 'Yoga Postures - Intermediate', 'content': 'Intermediate yoga postures - more complex asanas and flows.', 'order': 4, 'duration': 30},
        {'title': 'Yoga Postures - Advanced', 'content': 'Advanced yoga postures - challenging asanas and advanced practices.', 'order': 5, 'duration': 30},
        {'title': 'Yoga for Health', 'content': 'Yoga for specific health conditions - back pain, stress, anxiety, and overall wellness.', 'order': 6, 'duration': 25},
        {'title': 'Yoga Meditation', 'content': 'Meditation in yoga - concentration, mindfulness, and meditation practices.', 'order': 7, 'duration': 25},
        {'title': 'Yoga Philosophy', 'content': 'Yoga philosophy - the eight limbs of yoga, sutras, and philosophical foundations.', 'order': 8, 'duration': 30},
        {'title': 'Yoga Teaching and Practice', 'content': 'Teaching yoga - becoming a yoga teacher, class planning, and professional practice.', 'order': 9, 'duration': 30},
        {'title': 'Yoga Lifestyle', 'content': 'Integrating yoga into daily life - diet, ethics, and holistic living.', 'order': 10, 'duration': 25},
    ],
    'Meditation and Mindfulness': [
        {'title': 'Introduction to Meditation', 'content': 'What is meditation? History, techniques, and the science of meditation.', 'order': 1, 'duration': 30},
        {'title': 'Basic Meditation Techniques', 'content': 'Basic meditation - breath awareness, body scan, and concentration techniques.', 'order': 2, 'duration': 25},
        {'title': 'Mindfulness Practice', 'content': 'Mindfulness - present moment awareness, everyday mindfulness, and mindful living.', 'order': 3, 'duration': 25},
        {'title': 'Guided Meditation', 'content': 'Guided meditation - visualization, loving-kindness, and guided practices.', 'order': 4, 'duration': 25},
        {'title': 'Meditation for Stress Relief', 'content': 'Meditation for stress - techniques, practices, and stress reduction.', 'order': 5, 'duration': 25},
        {'title': 'Meditation for Anxiety', 'content': 'Meditation for anxiety - calming the mind and managing anxious thoughts.', 'order': 6, 'duration': 25},
        {'title': 'Meditation for Sleep', 'content': 'Meditation for sleep - relaxation, sleep practices, and insomnia relief.', 'order': 7, 'duration': 20},
        {'title': 'Meditation and Science', 'content': 'The science of meditation - research, benefits, and evidence-based practices.', 'order': 8, 'duration': 25},
        {'title': 'Creating a Meditation Practice', 'content': 'Building a meditation practice - consistency, challenges, and long-term practice.', 'order': 9, 'duration': 25},
        {'title': 'Meditation and Spirituality', 'content': 'Meditation and spirituality - exploring the deeper dimensions of meditation.', 'order': 10, 'duration': 25},
    ],
}

# Add lessons
total_added = 0
total_courses = 0

for course_title, lessons in arts_lessons.items():
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

for course_title, lessons in wellness_lessons.items():
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
print("🎉 Arts & Wellness lesson addition complete!")