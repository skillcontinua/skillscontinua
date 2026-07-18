from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    PILLAR_CHOICES = [
        ('literacy', 'Foundational Literacy'),
        ('computer', 'Computer Literacy'),
        ('vocational', 'Vocational Trades'),
        ('certification', 'Certifications'),
        ('life_skills', 'Life Skills'),
        ('primary', 'Primary Education'),
        ('secondary_arts', 'Secondary Education - Arts'),
        ('secondary_commercial', 'Secondary Education - Commercial'),
        ('secondary_science', 'Secondary Education - Science'),
        ('secondary_technical', 'Secondary Education - Technical'),
        ('secondary_trade', 'Secondary Education - Trade'),
        ('building', 'Building Construction'),
        ('housing', 'Housing and Appliances'),
        ('electrical', 'Electrical Installation'),
        ('auto_motorcycle', 'Automotive - Motorcycles'),
        ('auto_cars', 'Automotive - Cars and Vans'),
        ('auto_heavy', 'Automotive - Heavy Vehicles'),
        ('beauty_hair', 'Hair Care and Styling'),
        ('beauty_makeup', 'Makeup and Beauty'),
        ('it', 'Information Technology'),
        ('digital', 'Digital Skills'),
        ('carpentry', 'Carpentry and Woodwork'),
        ('welding', 'Welding and Metalwork'),
        ('agriculture', 'Agriculture and Farming'),
        ('tailoring', 'Tailoring and Fashion'),
        ('financial', 'Financial Literacy'),
    ]
    
    name = models.CharField(max_length=100)
    pillar = models.CharField(max_length=50, choices=PILLAR_CHOICES, unique=True)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order', 'name']
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
    
    def get_name(self, lang='en'):
        if lang == 'en':
            return self.name
        field_name = f'name_{lang}'
        value = getattr(self, field_name, '')
        return value if value else self.name
    
    def get_description(self, lang='en'):
        if lang == 'en':
            return self.description
        field_name = f'description_{lang}'
        value = getattr(self, field_name, '')
        return value if value else self.description


class Course(models.Model):
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]
    
    AGE_GROUP_CHOICES = [
        ('child', 'Child (6-12)'),
        ('teen', 'Teen (13-17)'),
        ('adult', 'Adult (18+)'),
        ('all', 'All Ages'),
    ]
    
    APPROACH_CHOICES = [
        ('pedagogic', 'Pedagogic (Child-focused)'),
        ('andragogic', 'Andragogic (Adult-focused)'),
        ('heutagogic', 'Heutagogic (Self-determined)'),
        ('cybergogic', 'Cybergogic (Tech-enhanced)'),
    ]
    
    # Basic fields
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses')
    description = models.TextField()
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    age_group = models.CharField(max_length=20, choices=AGE_GROUP_CHOICES)
    learning_approach = models.CharField(max_length=20, choices=APPROACH_CHOICES)
    duration_hours = models.PositiveIntegerField(default=10)
    
    # Additional fields
    learning_objectives = models.TextField(blank=True)
    prerequisites = models.TextField(blank=True)
    target_audience = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['category', 'level', 'title']
    
    def __str__(self):
        return self.title
    
    def get_title(self, lang='en'):
        if lang == 'en':
            return self.title
        field_name = f'title_{lang}'
        value = getattr(self, field_name, '')
        return value if value else self.title
    
    def get_description(self, lang='en'):
        if lang == 'en':
            return self.description
        field_name = f'description_{lang}'
        value = getattr(self, field_name, '')
        return value if value else self.description
    
    @property
    def total_lessons(self):
        return self.lessons.count()
    
    @property
    def total_enrollments(self):
        return self.enrollments.count()


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=200)
    content = models.TextField()
    order = models.IntegerField(default=0)
    duration_minutes = models.PositiveIntegerField(default=30)
    video_url = models.URLField(blank=True)
    is_free_preview = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title
    
    def get_title(self, lang='en'):
        if lang == 'en':
            return self.title
        field_name = f'title_{lang}'
        value = getattr(self, field_name, '')
        return value if value else self.title
    
    def get_content(self, lang='en'):
        if lang == 'en':
            return self.content
        field_name = f'content_{lang}'
        value = getattr(self, field_name, '')
        return value if value else self.content


class Enrollment(models.Model):
    STATUS_CHOICES = [
        ('enrolled', 'Enrolled'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('dropped', 'Dropped'),
    ]
    
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='enrolled')
    progress_percent = models.PositiveIntegerField(default=0)
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    certificate_issued = models.BooleanField(default=False)
    certificate_number = models.CharField(max_length=100, blank=True)
    certificate_issued_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        unique_together = ['student', 'course']
    
    def __str__(self):
        return f"{self.student.username} - {self.course.title}"
    
    @property
    def is_completed(self):
        return self.status == 'completed'