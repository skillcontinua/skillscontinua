from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import get_language
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.utils.safestring import mark_safe  # <-- ADD THIS LINE
import json

from .models import Course, Category, Lesson, Enrollment, UserProgress


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
    course = get_object_or_404(Course, pk=pk, is_active=True)
    
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
    """View a specific lesson with HTML rendering"""
    course = get_object_or_404(Course, pk=course_pk)
    lesson = get_object_or_404(Lesson, pk=lesson_pk, course=course)
    
    # Get next and previous lessons
    lessons = course.lessons.all().order_by('order')
    lesson_list = list(lessons)
    current_index = lesson_list.index(lesson)
    
    previous_lesson = lesson_list[current_index - 1] if current_index > 0 else None
    next_lesson = lesson_list[current_index + 1] if current_index < len(lesson_list) - 1 else None
    
    # FORCE HTML RENDERING - THIS IS THE KEY FIX
    lesson.content = mark_safe(lesson.content)
    
    # Check if user is enrolled
    try:
        enrollment = Enrollment.objects.get(student=request.user, course=course)
    except Enrollment.DoesNotExist:
        enrollment = None
    
    context = {
        'course': course,
        'lesson': lesson,
        'previous_lesson': previous_lesson,
        'next_lesson': next_lesson,
        'enrollment': enrollment,
    }
    return render(request, 'courses/lesson.html', context)


def lesson_detail(request, lesson_id):
    """Display a single lesson using just lesson_id"""
    lesson = get_object_or_404(Lesson, id=lesson_id)
    course = lesson.course
    
    # Get next and previous lessons
    lessons = course.lessons.all().order_by('order')
    lesson_list = list(lessons)
    current_index = lesson_list.index(lesson)
    
    previous_lesson = lesson_list[current_index - 1] if current_index > 0 else None
    next_lesson = lesson_list[current_index + 1] if current_index < len(lesson_list) - 1 else None
    
    # Check if user is enrolled
    is_enrolled = False
    if hasattr(request, 'user') and request.user.is_authenticated:
        is_enrolled = Enrollment.objects.filter(student=request.user, course=course).exists()
    
    context = {
        'lesson': lesson,
        'course': course,
        'previous_lesson': previous_lesson,
        'next_lesson': next_lesson,
        'is_enrolled': is_enrolled,
    }
    return render(request, 'courses/lesson_detail.html', context)


@csrf_exempt
@login_required
def mark_lesson_complete(request):
    """API endpoint to mark a lesson as complete"""
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
    try:
        data = json.loads(request.body)
        lesson_id = data.get('lesson_id')
        
        if not lesson_id:
            return JsonResponse({'error': 'lesson_id required'}, status=400)
        
        lesson = Lesson.objects.get(id=lesson_id)
        
        # Get or create progress record
        progress, created = UserProgress.objects.get_or_create(
            user=request.user,
            lesson=lesson,
            defaults={'completed': True, 'completed_at': timezone.now()}
        )
        
        # If already exists and not completed, update it
        if not created and not progress.completed:
            progress.completed = True
            progress.completed_at = timezone.now()
            progress.save()
        
        # Calculate progress percentage for this course
        total_lessons = lesson.course.lessons.count()
        completed_lessons = UserProgress.objects.filter(
            user=request.user,
            lesson__course=lesson.course,
            completed=True
        ).count()
        
        progress_percentage = int((completed_lessons / total_lessons) * 100) if total_lessons > 0 else 0
        
        return JsonResponse({
            'success': True,
            'completed': True,
            'progress_percentage': progress_percentage,
            'completed_lessons': completed_lessons,
            'total_lessons': total_lessons
        })
        
    except Lesson.DoesNotExist:
        return JsonResponse({'error': 'Lesson not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def get_course_progress(request, course_id):
    """Get progress for a specific course"""
    try:
        course = Course.objects.get(id=course_id)
        total_lessons = course.lessons.count()
        
        if request.user.is_authenticated:
            completed_lessons = UserProgress.objects.filter(
                user=request.user,
                lesson__course=course,
                completed=True
            ).count()
        else:
            completed_lessons = 0
        
        progress_percentage = int((completed_lessons / total_lessons) * 100) if total_lessons > 0 else 0
        
        return JsonResponse({
            'success': True,
            'progress_percentage': progress_percentage,
            'completed_lessons': completed_lessons,
            'total_lessons': total_lessons
        })
    except Course.DoesNotExist:
        return JsonResponse({'error': 'Course not found'}, status=404)


def test_lesson(request, lesson_id):
    """Simple test view"""
    lesson = get_object_or_404(Lesson, id=lesson_id)
    return render(request, 'courses/lesson_standalone.html', {'lesson': lesson})


def simple_lesson(request, lesson_id):
    """Simple lesson view that always works"""
    from .models import Lesson
    lesson = get_object_or_404(Lesson, id=lesson_id)
    context = {'lesson': lesson}
    return render(request, 'courses/simple_lesson.html', context)