from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    """Custom admin interface for User model"""
    
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_active')
    list_filter = ('role', 'is_active', 'age_group')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'bio')}),
        ('Location', {'fields': ('country', 'region', 'community')}),
        ('User Details', {'fields': ('role', 'age_group', 'profile_photo')}),
        ('Learning', {'fields': ('preferred_language', 'learning_approach')}),
        ('Statistics', {'fields': ('total_courses_completed', 'total_certificates_earned')}),
        ('Important dates', {'fields': ('last_login', 'date_joined', 'last_active')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'role', 'age_group'),
        }),
    )

# Register the custom User model
admin.site.register(User, CustomUserAdmin)