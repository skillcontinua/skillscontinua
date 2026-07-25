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
print("📚 ENRICHING ARTS & WELLNESS LESSONS")
print("="*70)

# Get all lessons from Arts and Wellness categories
arts_lessons = Lesson.objects.filter(course__category__pillar='arts')
wellness_lessons = Lesson.objects.filter(course__category__pillar='wellness')

all_lessons = list(arts_lessons) + list(wellness_lessons)
print(f"📚 Found {len(all_lessons)} lessons to enrich")

total_enriched = 0

for lesson in all_lessons:
    content = lesson.content or ""
    
    if "Learning Objectives" in content or len(content) > 500:
        print(f"📚 {lesson.title}: Already enriched (skipping)")
        continue
    
    # Enrich the content
    enriched_content = f"""
## 🎯 Learning Objectives
By the end of this lesson, you will be able to:
- Understand the core concepts of {lesson.title}
- Apply practical skills in real-world situations
- Develop confidence in your creative abilities
- Create professional-quality work

## 📖 Lesson Overview
{content}

## 🔑 Key Concepts
- **Core Principle:** Understanding the fundamental concept
- **Practical Application:** How to apply what you've learned
- **Creative Expression:** Developing your unique style
- **Professional Standards:** Quality and excellence

## 🛠️ Practical Exercises
1. **Exercise 1:** Practice the basic techniques
2. **Exercise 2:** Create a sample work
3. **Exercise 3:** Refine and perfect your work

## 📚 Resources for Further Learning
- Recommended books and materials
- Online tutorials and videos
- Art communities and forums
- Professional organizations

## ✅ Knowledge Check
- Can you explain the key concepts?
- Can you apply the techniques?
- What questions do you still have?

## 📝 Key Takeaways
- Practice regularly to improve
- Learn from masters and peers
- Develop your unique style
- Keep exploring and creating

## 🎓 Continue Learning
- Explore advanced techniques
- Join art communities
- Share your work with others
- Never stop creating
"""

    lesson.content = enriched_content
    lesson.save()
    total_enriched += 1
    print(f"✅ Enriched: {lesson.title}")

print("\n" + "="*70)
print(f"📊 Total Lessons Enriched: {total_enriched}")
print("🎉 Arts & Wellness enrichment complete!")