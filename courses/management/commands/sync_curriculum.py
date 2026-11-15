# courses/management/commands/sync_curriculum.py
import json
import os
import re
from django.core.management.base import BaseCommand
from courses.models import Category, Course

class Command(BaseCommand):
    help = 'Strictly imports true master vocational courses while ignoring lesson fragments and module permutations.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--file',
            type=str,
            default='backup_105_courses.json',
            help='Path to the JSON curriculum data file.'
        )

    def handle(self, *args, **options):
        input_path = options['file']
        
        possible_paths = [
            input_path,
            os.path.join('courses', 'fixtures', input_path),
            os.path.join('fixtures', input_path),
        ]
        
        file_path = None
        for path in possible_paths:
            if os.path.exists(path):
                file_path = path
                break

        if not file_path:
            self.stdout.write(self.style.ERROR(f"Target file '{input_path}' not found."))
            return

        self.stdout.write(self.style.SUCCESS(f"Reading master curriculum from {file_path}..."))

        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            raw_content = f.read()

        data = json.loads(raw_content)
        items = data if isinstance(data, list) else data.get('courses', [])
        
        Course.objects.all().delete()
        Category.objects.all().delete()

        default_category, _ = Category.objects.get_or_create(
            name="Vocational & Technical Skills",
            defaults={'description': 'Independent empowerment curriculum'}
        )

        created_courses = 0
        skipped_count = 0
        seen_titles = set()

        # Keywords that indicate a sub-lesson fragment rather than a true independent course
        fragment_keywords = [
            'lesson', 'module', 'where to buy', 'pricing', 'marketing', 
            'branding', 'mistakes', 'business plan', 'mentorship', 
            'tools needed', 'safety', 'theory', 'practical', 'next steps',
            'intermediate', 'expanding', 'intro'
        ]

        for idx, item in enumerate(items):
            fields = item.get('fields', item)
            model_type = item.get('model', '').lower()

            if model_type and 'course' not in model_type:
                continue

            title = fields.get('title') or fields.get('name', '')
            if not title:
                continue

            clean_title = title.strip()

            # Skip if title starts with numbers (e.g. "1. Introduction", "10. Where to Buy")
            if re.match(r'^\d+\.?\s*', clean_title):
                skipped_count += 1
                continue

            # Skip if title contains any fragment keywords
            lower_title = clean_title.lower()
            if any(kw in lower_title for kw in fragment_keywords):
                skipped_count += 1
                continue

            if clean_title in seen_titles:
                skipped_count += 1
                continue
            seen_titles.add(clean_title)

            description = fields.get('description', 'Comprehensive technical training module for vocational excellence.')
            level = fields.get('level', 'beginner').lower()
            if level not in ['beginner', 'intermediate', 'advanced']:
                level = 'beginner'

            Course.objects.create(
                title=clean_title,
                category=default_category,
                description=description,
                level=level,
                duration_hours=fields.get('duration_hours', 10),
                learning_objectives=fields.get('learning_objectives', 'Master practical trade skills for self-reliance and enterprise.'),
                prerequisites=fields.get('prerequisites', 'None'),
                is_active=True,
                featured=fields.get('featured', False)
            )
            created_courses += 1

        self.stdout.write(self.style.SUCCESS(
            f"\nPristine Master Import Complete!\n"
            f"- Valid Vocational Courses Imported: {created_courses}\n"
            f"- Fragment/Duplicate Rows Skipped: {skipped_count}\n"
            f"- Total Clean Courses in DB: {Course.objects.count()}"
        ))