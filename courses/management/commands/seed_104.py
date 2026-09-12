from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        from courses.models import Course, Category
        try:
            from courses.models import Pillar
            from courses.models import Category as CatModel
            # Check Pillar fields
            has_pillar = True
        except:
            has_pillar = False

        self.stdout.write(f"Before: {Course.objects.count()} courses, {Category.objects.count()} categories")

        # Get or create pillar - use name not slug
        pillar = None
        if has_pillar:
            pillar = Pillar.objects.first()
            if not pillar:
                pillar = Pillar.objects.create(
                    name="Digital Skills for Africa & World",
                    name_en="Digital Skills for Africa & World",
                )
                self.stdout.write(f"Created pillar: {pillar.name}")

        # Get or create category - NO slug field!
        cat = Category.objects.first()
        if not cat:
            if pillar:
                cat = Category.objects.create(
                    name="General Africa & World",
                    name_en="General Africa & World",
                    pillar=pillar,
                    description="For global fund",
                )
            else:
                cat = Category.objects.create(
                    name="General Africa & World",
                    name_en="General Africa & World",
                    description="For global fund",
                )
            self.stdout.write(f"Created category: {cat.name}")
        else:
            self.stdout.write(f"Using category: {cat.name}")

        # Create 104 courses
        created = 0
        for i in range(1, 105):
            title = f"Course {i} - Skills for Global Market & Aba"
            if not Course.objects.filter(title=title).exists():
                try:
                    Course.objects.create(
                        category=cat,
                        title=title,
                        description=f"Course {i} for Africa, global fund, Aba artisans, ABIAPOLY",
                        duration_hours=20,
                        level="beginner",
                    )
                    created += 1
                except Exception as e:
                    self.stdout.write(f"Error {i}: {e}")
                    # Try even simpler
                    try:
                        Course.objects.create(
                            category=cat,
                            title=title,
                        )
                        created += 1
                    except Exception as e2:
                        self.stdout.write(f"Failed {i}: {e2}")
                        break

        self.stdout.write(self.style.SUCCESS(f"Created {created} new. TOTAL: {Course.objects.count()} courses LIVE!"))