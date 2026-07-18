from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    """Custom User model for SkillsContinua"""
    
    ROLE_CHOICES = [
        ('learner', 'Learner'),
        ('instructor', 'Instructor'),
        ('mentor', 'Mentor'),
        ('admin', 'Administrator'),
    ]
    
    AGE_GROUP_CHOICES = [
        ('child', 'Child (6-12)'),
        ('teen', 'Teen (13-17)'),
        ('adult', 'Adult (18+)'),
        ('senior', 'Senior (55+)'),
    ]
    
    # Basic profile fields
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    
    # Location and community
    country = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    community = models.CharField(max_length=200, blank=True, null=True)
    
    # User categorization
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='learner')
    age_group = models.CharField(max_length=20, choices=AGE_GROUP_CHOICES, blank=True, null=True)
    
    # Learning preferences
    preferred_language = models.CharField(max_length=10, default='en')
    learning_approach = models.CharField(max_length=20, blank=True, null=True)
    
    # Timestamps
    date_joined = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    # Additional fields for tracking
    total_courses_completed = models.PositiveIntegerField(default=0)
    total_certificates_earned = models.PositiveIntegerField(default=0)
    
    class Meta:
        db_table = 'auth_user'
        verbose_name = _('User')
        verbose_name_plural = _('Users')
    
    def __str__(self):
        return self.username
    
    @property
    def full_name(self):
        """Return the user's full name"""
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.username
    
    @property
    def is_learner(self):
        """Check if user is a learner"""
        return self.role == 'learner'
    
    @property
    def is_instructor(self):
        """Check if user is an instructor"""
        return self.role == 'instructor'
    
    @property
    def is_mentor(self):
        """Check if user is a mentor"""
        return self.role == 'mentor'