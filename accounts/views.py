from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.utils import timezone
from .forms import RegisterForm, LoginForm
from courses.models import Enrollment, Course
from certifications.models import Certificate

User = get_user_model()

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome {user.first_name}! Your account has been created.')
            return redirect('home')
    else:
        form = RegisterForm()
    
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', 'home')
            messages.success(request, f'Welcome back {user.first_name}!')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home')

@login_required
def profile(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.email = request.POST.get('email', user.email)
        user.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('accounts:profile')
    
    return render(request, 'accounts/profile.html', {'user': request.user})

@login_required
def dashboard(request):
    """Professional dashboard with all user stats"""
    from courses.models import Enrollment, Course
    from certifications.models import Certificate
    
    # Get user's enrollments
    enrollments = Enrollment.objects.filter(student=request.user).select_related('course')
    in_progress = enrollments.filter(status='in_progress')
    completed = enrollments.filter(status='completed')
    
    # Get certificates
    certificates = Certificate.objects.filter(student=request.user)
    certificates_count = certificates.count()
    
    # Calculate overall progress
    total_courses = enrollments.count()
    total_progress = sum(e.progress_percent for e in enrollments) if enrollments else 0
    avg_progress = total_progress / total_courses if total_courses > 0 else 0
    
    # Get recommended courses (courses not enrolled in, with highest ratings)
    enrolled_course_ids = enrollments.values_list('course_id', flat=True)
    recommended = Course.objects.filter(is_active=True).exclude(id__in=enrolled_course_ids)[:5]
    
    # Get recent activity (for demo, use recent enrollments)
    recent_activity = []
    for enrollment in enrollments.order_by('-started_at')[:5]:
        recent_activity.append({
            'description': f"Started course: {enrollment.course.title}",
            'timestamp': enrollment.started_at
        })
    
    context = {
        'enrollments': enrollments,
        'in_progress': in_progress,
        'completed': completed,
        'total_courses': total_courses,
        'avg_progress': avg_progress,
        'certificates_count': certificates_count,
        'recommended_courses': recommended,
        'recent_activity': recent_activity,
    }
    return render(request, 'accounts/dashboard.html', context)