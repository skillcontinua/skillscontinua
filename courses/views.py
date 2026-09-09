from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count, Q
from .models import Category, Course, Lesson, Enrollment, UserProgress

def course_list(request):
    # All categories with course counts (user-friendly ordering)
    categories = Category.objects.annotate(
        total_courses=Count('courses', filter=Q(courses__is_active=True))
    ).order_by('order', 'name')

    # Featured first, then all active
    courses = Course.objects.filter(is_active=True).select_related('category').order_by('-featured', '-created_at')

    # Filters
    category_id = request.GET.get('category')
    approach = request.GET.get('approach')
    level = request.GET.get('level')
    search_query = request.GET.get('q', '').strip()
    selected_category = None

    if category_id and category_id.isdigit():
        selected_category = get_object_or_404(Category, id=category_id)
        courses = courses.filter(category=selected_category)
    
    if approach:
        courses = courses.filter(learning_approach=approach)
    
    if level:
        courses = courses.filter(level=level)
    
    if search_query:
        courses = courses.filter(
            Q(title__icontains=search_query) | 
            Q(description__icontains=search_query) |
            Q(category__name__icontains=search_query)
        )

    # Group courses by category for user-friendly display
    from collections import defaultdict
    grouped = defaultdict(list)
    for c in courses:
        grouped[c.category].append(c)

    # Stats for hero
    total_count = courses.count()
    featured_courses = courses.filter(featured=True)[:6]

    return render(request, 'courses/course_list.html', {
        'categories': categories,
        'courses': courses,
        'grouped_courses': dict(grouped),
        'selected_category': selected_category,
        'search_query': search_query,
        'approach': approach,
        'level': level,
        'total_count': total_count,
        'featured_courses': featured_courses,
    })

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    is_enrolled = False
    if request.user.is_authenticated:
        is_enrolled = Enrollment.objects.filter(student=request.user, course=course).exists()
    return render(request, 'courses/course_detail.html', {
        'course': course,
        'is_enrolled': is_enrolled,
        'lessons': course.lessons.order_by('order')
    })

@login_required
def enroll(request, pk):
    course = get_object_or_404(Course, pk=pk, is_active=True)
    Enrollment.objects.get_or_create(student=request.user, course=course, defaults={'status': 'enrolled'})
    messages.success(request, f'Enrolled in {course.title}')
    return redirect('courses:course_detail', pk=course.pk)

@login_required
def lesson_view(request, course_pk, lesson_pk):
    course = get_object_or_404(Course, pk=course_pk)
    lesson = get_object_or_404(Lesson, pk=lesson_pk, course=course)
    all_lessons = course.lessons.order_by('order')
    prev_lesson = all_lessons.filter(order__lt=lesson.order).order_by('-order').first()
    next_lesson = all_lessons.filter(order__gt=lesson.order).order_by('order').first()
    progress, _ = UserProgress.objects.get_or_create(user=request.user, lesson=lesson)
    total = all_lessons.count()
    completed = UserProgress.objects.filter(user=request.user, lesson__course=course, completed=True).count()
    progress_percent = int((completed/total*100)) if total else 0
    return render(request, 'courses/lesson_detail.html', {
        'course': course, 'lesson': lesson, 'progress': progress,
        'all_lessons': all_lessons, 'prev_lesson': prev_lesson, 'next_lesson': next_lesson,
        'progress_percent': progress_percent
    })

@login_required
def complete_lesson(request, course_pk, lesson_pk):
    lesson = get_object_or_404(Lesson, pk=lesson_pk, course_id=course_pk)
    UserProgress.objects.update_or_create(user=request.user, lesson=lesson, defaults={'completed': True})
    course = lesson.course
    total = course.lessons.count()
    done = UserProgress.objects.filter(user=request.user, lesson__course=course, completed=True).count()
    if done >= total and total>0:
        from certifications.models import Certificate
        cert, created = Certificate.objects.get_or_create(student=request.user, course=course, defaults={'score_percentage':100, 'duration_hours':course.duration_hours})
        if created:
            messages.success(request, f'Congratulations! Certificate issued: {cert.certificate_number}')
        Enrollment.objects.filter(student=request.user, course=course).update(status='completed', progress_percent=100, certificate_issued=True)
    messages.success(request, 'Lesson marked complete')
    return redirect('courses:lesson_view', course_pk=course_pk, lesson_pk=lesson_pk)

from django.contrib.auth.decorators import login_required
from .forms import LessonUploadForm

@login_required
def lesson_upload(request):
    if request.method == 'POST':
        form = LessonUploadForm(request.POST, request.FILES)
        if form.is_valid():
            lesson = form.save()
            messages.success(request, f"Lesson '{lesson.title}' uploaded!")
            return redirect('lesson_upload')
    else:
        form = LessonUploadForm()
    return render(request, 'courses/lesson_upload.html', {'form': form})