import os
import sys
import django
import csv

# Add project root to path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from courses.models import Course

print("📤 Exporting course titles for manual translation...")

# Export course titles to CSV
with open('course_titles.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['ID', 'English Title', 'French', 'Spanish', 'Portuguese', 'Swahili', 'Arabic'])
    
    for course in Course.objects.filter(is_active=True)[:50]:
        writer.writerow([
            course.id,
            course.title,
            '',  # French
            '',  # Spanish
            '',  # Portuguese
            '',  # Swahili
            ''   # Arabic
        ])

print("✅ Exported 50 courses to 'course_titles.csv'")
print("📝 Open the CSV file in Excel or Google Sheets")
print("🌍 Use Google Translate to fill in the translation columns")
print("📥 After filling, we can import the translations back")