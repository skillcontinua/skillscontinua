import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from courses.models import Course, Lesson

print("📚 Adding lessons to ALL courses without lessons...")

# Get all courses
all_courses = Course.objects.filter(is_active=True)
print(f"Found {all_courses.count()} courses")

# Comprehensive lessons data for all core courses
lessons_data = {
    # ===== PEDAGOGIC COURSES (Children) =====
    'Cognitive Development - Memory and Focus': [
        {'title': 'Introduction to Memory', 'content': 'Understanding what memory is and how it works in our brain. Fun introduction to the memory process.', 'order': 1, 'duration': 20},
        {'title': 'Memory Games - Visual Memory', 'content': 'Fun games to improve visual memory. Remember pictures, shapes, and patterns.', 'order': 2, 'duration': 25},
        {'title': 'Memory Games - Auditory Memory', 'content': 'Listen, remember, and repeat! Games to improve your listening and recall skills.', 'order': 3, 'duration': 25},
        {'title': 'Concentration Exercises', 'content': 'Exercises to improve focus and attention span. Learn to concentrate better.', 'order': 4, 'duration': 20},
        {'title': 'Brain Training Activities', 'content': 'Fun activities to challenge your brain and improve thinking speed.', 'order': 5, 'duration': 25},
        {'title': 'Learning Strategies for Kids', 'content': 'Tips and techniques to learn new things more easily and remember them longer.', 'order': 6, 'duration': 20},
    ],
    'Financial Literacy for Kids': [
        {'title': 'What is Money?', 'content': 'Learn about money - coins, notes, and what we use them for in daily life.', 'order': 1, 'duration': 20},
        {'title': 'How We Earn Money', 'content': 'Simple ways people earn money and why work is important.', 'order': 2, 'duration': 20},
        {'title': 'Saving Money - A Good Habit', 'content': 'Why saving money is important and how to save with a piggy bank.', 'order': 3, 'duration': 25},
        {'title': 'Smart Spending', 'content': 'Learn to make smart choices when spending money - needs vs wants.', 'order': 4, 'duration': 20},
        {'title': 'Giving and Sharing', 'content': 'Understanding the importance of sharing and helping others.', 'order': 5, 'duration': 20},
    ],
    'Communication Skills for Kids': [
        {'title': 'Speaking Clearly', 'content': 'How to speak clearly so others can understand you easily.', 'order': 1, 'duration': 20},
        {'title': 'Listening to Others', 'content': 'Learn to listen carefully when others are speaking.', 'order': 2, 'duration': 20},
        {'title': 'Using Kind Words', 'content': 'Understanding the power of kind words and good manners.', 'order': 3, 'duration': 20},
        {'title': 'Expressing Feelings', 'content': 'How to express your feelings in a healthy way.', 'order': 4, 'duration': 25},
        {'title': 'Making Friends', 'content': 'Tips for making friends and being a good friend.', 'order': 5, 'duration': 20},
    ],
    'Logic and Reasoning for Kids': [
        {'title': 'Fun Puzzles', 'content': 'Solve fun puzzles to develop logical thinking.', 'order': 1, 'duration': 20},
        {'title': 'Pattern Recognition', 'content': 'Learn to recognize patterns in numbers, shapes, and everyday life.', 'order': 2, 'duration': 25},
        {'title': 'Simple Deductions', 'content': 'Learn to make simple deductions and solve logic problems.', 'order': 3, 'duration': 25},
        {'title': 'Critical Thinking Games', 'content': 'Games that challenge you to think critically and solve problems.', 'order': 4, 'duration': 20},
        {'title': 'Decision Making for Kids', 'content': 'Learn to make good decisions by thinking through options.', 'order': 5, 'duration': 20},
    ],
    
    # ===== ANDRAGOGIC COURSES (Adults) =====
    'Financial Management for Adults': [
        {'title': 'Financial Goals and Planning', 'content': 'Setting financial goals and creating a roadmap to achieve them.', 'order': 1, 'duration': 30},
        {'title': 'Creating a Personal Budget', 'content': 'Step-by-step guide to tracking income and expenses.', 'order': 2, 'duration': 35},
        {'title': 'Emergency Fund and Savings', 'content': 'Building emergency savings and different saving strategies.', 'order': 3, 'duration': 25},
        {'title': 'Understanding and Managing Debt', 'content': 'Managing loans, credit cards, and avoiding debt traps.', 'order': 4, 'duration': 30},
        {'title': 'Investment Basics', 'content': 'Introduction to stocks, bonds, mutual funds, and building wealth.', 'order': 5, 'duration': 35},
        {'title': 'Retirement Planning', 'content': 'Planning for retirement and pension options.', 'order': 6, 'duration': 30},
        {'title': 'Small Business Finance', 'content': 'Managing finances for entrepreneurship and side businesses.', 'order': 7, 'duration': 35},
    ],
    'Advanced Communication Skills': [
        {'title': 'Principles of Communication', 'content': 'Understanding the fundamentals and importance of effective communication.', 'order': 1, 'duration': 25},
        {'title': 'Active Listening Skills', 'content': 'Mastering listening - the foundation of all communication.', 'order': 2, 'duration': 30},
        {'title': 'Public Speaking Mastery', 'content': 'Overcoming fear and speaking confidently to any audience.', 'order': 3, 'duration': 35},
        {'title': 'Non-Verbal Communication', 'content': 'Understanding body language, tone, and unspoken messages.', 'order': 4, 'duration': 25},
        {'title': 'Professional Writing Skills', 'content': 'Writing effective emails, reports, and business documents.', 'order': 5, 'duration': 30},
        {'title': 'Conflict Resolution', 'content': 'Managing and resolving conflicts professionally.', 'order': 6, 'duration': 30},
        {'title': 'Negotiation and Persuasion', 'content': 'Mastering negotiation and influencing skills.', 'order': 7, 'duration': 35},
    ],
    'Logic and Critical Thinking': [
        {'title': 'Introduction to Logical Thinking', 'content': 'Understanding logic and its importance in decision making.', 'order': 1, 'duration': 25},
        {'title': 'Identifying Arguments and Reasoning', 'content': 'Analyzing arguments and evaluating reasoning.', 'order': 2, 'duration': 30},
        {'title': 'Logical Fallacies', 'content': 'Recognizing common errors in reasoning.', 'order': 3, 'duration': 35},
        {'title': 'Deductive Reasoning', 'content': 'Using deductive logic to draw conclusions.', 'order': 4, 'duration': 30},
        {'title': 'Inductive Reasoning', 'content': 'Using evidence and patterns to make conclusions.', 'order': 5, 'duration': 30},
        {'title': 'Critical Thinking in Action', 'content': 'Applying critical thinking to real-world problems.', 'order': 6, 'duration': 35},
        {'title': 'Decision Making Frameworks', 'content': 'Structured approaches to making better decisions.', 'order': 7, 'duration': 35},
    ],
    'Cognitive Training for Adults': [
        {'title': 'Understanding Cognitive Abilities', 'content': 'Understanding memory, attention, and cognitive functions.', 'order': 1, 'duration': 25},
        {'title': 'Memory Enhancement Techniques', 'content': 'Proven techniques to improve memory and recall.', 'order': 2, 'duration': 30},
        {'title': 'Attention and Concentration Training', 'content': 'Exercises to improve focus and attention.', 'order': 3, 'duration': 30},
        {'title': 'Problem-Solving Skills', 'content': 'Developing effective problem-solving strategies.', 'order': 4, 'duration': 35},
        {'title': 'Brain Training Exercises', 'content': 'Daily exercises to keep your brain sharp and active.', 'order': 5, 'duration': 25},
        {'title': 'Learning How to Learn', 'content': 'Effective strategies for learning new skills quickly.', 'order': 6, 'duration': 30},
    ],
    'Qualitative and Quantitative Appraisal': [
        {'title': 'Introduction to Appraisal', 'content': 'Understanding qualitative and quantitative methods.', 'order': 1, 'duration': 30},
        {'title': 'Qualitative Research Methods', 'content': 'Interviews, focus groups, and observational methods.', 'order': 2, 'duration': 35},
        {'title': 'Quantitative Research Methods', 'content': 'Surveys, experiments, and statistical analysis.', 'order': 3, 'duration': 35},
        {'title': 'Data Collection Techniques', 'content': 'How to collect reliable and valid data.', 'order': 4, 'duration': 30},
        {'title': 'Data Analysis Skills', 'content': 'Analyzing data and drawing meaningful conclusions.', 'order': 5, 'duration': 35},
        {'title': 'Evidence-Based Decision Making', 'content': 'Using appraisal results for better decisions.', 'order': 6, 'duration': 30},
        {'title': 'Reporting and Presenting Findings', 'content': 'Communicating appraisal results effectively.', 'order': 7, 'duration': 35},
    ],
    
    # ===== HEUTAGOGIC COURSES (Advanced) =====
    'Advanced Financial Strategy': [
        {'title': 'Strategic Financial Planning', 'content': 'Advanced strategies for long-term financial success.', 'order': 1, 'duration': 35},
        {'title': 'Investment Portfolio Management', 'content': 'Building and managing a diversified investment portfolio.', 'order': 2, 'duration': 40},
        {'title': 'Risk Management and Insurance', 'content': 'Understanding and managing financial risks.', 'order': 3, 'duration': 35},
        {'title': 'Tax Planning and Optimization', 'content': 'Strategies for tax efficiency and optimization.', 'order': 4, 'duration': 35},
        {'title': 'Wealth Creation Strategies', 'content': 'Building sustainable wealth over time.', 'order': 5, 'duration': 40},
        {'title': 'Business and Investment Analysis', 'content': 'Advanced techniques for evaluating opportunities.', 'order': 6, 'duration': 35},
    ],
    'Strategic Communication and Leadership': [
        {'title': 'Strategic Communication in Leadership', 'content': 'Using communication as a strategic tool for leadership.', 'order': 1, 'duration': 30},
        {'title': 'Corporate and Organizational Communication', 'content': 'Understanding communication in organizations.', 'order': 2, 'duration': 35},
        {'title': 'Leadership Communication Strategies', 'content': 'Communicating as a leader to inspire and motivate.', 'order': 3, 'duration': 30},
        {'title': 'Crisis Communication', 'content': 'Managing communication during challenging situations.', 'order': 4, 'duration': 35},
        {'title': 'Building Communication Frameworks', 'content': 'Designing effective communication frameworks for teams.', 'order': 5, 'duration': 30},
    ],
    'Advanced Logic and Systems Thinking': [
        {'title': 'Systems Thinking Fundamentals', 'content': 'Understanding systems and their interconnections.', 'order': 1, 'duration': 30},
        {'title': 'Complex Problem Solving', 'content': 'Advanced techniques for solving complex problems.', 'order': 2, 'duration': 35},
        {'title': 'Logical Frameworks and Models', 'content': 'Building logical frameworks for analysis.', 'order': 3, 'duration': 30},
        {'title': 'Systems Analysis Techniques', 'content': 'Methods for analyzing and improving systems.', 'order': 4, 'duration': 35},
        {'title': 'Strategic Decision Making', 'content': 'Using systems thinking for strategic decisions.', 'order': 5, 'duration': 35},
    ],
    'Cognitive Enhancement and Neuroplasticity': [
        {'title': 'Understanding Neuroplasticity', 'content': 'How the brain adapts and changes through learning.', 'order': 1, 'duration': 30},
        {'title': 'Advanced Memory Systems', 'content': 'Advanced memory techniques and mnemonic strategies.', 'order': 2, 'duration': 35},
        {'title': 'Cognitive Performance Optimization', 'content': 'Techniques for optimizing brain performance.', 'order': 3, 'duration': 35},
        {'title': 'Learning Acceleration', 'content': 'Advanced methods for rapid skill acquisition.', 'order': 4, 'duration': 30},
        {'title': 'Brain Health and Wellness', 'content': 'Maintaining brain health for long-term performance.', 'order': 5, 'duration': 30},
    ],
    'Advanced Research and Appraisal Methods': [
        {'title': 'Advanced Research Design', 'content': 'Designing advanced research studies and experiments.', 'order': 1, 'duration': 35},
        {'title': 'Advanced Data Analysis', 'content': 'Advanced statistical methods and data interpretation.', 'order': 2, 'duration': 40},
        {'title': 'Mixed Methods Research', 'content': 'Combining qualitative and quantitative approaches.', 'order': 3, 'duration': 35},
        {'title': 'Research Ethics and Standards', 'content': 'Ethical considerations in research and appraisal.', 'order': 4, 'duration': 30},
        {'title': 'Publishing and Disseminating Research', 'content': 'Sharing research findings with the community.', 'order': 5, 'duration': 35},
    ],
}

