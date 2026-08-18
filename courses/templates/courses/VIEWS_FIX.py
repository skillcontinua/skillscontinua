
# Add to courses/views.py - Language handling
def get_current_language(request):
    lang = request.GET.get('lang', request.LANGUAGE_CODE if hasattr(request, 'LANGUAGE_CODE') else 'en')
    if lang not in ['en','fr','es','pt','sw','ar']:
        lang = 'en'
    return lang

def course_list(request):
    current_lang = get_current_language(request)
    courses = Course.objects.filter(language=current_lang).order_by('title')
    # Fallback to English if no courses in that language
    if not courses.exists() and current_lang != 'en':
        courses = Course.objects.filter(language='en')
    return render(request, 'courses/course_list.html', {
        'courses': courses,
        'current_lang': current_lang
    })

def course_detail(request, slug):
    current_lang = get_current_language(request)
    course = get_object_or_404(Course, slug=slug)
    lessons = course.lessons.order_by('order', 'id')
    return render(request, 'courses/course_detail.html', {
        'course': course,
        'lessons': lessons,
        'current_lang': current_lang
    })

def lesson_detail(request, course_slug, lesson_slug):
    current_lang = get_current_language(request)
    course = get_object_or_404(Course, slug=course_slug)
    lesson = get_object_or_404(Lesson, slug=lesson_slug, course=course)
    all_lessons = course.lessons.order_by('order', 'id')
    # Find prev/next
    lesson_list = list(all_lessons)
    idx = lesson_list.index(lesson)
    prev_lesson = lesson_list[idx-1] if idx > 0 else None
    next_lesson = lesson_list[idx+1] if idx < len(lesson_list)-1 else None
    
    return render(request, 'courses/lesson_detail.html', {
        'course': course,
        'lesson': lesson,
        'all_lessons': all_lessons,
        'prev_lesson': prev_lesson,
        'next_lesson': next_lesson,
        'current_lang': current_lang
    })
