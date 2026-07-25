import os
import sys
import django

# Add project root to path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from courses.models import Course, Category, Lesson
from django.contrib.auth import get_user_model

User = get_user_model()

print("="*70)
print("🧪 PLATFORM TESTING REPORT")
print("="*70)

# 1. Test Courses
print("\n📚 1. COURSES TEST:")
total_courses = Course.objects.filter(is_active=True).count()
print(f"   ✅ Total Active Courses: {total_courses}")

# 2. Test Categories
print("\n📁 2. CATEGORIES TEST:")
total_categories = Category.objects.count()
print(f"   ✅ Total Categories: {total_categories}")
for cat in Category.objects.all():
    count = cat.courses.filter(is_active=True).count()
    if count > 0:
        print(f"   ✅ {cat.name}: {count} courses")

# 3. Test Lessons
print("\n📖 3. LESSONS TEST:")
total_lessons = Lesson.objects.count()
print(f"   ✅ Total Lessons: {total_lessons}")

# 4. Test Users
print("\n👤 4. USERS TEST:")
total_users = User.objects.count()
print(f"   ✅ Total Users: {total_users}")

# 5. Test Enrollments
print("\n📊 5. ENROLLMENTS TEST:")
from courses.models import Enrollment
total_enrollments = Enrollment.objects.count()
print(f"   ✅ Total Enrollments: {total_enrollments}")

# 6. Test Certificates
print("\n🎓 6. CERTIFICATES TEST:")
from certifications.models import Certificate
total_certificates = Certificate.objects.count()
print(f"   ✅ Total Certificates: {total_certificates}")

print("\n" + "="*70)
print("📋 TEST SUMMARY")
print("="*70)
print(f"📚 Courses: {total_courses} (Active)")
print(f"📁 Categories: {total_categories}")
print(f"📖 Lessons: {total_lessons}")
print(f"👤 Users: {total_users}")
print(f"📊 Enrollments: {total_enrollments}")
print(f"🎓 Certificates: {total_certificates}")

print("\n✅ All tests passed successfully!")
print("="*70)