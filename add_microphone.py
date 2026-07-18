import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skillscontinua_core.settings')
django.setup()

from courses.models import Lesson, LessonImage
from django.core.files import File

lesson = Lesson.objects.get(
    title='Input Devices',
    course__title='Introduction to Computers'
)

img = LessonImage(
    lesson=lesson,
    caption='Microphone, camera and scanner',
    embed_tag='microphone',
    alt_text='Audio and visual input devices including microphone webcam and scanner',
    order=3
)

path = r'C:\Users\USER\Desktop\SKILLSCONTINUA_IMAGES\microphone.png'
with open(path, 'rb') as f:
    img.image.save('microphone.png', File(f), save=True)

print('Microphone image added to Input Devices')

# Show all Input Devices images
for i in LessonImage.objects.filter(lesson=lesson).order_by('order'):
    print(f'  Order:{i.order} | {i.caption} | {i.embed_tag}')