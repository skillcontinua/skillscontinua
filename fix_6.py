import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
from courses.models import Course

LANGS=['fr','es','pt','sw','ar']
print("=== Restoring Courses ===")
for course in Course.objects.all():
    changed=False
    en_title = (getattr(course, 'title_en', '') or getattr(course, 'title', '') or '') or ''
    en_desc = (getattr(course, 'description_en', '') or getattr(course, 'description', '') or '') or ''
    for lang in LANGS:
        tf=f'title_{lang}'
        df=f'description_{lang}'
        if hasattr(course, tf):
            val = getattr(course, tf)
            if not val:
                setattr(course, tf, f'[{lang.upper()}] {en_title[:200]}')
                changed=True
        if hasattr(course, df):
            val = getattr(course, df)
            if not val or len(val or '')<20:
                if en_desc:
                    setattr(course, df, f'[{lang.upper()}] {en_desc[:500]}')
                    changed=True
    if changed:
        course.save()
        print(f"Fixed {course.id} - {en_title[:30]}")
print("Courses DONE")