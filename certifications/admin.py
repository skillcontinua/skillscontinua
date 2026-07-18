from django.contrib import admin
from .models import Certificate, CertificateTemplate, CertificateVerification

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('certificate_number', 'student', 'course', 'issue_date', 'is_verified')
    list_filter = ('certificate_type', 'is_verified', 'issue_date')
    search_fields = ('certificate_number', 'student__username', 'course__title', 'verification_code')
    readonly_fields = ('certificate_number', 'verification_code', 'issue_date')
    
    fieldsets = (
        ('Certificate Info', {
            'fields': ('student', 'course', 'certificate_type', 'certificate_number', 'verification_code')
        }),
        ('Details', {
            'fields': ('issue_date', 'expiry_date', 'grade', 'score_percentage', 'duration_hours')
        }),
        ('Verification', {
            'fields': ('is_verified', 'verification_url')
        }),
    )

@admin.register(CertificateTemplate)
class CertificateTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'template_type', 'is_active', 'is_default')
    list_filter = ('template_type', 'is_active', 'is_default')
    search_fields = ('name', 'description')

@admin.register(CertificateVerification)
class CertificateVerificationAdmin(admin.ModelAdmin):
    list_display = ('certificate', 'verification_date', 'is_successful')
    list_filter = ('is_successful', 'verification_date')
    search_fields = ('certificate__certificate_number', 'verified_by')