# Add lessons to courses
total_added = 0
course_count = 0

for course_title, lessons in lessons_data.items():
    try:
        course = Course.objects.get(title=course_title)
        course_count += 1
        print(f"\n📖 Adding lessons to: {course_title}")
        
        for lesson_data in lessons:
            lesson, created = Lesson.objects.get_or_create(
                course=course,
                title=lesson_data['title'],
                defaults={
                    'content': lesson_data['content'],
                    'order': lesson_data['order'],
                    'duration_minutes': lesson_data['duration'],
                    'is_free_preview': True if lesson_data['order'] == 1 else False,
                }
            )
            if created:
                total_added += 1
                print(f"  ✅ Added: {lesson.title}")
            else:
                print(f"  📚 Already exists: {lesson.title}")
                
    except Course.DoesNotExist:
        print(f"⚠️ Course '{course_title}' not found - skipping")
    except Exception as e:
        print(f"⚠️ Error adding lessons to '{course_title}': {e}")

print(f"\n" + "="*50)
print(f"📊 Courses updated: {course_count}")
print(f"📊 Total Lessons Added: {total_added}")
print(f"📚 Total Lessons in Database: {Lesson.objects.count()}")

# Show summary
print("\n📊 Summary by learning approach:")
for approach in ['pedagogic', 'andragogic', 'heutagogic']:
    courses = Course.objects.filter(learning_approach=approach, is_active=True)
    for course in courses:
        lesson_count = course.lessons.count()
        if lesson_count > 0:
            print(f"  📖 {course.title} ({approach.upper()}): {lesson_count} lessons")

print("\n🎉 Lesson addition complete!")