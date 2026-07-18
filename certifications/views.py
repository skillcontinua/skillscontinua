from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from courses.models import Enrollment

@login_required
def certification_list(request):
    enrollments = Enrollment.objects.filter(
        student=request.user,
        status='completed'
    ).select_related('course')
    
    context = {
        'certifications': enrollments,
        'total': enrollments.count(),
    }
    return render(request, 'certifications/list.html', context)

@login_required
def certification_detail(request, pk):
    enrollment = Enrollment.objects.get(
        student=request.user,
        course__pk=pk
    )
    return render(request, 'certifications/detail.html', {
        'certification': enrollment
    })