import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skillscontinua_core.settings')
django.setup()

from courses.models import Course, Lesson

# First, show all courses with 'mac' or 'linux' or 'operating' in the title
print('Searching for OS courses...')
for c in Course.objects.all().order_by('title'):
    if any(word in c.title.lower() for word in ['mac', 'linux', 'operating', 'apple', 'ubuntu']):
        print(f'  FOUND: "{c.title}" — {c.lessons.count()} lessons')

print('\nAlso showing all Computer category courses:')
for c in Course.objects.filter(category__pillar='computer').order_by('title'):
    print(f'  {c.title} — {c.lessons.count()} lessons')