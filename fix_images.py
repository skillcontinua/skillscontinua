import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skillscontinua_core.settings')
django.setup()

from courses.models import Lesson, LessonImage

def get_lesson(title):
    return Lesson.objects.get(title=title, course__title='Introduction to Computers')

# Fix: move system-unit image to correct lesson
try:
    img = LessonImage.objects.get(caption='Inside the System Unit')
    img.lesson = get_lesson('Inside the System Unit')
    img.save()
    print('Fixed: system-unit moved')
except Exception as e:
    print(f'system-unit: {e}')

# Fix: move mouse image to Input Devices
try:
    img = LessonImage.objects.get(caption='Standard Mouse Layout Mouse Diagram')
    img.lesson = get_lesson('Input Devices')
    img.embed_tag = 'mouse-diagram'
    img.save()
    print('Fixed: mouse moved to Input Devices')
except Exception as e:
    print(f'mouse: {e}')

# Delete duplicates
for caption in ['Storage Devices', 'Output Devices', 'How a computer works']:
    try:
        imgs = LessonImage.objects.filter(
            caption=caption,
            lesson=get_lesson('What is a Computer?')
        )
        count = imgs.count()
        imgs.delete()
        print(f'Deleted {count} x {caption}')
    except Exception as e:
        print(f'Error {caption}: {e}')

# Delete wrong keyboard
try:
    img = LessonImage.objects.get(caption='Standard keyboard layout')
    img.delete()
    print('Deleted: Standard keyboard layout')
except Exception as e:
    print(f'Keyboard: {e}')

# Show final state
print('\nFinal state:')
for img in LessonImage.objects.filter(
    lesson__course__title='Introduction to Computers'
).order_by('lesson__order'):
    print(f'  {img.lesson.title} | {img.caption} | {img.embed_tag}')