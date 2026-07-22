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
print("📚 ENRICHING LESSON CONTENT QUALITY")
print("="*70)

# Content enrichment templates
enrichment_templates = {
    'introduction': """
## 🎯 Learning Objectives
By the end of this lesson, you will be able to:
- Understand the core concepts of {topic}
- Apply practical techniques in real-world scenarios
- Identify and solve common problems
- Build confidence in your skills

## 📖 Introduction
{content}

## 🔑 Key Concepts
- **Concept 1:** Understanding the fundamentals
- **Concept 2:** Practical application techniques
- **Concept 3:** Common challenges and solutions
- **Concept 4:** Best practices for success

## 🛠️ Practical Exercises
1. **Exercise 1:** Apply what you've learned to a real situation
2. **Exercise 2:** Practice the techniques covered
3. **Exercise 3:** Solve a practical problem

## 📚 Additional Resources
- Course materials and handouts
- Recommended reading and videos
- Online forums and communities
- Practice tools and templates

## ✅ Quick Check
- Have I understood the key concepts?
- Can I apply this in real life?
- What questions do I still have?

## 📝 Key Takeaways
- Takeaway 1: Remember this important point
- Takeaway 2: This will help you in your journey
- Takeaway 3: Practice makes perfect
""",

    'technical': """
## 🎯 Learning Objectives
- Master the technical concepts of {topic}
- Develop practical skills through hands-on practice
- Understand troubleshooting and problem-solving
- Build professional competence

## 📖 Technical Overview
{content}

## 🔧 Technical Details
- **Component 1:** Understanding the core technology
- **Component 2:** Installation and setup procedures
- **Component 3:** Configuration and optimization
- **Component 4:** Maintenance and troubleshooting

## 🛠️ Hands-On Practice
1. **Practice 1:** Setup and configuration
2. **Practice 2:** Operation and maintenance
3. **Practice 3:** Troubleshooting common issues
4. **Practice 4:** Optimization and improvement

## ⚠️ Safety and Precautions
- Always follow safety guidelines
- Use appropriate protective equipment
- Follow manufacturer instructions
- Know emergency procedures

## 📚 Reference Materials
- Technical documentation
- Manufacturer guides
- Industry standards
- Online tutorials and videos

## ✅ Knowledge Check
- Can you explain the key concepts?
- Can you perform the procedures?
- Can you solve common problems?
""",

    'practical': """
## 🎯 Learning Objectives
- Gain practical skills in {topic}
- Apply knowledge to real-world situations
- Build confidence through hands-on practice
- Develop problem-solving abilities

## 📖 Practical Overview
{content}

## 🛠️ Step-by-Step Guide
1. **Step 1:** Preparation and setup
2. **Step 2:** Executing the task
3. **Step 3:** Quality checks and verification
4. **Step 4:** Completion and documentation

## 💡 Tips and Best Practices
- **Tip 1:** Work systematically
- **Tip 2:** Check your work regularly
- **Tip 3:** Ask for help when needed
- **Tip 4:** Document your progress

## ⚡ Common Challenges
- Challenge 1: How to overcome common obstacles
- Challenge 2: Dealing with unexpected situations
- Challenge 3: Maintaining quality standards

## 📋 Practical Exercise
Follow these steps to practice what you've learned:
1. Gather the necessary materials
2. Follow the step-by-step guide
3. Check your work against the checklist
4. Document your results and reflections

## 📚 Resources for Further Learning
- Additional reading materials
- Video tutorials and demonstrations
- Practice exercises and assignments
- Community forums and support
""",
}

# Get all lessons
lessons = Lesson.objects.all()
print(f"📚 Found {lessons.count()} lessons to enrich")

total_enriched = 0

for lesson in lessons:
    # Determine which template to use based on lesson title and content
    content = lesson.content or ""
    title = lesson.title or ""
    
    # Check if content needs enrichment (is it too short or missing structure)
    if len(content) > 500:
        print(f"📚 {lesson.title}: Already detailed (skipping)")
        continue
    
    # Choose template based on keywords
    if any(word in title.lower() for word in ['technical', 'installation', 'repair', 'maintenance', 'diagnostic', 'engineering']):
        template = enrichment_templates['technical']
    elif any(word in title.lower() for word in ['exercise', 'practice', 'project', 'skill', 'application']):
        template = enrichment_templates['practical']
    else:
        template = enrichment_templates['introduction']
    
    # Enrich the content
    enriched_content = template.format(topic=title, content=content if content else "This lesson covers essential concepts and practical skills.")
    
    # Add a section for further learning
    enriched_content += """
## 🎓 Further Learning
### Explore More
- Check out related lessons
- Join the discussion forums
- Connect with fellow learners
- Share your projects and experiences

### Continue Your Journey
- **Next Lesson:** [Link to next lesson]
- **Related Courses:** [Link to related courses]
- **Advanced Topics:** [Link to advanced materials]

### Stay Connected
- Follow us on social media
- Join our learning community
- Subscribe to updates
- Share your success stories
"""

    lesson.content = enriched_content
    lesson.save()
    total_enriched += 1
    print(f"✅ Enriched: {lesson.title}")

print("\n" + "="*70)
print(f"📊 Total Lessons Enriched: {total_enriched}")
print("🎉 Content enrichment complete!")