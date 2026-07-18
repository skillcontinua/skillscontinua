from django.shortcuts import render
from courses.models import Category, Course

def home(request):
    """Home page with learning pillars"""
    categories = Category.objects.all()
    courses = Course.objects.filter(is_active=True)
    
    total_courses = courses.count()
    total_pillars = categories.count()
    approaches = courses.values_list('learning_approach', flat=True).distinct().count()
    
    context = {
        'categories': categories,
        'courses': courses,
        'total_courses': total_courses,
        'total_pillars': total_pillars,
        'approaches_count': approaches if approaches > 0 else 4,
    }
    return render(request, 'core/home.html', context)