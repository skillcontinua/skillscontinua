from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.utils import timezone
from django.template.loader import render_to_string
from xhtml2pdf import pisa
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
    """Download certificate as PDF using xhtml2pdf"""
    certificate = get_object_or_404(Certificate, pk=pk, student=request.user)
    
    context = {
        'certificate': certificate,
        'student_name': f"{request.user.first_name} {request.user.last_name}".strip() or request.user.username,
        'issue_date': certificate.issue_date.strftime('%B %d, %Y'),
    }
    
    # Render HTML to string
    html_string = render_to_string('certifications/certificate_pdf.html', context)
    
    # Create PDF
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.StringIO(html_string), dest=result)
    
    if not pdf.err:
        response = HttpResponse(result.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="certificate_{certificate.certificate_number}.pdf"'
        return response
    else:
        messages.error(request, 'Error generating PDF. Please try again.')
        return redirect('certifications:certificate_detail', pk=certificate.id)

@login_required
def share_certificate(request, pk):
    """Share certificate on social media"""
    certificate = get_object_or_404(Certificate, pk=pk, student=request.user)
    
    verification_url = f"{request.scheme}://{request.get_host()}{certificate.verification_url}"
    
    share_urls = {
        'facebook': f"https://www.facebook.com/sharer/sharer.php?u={verification_url}",
        'twitter': f"https://twitter.com/intent/tweet?text=I earned a certificate from SkillsContinua!&url={verification_url}",
        'linkedin': f"https://www.linkedin.com/sharing/share-offsite/?url={verification_url}",
        'whatsapp': f"https://api.whatsapp.com/send?text=I earned a certificate from SkillsContinua! {verification_url}",
    }
    
    context = {
        'certificate': certificate,
        'share_urls': share_urls,
        'verification_url': verification_url,
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