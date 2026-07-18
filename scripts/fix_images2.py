import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skillscontinua_core.settings')
django.setup()

from courses.models import Lesson, LessonImage

def get_lesson(title):
    return Lesson.objects.get(title=title, course__title='Introduction to Computers')

# Fix mouse — it's on What is a Computer, move to Input Devices
try:
    imgs = LessonImage.objects.filter(lesson=get_lesson('What is a Computer?'))
    for img in imgs:
        print(f'Found on What is a Computer: {img.caption} | {img.embed_tag}')
        if img.embed_tag == 'mouse-diagram':
            img.lesson = get_lesson('Input Devices')
            img.save()
            print('  -> Moved to Input Devices')
        elif img.embed_tag == 'computer-flow':
            print('  -> computer-flow already here, keeping')
        else:
            img.delete()
            print('  -> Deleted (not needed)')
except Exception as e:
    print(f'Error: {e}')

# Check keyboard on Input Devices
try:
    k = LessonImage.objects.get(lesson=get_lesson('Input Devices'), embed_tag='keyboard-diagram')
    print(f'Keyboard OK: {k.caption}')
except LessonImage.DoesNotExist:
    print('WARNING: No keyboard image on Input Devices — needs uploading')

# Check computer-flow on What is a Computer
try:
    c = LessonImage.objects.get(lesson=get_lesson('What is a Computer?'), embed_tag='computer-flow')
    print(f'Computer flow OK: {c.caption}')
except LessonImage.DoesNotExist:
    print('WARNING: No computer-flow image on What is a Computer — needs uploading')

print('\nFinal state:')
for img in LessonImage.objects.filter(
    lesson__course__title='Introduction to Computers'
).order_by('lesson__order'):
    print(f'  {img.lesson.title} | {img.caption} | {img.embed_tag}')