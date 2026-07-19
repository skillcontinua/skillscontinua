from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import get_language
from .models import Course, Category, Lesson, Enrollment
from django.db.models import Q

def course_list(request):
    """List all courses with language support, filtering, and search"""
    language = get_language()
    
    # Get all categories
    categories = Category.objects.all()
    
    # Get translated names for categories
    for category in categories:
        category.translated_name = category.get_name(language)
        category.translated_description = category.get_description(language)
    
    # Get filter parameters
    category_id = request.GET.get('category')
    approach = request.GET.get('approach')
    search_query = request.GET.get('q', '').strip()
    
    # Base queryset
    courses = Course.objects.filter(is_active=True)
    
    # Apply search filter
    if search_query:
        courses = courses.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(category__name__icontains=search_query)
        )
    
    # Apply category filter
    if category_id:
        try:
            category_id = int(category_id)
            courses = courses.filter(category_id=category_id)
        except ValueError:
            pass
    
    # Apply approach filter
    if approach:
        courses = courses.filter(learning_approach=approach)
    
    # Get translated content for courses
    for course in courses:
        course.translated_title = course.get_title(language)
        course.translated_description = course.get_description(language)
    
    context = {
        'categories': categories,
        'courses': courses,
        'current_language': language,
        'selected_category': category_id,
        'selected_approach': approach,
        'search_query': search_query,
        'total_results': courses.count(),
    }
    return render(request, 'courses/list.html', context)

def course_detail(request, pk):
    """Course detail with language support"""
    language = get_language()
    course = get_object_or_404(Course, pk=pk)
    
    course.translated_title = course.get_title(language)
    course.translated_description = course.get_description(language)
    
    # Translate lessons
    lessons = course.lessons.all()
    for lesson in lessons:
        lesson.translated_title = lesson.get_title(language)
        lesson.translated_content = lesson.get_content(language)
    
    context = {
        'course': course,
        'lessons': lessons,
        'current_language': language,
    }
    return render(request, 'courses/detail.html', context)

@login_required
def enroll(request, pk):
    """Enroll in a course"""
    course = get_object_or_404(Course, pk=pk)
    enrollment, created = Enrollment.objects.get_or_create(
        student=request.user,
        course=course,
        defaults={'status': 'enrolled'}
    )
    
    if created:
        messages.success(request, f'Successfully enrolled in {course.title}!')
    else:
        messages.info(request, f'You are already enrolled in {course.title}')
    
    return redirect('courses:course_detail', pk=pk)

@login_required
def lesson_view(request, course_pk, lesson_pk):
    """View a specific lesson"""
    course = get_object_or_404(Course, pk=course_pk)
    lesson = get_object_or_404(Lesson, pk=lesson_pk, course=course)
    enrollment = get_object_or_404(Enrollment, student=request.user, course=course)
    
    language = get_language()
    lesson.translated_title = lesson.get_title(language)
    lesson.translated_content = lesson.get_content(language)
    
    context = {
        'course': course,
        'lesson': lesson,
        'enrollment': enrollment,
        'current_language': language,
    }
    return render(request, 'courses/lesson.html', context)