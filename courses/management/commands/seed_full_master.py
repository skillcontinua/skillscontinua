# C:\skillscontinua\courses\management\commands\seed_full_master.py
import json
import os
from django.core.management.base import BaseCommand
from django.db import transaction
from courses.models import Category, Course, Lesson

class Command(BaseCommand):
    help = 'Seeds all courses and lessons from full_courses_export.json into the database.'

    def handle(self, *args, **options):
        json_path = os.path.join('full_courses_export.json')
        if not os.path.exists(json_path):
            self.stdout.write(self.style.ERROR(f"Export file not found at {json_path}"))
            return

        self.stdout.write("Loading full course catalog from JSON...")
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        with transaction.atomic():
            # 1. Ensure categories/pillars
            categories = {}
            for cat_data in data.get('categories', []):
                cat, _ = Category.objects.get_or_create(
                    pillar=cat_data['pillar'],
                    defaults={
                        'name': cat_data['name'],
                        'icon': cat_data.get('icon', '📚'),
                        'description': cat_data.get('description', '')
                    }
                )
                categories[cat_data['pillar']] = cat

            # Fallback default category
            default_cat, _ = Category.objects.get_or_create(
                pillar='vocational_technical_skills',
                defaults={'name': 'Vocational & Technical Skills', 'icon': '🔧'}
            )

            # 2. Seed Courses and Lessons
            courses_added = 0
            lessons_added = 0
            for c_data in data.get('courses', []):
                cat = categories.get(c_data['pillar'], default_cat)
                course, created = Course.objects.get_or_create(
                    title=c_data['title'],
                    defaults={
                        'category': cat,
                        'description': c_data.get('description', ''),
                        'level': c_data.get('level', 'beginner'),
                        'learning_approach': c_data.get('learning_approach', 'andragogic'),
                        'duration_hours': c_data.get('duration_hours', 30),
                        'is_active': c_data.get('is_active', True),
                        'featured': c_data.get('featured', False),
                    }
                )
                if created:
                    courses_added += 1

                # Seed lessons for this course
                for l_data in c_data.get('lessons', []):
                    _, l_created = Lesson.objects.get_or_create(
                        course=course,
                        order=l_data['order'],
                        defaults={
                            'title': l_data['title'],
                            'content': l_data.get('content', ''),
                            'duration_minutes': l_data.get('duration_minutes', 30),
                            'video_url': l_data.get('video_url', '')
                        }
                    )
                    if l_created:
                        lessons_added += 1

        self.stdout.write(self.style.SUCCESS(
            f"Successfully synced master catalog! Added {courses_added} new courses and {lessons_added} new lessons. "
            f"Total Courses in DB: {Course.objects.count()}"
        ))