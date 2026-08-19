from django.shortcuts import render, get_object_or_404
from.models import Category, Course

def course_list(request):
    # Uses Category.translated_name property — no manual setting
    categories = Category.objects.all().order_by('order', 'name')
    courses = Course.objects.filter(is_active=True).select_related('category')

    category_id = request.GET.get('category')
    approach = request.GET.get('approach')
    search_query = request.GET.get('q', '').strip()

    selected_category = None
    if category_id:
        selected_category = get_object_or_404(Category, id=category_id)
        courses = courses.filter(category=selected_category)
    if approach:
        courses = courses.filter(learning_approach=approach)
    if search_query:
        courses = courses.filter(title__icontains=search_query)

    return render(request, 'courses/course_list.html', {
        'categories': categories,
        'courses': courses,
        'selected_category': selected_category,
        'search_query': search_query,
        'approach': approach,
    })

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk, is_active=True)
    return render(request, 'courses/course_detail.html', {'course': course})