from django.shortcuts import render
from courses.models import Category, Course

def home(request):
    categories = Category.objects.all().order_by('order','name')
    total_courses = Course.objects.filter(is_active=True).count()
    return render(request, 'core/home.html', {
        'categories': categories,
        'total_courses': total_courses,
    })

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')