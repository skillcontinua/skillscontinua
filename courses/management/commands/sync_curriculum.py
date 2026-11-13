# courses/management/commands/sync_curriculum.py
import json
import os
from django.core.management.base import BaseCommand
from courses.models import Category, Course, Lesson

class Command(BaseCommand):
    help = 'Idempotently syncs and seeds courses from standard Django fixture JSON files.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--file',
            type=str,
            default='courses_316.json',
            help='Path to the JSON curriculum data file.'
        )

    def handle(self, *args, **options):
        file_path = options['file']
        self.stdout.write(self.style.SUCCESS(f"Starting curriculum synchronization from {file_path}..."))

        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f"Target file {file_path} not found in root directory."))
            return

        # Load JSON with encoding fallback
        raw_content = None
        used_encoding = 'utf-8'
        for encoding in ['utf-8', 'latin-1', 'cp1252']:
            try:
                with open(file_path, 'r', encoding=encoding) as f:
                    raw_content = f.read()
                used_encoding = encoding
                break
            except UnicodeDecodeError:
                continue

        if raw_content is None:
            self.stdout.write(self.style.ERROR("Failed to decode JSON file with any standard encoding."))
            return

        try:
            data = json.loads(raw_content)
        except json.JSONDecodeError as e:
            self.stdout.write(self.style.ERROR(
                f"\n[CRITICAL JSON ERROR]\n"
                f"File '{file_path}' has a syntax error at Line {e.lineno}, Column {e.colno}.\n"
                f"Error detail: {e.msg}\n"
            ))
            return

        items = data if isinstance(data, list) else data.get('courses', [])
        created_courses = 0
        updated_courses = 0
        created_categories = 0

        # Ensure a default category exists for fixture items
        default_category, _ = Category.objects.get_or_create(
            name="General Technical Skills",
            defaults={'description': 'Core technical curriculum category'}
        )

        for idx, item in enumerate(items):
            # Handle Django fixture format vs flat dict format
            fields = item.get('fields', item)
            model_type = item.get('model', '')

            # Only process course models (skip if it's a category fixture or other model)
            if model_type and 'course' not in model_type:
                continue

            try:
                title = fields.get('title') or fields.get('name', f'Untitled Course {idx+1}')
                description = fields.get('description', 'Comprehensive technical training module.')
                level = fields.get('level', 'beginner').lower()
                if level not in ['beginner', 'intermediate', 'advanced']:
                    level = 'beginner'

                # Resolve category FK if provided as integer ID or name
                cat_id = fields.get('category', default_category.id)
                if isinstance(cat_id, int):
                    try:
                        category = Category.objects.get(pk=cat_id)
                    except Category.DoesNotExist:
                        category = default_category
                else:
                    category, _ = Category.objects.get_or_create(name=str(cat_id))

                course, course_created = Course.objects.update_or_create(
                    title=title,
                    defaults={
                        'category': category,
                        'description': description,
                        'level': level,
                        'duration_hours': fields.get('duration_hours', 10),
                        'learning_objectives': fields.get('learning_objectives', ''),
                        'prerequisites': fields.get('prerequisites', ''),
                        'is_active': fields.get('is_active', True),
                        'featured': fields.get('featured', False),
                        'title_fr': fields.get('title_fr'),
                        'title_es': fields.get('title_es'),
                        'title_pt': fields.get('title_pt'),
                        'title_sw': fields.get('title_sw'),
                        'title_ar': fields.get('title_ar'),
                    }
                )

                if course_created:
                    created_courses += 1
                else:
                    updated_courses += 1

            except Exception as row_err:
                self.stdout.write(self.style.WARNING(f"Skipping course item at index {idx}: {row_err}"))

        self.stdout.write(self.style.SUCCESS(
            f"\nSync Complete using {used_encoding} encoding!\n"
            f"- Courses Created: {created_courses}\n"
            f"- Courses Updated: {updated_courses}\n"
            f"- Total Courses in DB: {Course.objects.count()}"
        ))