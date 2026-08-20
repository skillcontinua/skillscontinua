from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Category, Course, Lesson, Enrollment, UserProgress

def course_list(request):
    categories = Category.objects.all().order_by('order', 'name')
    courses = Course.objects.filter(is_active=True).select_related('category')
    category_id = request.GET.get('category')
    approach = request.GET.get('approach')
    search_query = request.GET.get('q', '').strip()
    selected_category = None
    if category_id:
        selected_category = get_object_or_404(Category, id=category_id)
        courses = courses.filter(category=selected_category)
    if approach:
        courses = courses.filter(learning_approach=approach)
    if search_query:
        courses = courses.filter(title__icontains=search_query)
    return render(request, 'courses/course_list.html', {
        'categories': categories, 'courses': courses,
        'selected_category': selected_category,
        'search_query': search_query, 'approach': approach,
    })

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk, is_active=True)
    lessons = course.lessons.all().order_by('order')
    return render(request, 'courses/course_detail.html', {'course': course, 'lessons': lessons})

@login_required
def enroll(request, pk):
    course = get_object_or_404(Course, pk=pk, is_active=True)
    Enrollment.objects.get_or_create(student=request.user, course=course, defaults={'status': 'enrolled'})
    messages.success(request, f'Enrolled in {course.title}')
    return redirect('courses:course_detail', pk=course.pk)

@login_required
def lesson_view(request, course_pk, lesson_pk):
    course = get_object_or_404(Course, pk=course_pk, is_active=True)
    lesson = get_object_or_404(Lesson, pk=lesson_pk, course=course)
    progress, _ = UserProgress.objects.get_or_create(user=request.user, lesson=lesson)
    return render(request, 'courses/lesson_detail.html', {'course': course, 'lesson': lesson, 'progress': progress})

@login_required
def complete_lesson(request, course_pk, lesson_pk):
    lesson = get_object_or_404(Lesson, pk=lesson_pk, course_id=course_pk)
    UserProgress.objects.update_or_create(user=request.user, lesson=lesson, defaults={'completed': True})
    return redirect('courses:lesson_view', course_pk=course_pk, lesson_pk=lesson_pk)