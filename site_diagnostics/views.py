from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import get_template
import os
from django.conf import settings
from courses.models import Course, Lesson, Enrollment
from django.contrib.auth.models import User

def diagnostic_dashboard(request):
    """Main diagnostic dashboard"""
    context = {
        'total_courses': Course.objects.count(),
        'total_lessons': Lesson.objects.count(),
        'total_users': User.objects.count(),
        'total_enrollments': Enrollment.objects.count(),
        'template_exists': os.path.exists(settings.BASE_DIR / 'templates' / 'courses' / 'lesson_standalone.html'),
    }
    return render(request, 'site_diagnostics/diagnostic.html', context)

def check_template(request):
    """Check if a template can be loaded"""
    template_name = request.GET.get('template', 'courses/lesson_standalone.html')
    try:
        template = get_template(template_name)
        return JsonResponse({
            'status': 'success',
            'template': template_name,
            'origin': str(template.origin)
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'template': template_name,
            'error': str(e)
        })

def check_url(request):
    """Check if a URL pattern exists"""
    from django.urls import resolve
    url_path = request.GET.get('url', '/courses/300/lesson/3066/')
    try:
        resolver = resolve(url_path)
        return JsonResponse({
            'status': 'success',
            'url': url_path,
            'view': resolver.func.__name__
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'url': url_path,
            'error': str(e)
        })

def check_database(request):
    """Check database connectivity and data"""
    try:
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            db_ok = True
    except:
        db_ok = False
    
    return JsonResponse({
        'status': 'success',
        'database_connected': db_ok,
        'total_courses': Course.objects.count(),
        'total_lessons': Lesson.objects.count(),
        'sample_course': Course.objects.first().title if Course.objects.exists() else None,
        'sample_lesson': Lesson.objects.first().title if Lesson.objects.exists() else None,
    })