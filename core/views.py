from django.shortcuts import render
from django.utils.translation import get_language
from courses.models import Category, Course

def home(request):
    """Home page with learning pillars and language support"""
    # Get current language
    current_language = get_language()
    
    # Get all categories
    categories = Category.objects.all()
    
    # Get translated names for categories
    for category in categories:
        category.translated_name = category.get_name(current_language)
        category.translated_description = category.get_description(current_language)
    
    # Get active courses
    courses = Course.objects.filter(is_active=True)
    
    # Get translated titles for courses
    for course in courses:
        course.translated_title = course.get_title(current_language)
        course.translated_description = course.get_description(current_language)
    
    # Calculate statistics
    total_courses = courses.count()
    total_pillars = categories.count()
    approaches = courses.values_list('learning_approach', flat=True).distinct().count()
    
    context = {
        'categories': categories,
        'courses': courses,
        'total_courses': total_courses,
        'total_pillars': total_pillars,
        'approaches_count': approaches if approaches > 0 else 4,
        'current_language': current_language,
    }
    return render(request, 'core/home.html', context)