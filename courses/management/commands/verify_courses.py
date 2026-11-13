# courses/management/commands/verify_courses.py
from django.core.management.base import BaseCommand
from courses.models import Course, Category, Lesson

class Command(BaseCommand):
    help = 'Audits the curriculum database for completeness, missing metadata, and structural health.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Starting Curriculum & Institutional Audit...\n"))

        courses = Course.objects.all()
        total_courses = courses.count()

        if total_courses == 0:
            self.stdout.write(self.style.WARNING("No courses found in database. Run sync_curriculum first."))
            return

        issues_found = 0
        orphaned_courses = 0
        missing_descriptions = 0
        missing_objectives = 0

        self.stdout.write(f"Total Courses in Database: {total_courses}")
        self.stdout.write(f"Total Categories: {Category.objects.count()}")
        self.stdout.write("-" * 60)

        for course in courses:
            course_issues = []
            
            # Check description quality
            if not course.description or len(course.description.strip()) < 10:
                missing_descriptions += 1
                course_issues.append("Missing or insufficient description")

            # Check learning objectives
            if not course.learning_objectives or len(course.learning_objectives.strip()) < 5:
                missing_objectives += 1
                course_issues.append("Missing learning objectives")

            # Check linked lessons
            lesson_count = course.lessons.count()
            if lesson_count == 0:
                orphaned_courses += 1
                course_issues.append("0 lessons (Orphaned course)")

            if course_issues:
                issues_found += 1
                self.stdout.write(self.style.WARNING(f"[!] Course ID {course.pk}: '{course.title}'"))
                for issue in course_issues:
                    self.stdout.write(f"    - {issue}")

        self.stdout.write("-" * 60)
        self.stdout.write(self.style.SUCCESS("Audit Summary Report:"))
        self.stdout.write(f"  - Total Courses Audited: {total_courses}")
        self.stdout.write(f"  - Courses Flagged with Issues: {issues_found}")
        self.stdout.write(f"  - Missing Descriptions: {missing_descriptions}")
        self.stdout.write(f"  - Missing Objectives: {missing_objectives}")
        f"  - Orphaned (0 Lessons): {orphaned_courses}"
        
        health_score = max(0, int(((total_courses - issues_found) / total_courses) * 100)) if total_courses > 0 else 0
        
        if health_score >= 85:
            score_output = self.style.SUCCESS(f"\nOverall Curriculum Health Score: {health_score}% [EXCELLENT]")
        elif health_score >= 60:
            score_output = self.style.WARNING(f"\nOverall Curriculum Health Score: {health_score}% [MODERATE]")
        else:
            score_output = self.style.ERROR(f"\nOverall Curriculum Health Score: {health_score}% [ACTION REQUIRED]")
            
        self.stdout.write(score_output)
        
        if health_score < 100:
            self.stdout.write(self.style.NOTICE("Recommendation: Run enrichment scripts or update JSON fixtures to resolve flagged records before generating donor reports."))