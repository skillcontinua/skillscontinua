from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.utils import timezone
from django.template.loader import render_to_string
from weasyprint import HTML
import io
from .models import Certificate, CertificateTemplate, CertificateVerification
from courses.models import Enrollment

@login_required
def my_certificates(request):
    """Display all certificates earned by the user"""
    certificates = Certificate.objects.filter(student=request.user).select_related('course')
    
    context = {
        'certificates': certificates,
        'total': certificates.count(),
    }
    return render(request, 'certifications/my_certificates.html', context)

@login_required
def generate_certificate(request, enrollment_id):
    """Generate certificate for a completed course"""
    enrollment = get_object_or_404(Enrollment, id=enrollment_id, student=request.user)
    
    # Check if course is completed
    if enrollment.status != 'completed':
        messages.error(request, 'You must complete the course first!')
        return redirect('courses:course_detail', pk=enrollment.course.id)
    
    # Check if certificate already exists
    existing_certificate = Certificate.objects.filter(student=request.user, course=enrollment.course).first()
    if existing_certificate:
        messages.info(request, 'Certificate already generated!')
        return redirect('certifications:certificate_detail', pk=existing_certificate.id)
    
    # Create certificate
    certificate = Certificate.objects.create(
        student=request.user,
        course=enrollment.course,
        certificate_type='course_completion',
        issue_date=timezone.now(),
        score_percentage=enrollment.progress_percent,
        duration_hours=enrollment.course.duration_hours,
    )
    
    messages.success(request, 'Certificate generated successfully!')
    return redirect('certifications:certificate_detail', pk=certificate.id)

@login_required
def certificate_detail(request, pk):
    """View certificate details"""
    certificate = get_object_or_404(Certificate, pk=pk, student=request.user)
    
    context = {
        'certificate': certificate,
        'student_name': f"{request.user.first_name} {request.user.last_name}".strip() or request.user.username,
    }
    return render(request, 'certifications/certificate_detail.html', context)

def verify_certificate(request, verification_code):
    """Verify a certificate using verification code"""
    certificate = get_object_or_404(Certificate, verification_code=verification_code)
    
    # Log verification
    CertificateVerification.objects.create(
        certificate=certificate,
        ip_address=request.META.get('REMOTE_ADDR'),
        user_agent=request.META.get('HTTP_USER_AGENT', ''),
        is_successful=True,
    )
    
    context = {
        'certificate': certificate,
        'student_name': f"{certificate.student.first_name} {certificate.student.last_name}".strip() or certificate.student.username,
        'is_verified': True,
    }
    return render(request, 'certifications/verify_certificate.html', context)

@login_required
def download_certificate(request, pk):
    """Download certificate as PDF"""
    certificate = get_object_or_404(Certificate, pk=pk, student=request.user)
    
    # Get template (use default if available)
    template = CertificateTemplate.objects.filter(is_active=True, is_default=True).first()
    
    context = {
        'certificate': certificate,
        'student_name': f"{request.user.first_name} {request.user.last_name}".strip() or request.user.username,
        'template': template,
    }
    
    # Render HTML
    html_string = render_to_string('certifications/certificate_pdf.html', context)
    
    # Generate PDF
    html = HTML(string=html_string)
    pdf = html.write_pdf()
    
    # Return PDF response
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="certificate_{certificate.certificate_number}.pdf"'
    return response

@login_required
def share_certificate(request, pk):
    """Share certificate on social media"""
    certificate = get_object_or_404(Certificate, pk=pk, student=request.user)
    
    # Social media sharing URLs
    share_urls = {
        'facebook': f"https://www.facebook.com/sharer/sharer.php?u={certificate.verification_url}",
        'twitter': f"https://twitter.com/intent/tweet?text=I earned a certificate from SkillsContinua!&url={certificate.verification_url}",
        'linkedin': f"https://www.linkedin.com/sharing/share-offsite/?url={certificate.verification_url}",
        'whatsapp': f"https://api.whatsapp.com/send?text=I earned a certificate from SkillsContinua! {certificate.verification_url}",
    }
    
    context = {
        'certificate': certificate,
        'share_urls': share_urls,
    }
    return render(request, 'certifications/share_certificate.html', context)

@login_required
def certificate_list_admin(request):
    """Admin view for managing certificates"""
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to view this page.')
        return redirect('home')
    
    certificates = Certificate.objects.all().select_related('student', 'course')
    total_issued = certificates.count()
    total_verified = certificates.filter(is_verified=True).count()
    
    context = {
        'certificates': certificates,
        'total_issued': total_issued,
        'total_verified': total_verified,
    }
    return render(request, 'certifications/admin_certificates.html', context)