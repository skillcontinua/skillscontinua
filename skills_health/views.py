from django.shortcuts import render
from django.http import JsonResponse
from courses.models import Course, Lesson
from django.contrib.auth.models import User
import os
from django.conf import settings

def diagnostic_dashboard(request):
    """Main diagnostic dashboard"""
    context = {
        'total_courses': Course.objects.count(),
        'total_lessons': Lesson.objects.count(),
        'total_users': User.objects.count(),
        'template_exists': os.path.exists(settings.BASE_DIR / 'templates' / 'courses' / 'lesson_standalone.html'),
    }
    return render(request, 'skills_health/diagnostic.html', context)