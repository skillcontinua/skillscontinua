import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skillscontinua_core.settings')
django.setup()

from courses.models import Lesson, LessonImage
from django.core.files import File

def get_lesson(title):
    return Lesson.objects.get(title=title, course__title='Introduction to Computers')

folder = r'C:\Users\USER\Desktop\SKILLSCONTINUA_IMAGES'
keyboard_path = os.path.join(folder, 'keyboard-diagram.png')
flow_path = os.path.join(folder, 'computer-flow.png')

# Add keyboard to Input Devices
try:
    lesson = get_lesson('Input Devices')
    img = LessonImage(
        lesson=lesson,
        caption='Keyboard layout',
        embed_tag='keyboard-diagram',
        alt_text='Labeled keyboard showing all key groups',
        order=1
    )
    with open(keyboard_path, 'rb') as f:
        img.image.save('keyboard-diagram.png', File(f), save=True)
    print('Keyboard image added to Input Devices')
except Exception as e:
    print(f'Keyboard error: {e}')

# Add computer-flow to What is a Computer
try:
    lesson = get_lesson('What is a Computer?')
    img = LessonImage(
        lesson=lesson,
        caption='How a computer works',
        embed_tag='computer-flow',
        alt_text='Input process output storage diagram',
        order=1
    )
    with open(flow_path, 'rb') as f:
        img.image.save('computer-flow.png', File(f), save=True)
    print('Computer flow image added to What is a Computer')
except Exception as e:
    print(f'Flow error: {e}')

print('\nFinal state:')
for img in LessonImage.objects.filter(
    lesson__course__title='Introduction to Computers'
).order_by('lesson__order'):
    print(f'  {img.lesson.title} | {img.embed_tag}')