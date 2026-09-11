from django.core.management.base import BaseCommand
from django.db import connection
from courses.models import Course, Category

class Command(BaseCommand):
    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT id, category_id, LOWER(TRIM(title))
                FROM courses_course
                ORDER BY id
            """)
            seen = {}
            dup_ids = []
            for cid, cat_id, title in cursor.fetchall():
                key = (cat_id, title)
                if key in seen:
                    dup_ids.append(cid)
                else:
                    seen[key] = cid

            print(f"Found {len(dup_ids)} duplicates: {dup_ids}")

            if dup_ids:
                cursor.execute("DELETE FROM courses_lesson WHERE course_id IN %s", (tuple(dup_ids),))
                print(f"Deleted lessons: {cursor.rowcount}")
                cursor.execute("DELETE FROM courses_course WHERE id IN %s", (tuple(dup_ids),))
                print(f"Deleted courses: {cursor.rowcount}")

        print(f"\nTOTAL after clean: {Course.objects.filter(is_active=True).count()} courses")
        for cat in Category.objects.all().order_by('order'):
            print(f"{cat.order:2} {cat.pillar[:35]:35} {cat.courses.filter(is_active=True).count():2} courses")