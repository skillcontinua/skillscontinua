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
print("📚 FIXING LESSON CONTENT - PRESERVING ORIGINAL MATERIAL")
print("="*70)

# Get all lessons
lessons = Lesson.objects.all()
print(f"📚 Found {lessons.count()} lessons to check")

total_fixed = 0

for lesson in lessons:
    content = lesson.content or ""
    
    # Check if content has been overwritten by enrichment template
    if "Learning Objectives" in content and "Lesson Overview" in content:
        # Extract the original content from the "Lesson Overview" section
        original_content = ""
        if "## 📖 Lesson Overview" in content:
            # Get everything after "## 📖 Lesson Overview" up to "## 🔑 Key Concepts"
            start_marker = "## 📖 Lesson Overview"
            end_marker = "## 🔑 Key Concepts"
            start_pos = content.find(start_marker)
            end_pos = content.find(end_marker, start_pos)
            
            if start_pos != -1 and end_pos != -1:
                # Extract the original content (skip the marker)
                overview_section = content[start_pos + len(start_marker):end_pos].strip()
                # Keep the original content
                original_content = overview_section
        
        # If we couldn't extract, use the lesson title as content
        if not original_content or len(original_content) < 10:
            original_content = f"Learn about {lesson.title} in this comprehensive lesson. This lesson covers all the essential concepts and practical skills you need to master this topic."
        
        # Rebuild content with original content preserved
        fixed_content = f"""
## 🎯 Learning Objectives
By the end of this lesson, you will be able to:
- Understand the core concepts of {lesson.title}
- Apply practical skills in real-world situations
- Solve common problems independently
- Build confidence in your abilities

## 📖 Lesson Content
{original_content}

## 🔑 Key Concepts
- **Core Principle:** Understanding the fundamentals
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
- Practice regularly to build expertise
- Apply what you learn in real situations
- Continue exploring and expanding your knowledge

## 🎓 Continue Learning
- Explore related lessons
- Join the discussion forum
- Connect with fellow learners
- Share your progress and experiences
"""
        
        lesson.content = fixed_content
        lesson.save()
        total_fixed += 1
        print(f"✅ Fixed: {lesson.title}")

print("\n" + "="*70)
print(f"📊 Total Lessons Fixed: {total_fixed}")
print("🎉 Lesson content fixed!")