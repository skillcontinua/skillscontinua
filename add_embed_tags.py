import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skillscontinua_core.settings')
django.setup()

from courses.models import Lesson

lesson = Lesson.objects.get(
    title='Input Devices',
    course__title='Introduction to Computers'
)

# Add microphone embed tag after the mouse section
old_text = lesson.content_text
new_text = old_text.replace(
    'MICROPHONE: Speak to the computer for calls and voice commands',
    '[[image:microphone]]\n\nMICROPHONE: Speak to the computer for calls and voice commands'
)

if new_text != old_text:
    lesson.content_text = new_text
    lesson.save()
    print('Embed tag added successfully')
else:
    print('Text not found — printing current content for inspection:')
    print(lesson.content_text[:500])