from django.shortcuts import render, get_object_or_404
from .models import Category, Course

def course_list(request):
    categories = Category.objects.all().order_by('order','name')
    courses = Course.objects.filter(is_active=True).order_by('category','title')
    
    category_id = request.GET.get('category')
    selected_category = None
    if category_id:
        selected_category = get_object_or_404(Category, id=category_id)
        courses = courses.filter(category=selected_category)
    
    context = {
        'categories': categories,
        'courses': courses,
        'selected_category': selected_category,
    }
    return render(request, 'courses/course_list.html', context)

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk, is_active=True)
    return render(request, 'courses/course_detail.html', {'course': course})