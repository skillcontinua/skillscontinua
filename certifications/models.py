from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from courses.models import Course

User = get_user_model()

class Certificate(models.Model):
    """Certificate awarded upon course completion"""
    
    # Certificate Types
    TYPE_CHOICES = [
        ('course_completion', 'Course Completion'),
        ('skill_mastery', 'Skill Mastery'),
        ('professional', 'Professional Certification'),
        ('honors', 'Honors Certificate'),
    ]
    
    # Core Fields
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='certificates')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='certificates')
    certificate_type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='course_completion')
    
    # Certificate Details
    certificate_number = models.CharField(max_length=50, unique=True, blank=True)
    issue_date = models.DateTimeField(default=timezone.now)
    expiry_date = models.DateTimeField(null=True, blank=True)
    
    # Verification
    verification_code = models.CharField(max_length=100, unique=True, blank=True)
    is_verified = models.BooleanField(default=True)
    verification_url = models.URLField(blank=True)
    
    # Additional Info
    grade = models.CharField(max_length=10, blank=True)  # A, B, C, Distinction, etc.
    score_percentage = models.PositiveIntegerField(default=0)
    duration_hours = models.PositiveIntegerField(default=0)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-issue_date']
        unique_together = ['student', 'course']
    
    def __str__(self):
        return f"{self.student.username} - {self.course.title} Certificate"
    
    def generate_certificate_number(self):
        """Generate unique certificate number"""
        import random
        import string
        prefix = self.certificate_type[:3].upper()
        year = self.issue_date.strftime('%Y')
        random_chars = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        return f"{prefix}-{year}-{random_chars}"
    
    def generate_verification_code(self):
        """Generate unique verification code"""
        import random
        import string
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
    
    def save(self, *args, **kwargs):
        if not self.certificate_number:
            self.certificate_number = self.generate_certificate_number()
        if not self.verification_code:
            self.verification_code = self.generate_verification_code()
        if not self.verification_url:
            self.verification_url = f"/certificates/verify/{self.verification_code}/"
        super().save(*args, **kwargs)

class CertificateTemplate(models.Model):
    """Certificate design templates"""
    
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    template_type = models.CharField(max_length=50, choices=Certificate.TYPE_CHOICES)
    
    # Design fields
    background_color = models.CharField(max_length=20, default='#1a3c6e')
    text_color = models.CharField(max_length=20, default='#ffffff')
    accent_color = models.CharField(max_length=20, default='#e8a838')
    font_family = models.CharField(max_length=100, default='Georgia, serif')
    
    # Content
    header_text = models.CharField(max_length=200, default='Certificate of Completion')
    body_text = models.TextField(default='This certifies that [student_name] has successfully completed the course [course_name]')
    footer_text = models.CharField(max_length=200, default='SkillsContinua - Building communities through skills')
    
    # Images
    logo = models.ImageField(upload_to='certificates/logos/', blank=True)
    signature_image = models.ImageField(upload_to='certificates/signatures/', blank=True)
    background_image = models.ImageField(upload_to='certificates/backgrounds/', blank=True)
    
    is_active = models.BooleanField(default=True)
    is_default = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class CertificateVerification(models.Model):
    """Track certificate verification requests"""
    
    certificate = models.ForeignKey(Certificate, on_delete=models.CASCADE, related_name='verifications')
    verified_by = models.CharField(max_length=100, blank=True)
    verification_date = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)
    is_successful = models.BooleanField(default=True)
    
    def __str__(self):
        return f"Verification for {self.certificate} on {self.verification_date}"