from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm
from courses.models import Course, Lesson, Enrollment, Category


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome to SkillsContinua, {user.first_name}! Your journey begins now.')
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.first_name or user.username}!')
            if user.role == 'instructor':
                return redirect('instructor_dashboard')
            elif user.role == 'admin':
                return redirect('/admin/')
            else:
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.info(request, 'You have been logged out safely.')
    return redirect('home')


@login_required
def dashboard(request):
    if request.user.role == 'instructor':
        enrollments = request.user.enrollments.select_related('course').all()
        context = {
            'user': request.user,
            'enrollments': enrollments,
        }
        return render(request, 'accounts/dashboard.html', context)
    enrollments = request.user.enrollments.select_related('course').all()
    context = {
        'user': request.user,
        'enrollments': enrollments,
    }
    return render(request, 'accounts/dashboard.html', context)


@login_required
def instructor_dashboard(request):
    if request.user.role not in ['instructor', 'admin']:
        messages.error(request, 'Access denied. Instructor account required.')
        return redirect('dashboard')
    courses = Course.objects.filter(
        created_by=request.user
    ).prefetch_related('lessons', 'enrollments')
    all_courses = Course.objects.all().prefetch_related('lessons', 'enrollments')
    total_learners = Enrollment.objects.filter(
        course__created_by=request.user
    ).count()
    total_lessons = Lesson.objects.filter(course__in=all_courses).count()
    context = {
        'courses': courses,
        'all_courses': all_courses,
        'total_learners': total_learners,
        'total_lessons': total_lessons,
    }
    return render(request, 'accounts/instructor_dashboard.html', context)


@login_required
def add_lesson(request, course_pk):
    if request.user.role not in ['instructor', 'admin']:
        messages.error(request, 'Access denied.')
        return redirect('dashboard')
    course = get_object_or_404(Course, pk=course_pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        content_type = request.POST.get('content_type')
        content_text = request.POST.get('content_text')
        order = request.POST.get('order', 1)
        duration_minutes = request.POST.get('duration_minutes', 0)
        content_file = request.FILES.get('content_file')
        lesson = Lesson.objects.create(
            course=course,
            title=title,
            content_type=content_type,
            content_text=content_text,
            order=order,
            duration_minutes=duration_minutes,
            content_file=content_file,
            is_active=True
        )
        messages.success(request, f'Lesson "{lesson.title}" added successfully.')
        return redirect('edit_course', course_pk=course.pk)
    last_lesson = course.lessons.order_by('order').last()
    next_order = (last_lesson.order + 1) if last_lesson else 1
    return render(request, 'accounts/add_lesson.html', {
        'course': course,
        'next_order': next_order
    })


@login_required
def edit_lesson(request, lesson_pk):
    if request.user.role not in ['instructor', 'admin']:
        messages.error(request, 'Access denied.')
        return redirect('dashboard')
    lesson = get_object_or_404(Lesson, pk=lesson_pk)
    if request.method == 'POST':
        lesson.title = request.POST.get('title')
        lesson.content_type = request.POST.get('content_type')
        lesson.content_text = request.POST.get('content_text')
        lesson.order = request.POST.get('order', lesson.order)
        lesson.duration_minutes = request.POST.get('duration_minutes', lesson.duration_minutes)
        if request.FILES.get('content_file'):
            lesson.content_file = request.FILES.get('content_file')
        lesson.save()
        messages.success(request, f'Lesson "{lesson.title}" updated successfully.')
        return redirect('edit_course', course_pk=lesson.course.pk)
    return render(request, 'accounts/edit_lesson.html', {'lesson': lesson})


@login_required
def edit_course(request, course_pk):
    if request.user.role not in ['instructor', 'admin']:
        messages.error(request, 'Access denied.')
        return redirect('dashboard')
    course = get_object_or_404(Course, pk=course_pk)
    lessons = course.lessons.order_by('order')
    enrollments = course.enrollments.select_related('student').all()
    context = {
        'course': course,
        'lessons': lessons,
        'enrollments': enrollments,
        'enrollment_count': enrollments.count(),
    }
    return render(request, 'accounts/edit_course.html', context)