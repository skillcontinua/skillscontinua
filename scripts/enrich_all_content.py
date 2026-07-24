import os
import sys
import django

# Add project root to path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from courses.models import Lesson

print("="*70)
print("📚 ENRICHING ALL LESSON CONTENT")
print("="*70)

# Get all lessons
lessons = Lesson.objects.all()
print(f"📚 Found {lessons.count()} lessons to enrich")

total_enriched = 0

for lesson in lessons:
    content = lesson.content or ""
    
    # Check if content already has structure (enriched)
    if "Learning Objectives" in content or len(content) > 500:
        print(f"📚 {lesson.title}: Already enriched (skipping)")
        continue
    
    # Enrich the content
    enriched_content = f"""
## 🎯 Learning Objectives
By the end of this lesson, you will be able to:
- Understand the core concepts of {lesson.title}
- Apply practical skills in real-world situations
- Solve common problems independently
- Build confidence in your abilities

## 📖 Lesson Overview
{content}

## 🔑 Key Concepts
- **Core Principle:** Understanding the fundamental concept
- **Practical Application:** How to apply what you've learned
- **Common Challenges:** Anticipating and overcoming obstacles
- **Best Practices:** Professional approaches and techniques

## 🛠️ Practical Exercises
1. **Exercise 1:** Apply the concept to a real situation
2. **Exercise 2:** Practice the skills learned
3. **Exercise 3:** Solve a practical problem

## 📚 Resources for Further Learning
- Course materials and handouts
- Recommended reading and videos
- Online communities and forums
- Additional practice exercises

## ✅ Knowledge Check
- Can you explain the key concepts?
- Can you apply what you've learned?
- What questions do you still have?

## 📝 Key Takeaways
- Takeaway 1: Remember this important point
- Takeaway 2: This will help you in your journey
- Takeaway 3: Practice makes perfect

## 🎓 Continue Learning
- Explore related lessons
- Join the discussion forum
- Connect with fellow learners
- Share your progress and experiences
"""

    lesson.content = enriched_content
    lesson.save()
    total_enriched += 1
    print(f"✅ Enriched: {lesson.title}")

print("\n" + "="*70)
print(f"📊 Total Lessons Enriched: {total_enriched}")
print("🎉 Content enrichment complete!")