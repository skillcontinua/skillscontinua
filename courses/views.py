from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Course

def course_list(request):
    categories = Category.objects.all().order_by('order').prefetch_related('courses')
    total_courses = Course.objects.filter(is_active=True).count()
    return render(request, 'courses/course_list.html', {
        'categories': categories,
        'total_courses': total_courses,
        'total_pillars': categories.count(),
    })

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk, is_active=True)
    return render(request, 'courses/course_detail.html', {'course': course})

def enroll(request, pk):
    # Simple enroll placeholder - redirects to course detail for now
    course = get_object_or_404(Course, pk=pk, is_active=True)
    return redirect('course_detail', pk=course.pk)

def pillar_courses(request, pillar_slug):
    category = get_object_or_404(Category, pillar=pillar_slug)
    courses = category.courses.filter(is_active=True)
    return render(request, 'courses/pillar_courses.html', {
        'category': category,
        'courses': courses,
    })