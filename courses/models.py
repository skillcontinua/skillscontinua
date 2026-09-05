from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import get_language

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100)
    pillar = models.CharField(max_length=100, unique=True, blank=True)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True)
    order = models.IntegerField(default=0)

    name_en = models.CharField(max_length=100, blank=True, null=True)
    name_fr = models.CharField(max_length=100, blank=True, null=True)
    name_es = models.CharField(max_length=100, blank=True, null=True)
    name_pt = models.CharField(max_length=100, blank=True, null=True)
    name_sw = models.CharField(max_length=100, blank=True, null=True)
    name_ar = models.CharField(max_length=100, blank=True, null=True)

    description_en = models.TextField(blank=True, null=True)
    description_fr = models.TextField(blank=True, null=True)
    description_es = models.TextField(blank=True, null=True)
    description_pt = models.TextField(blank=True, null=True)
    description_sw = models.TextField(blank=True, null=True)
    description_ar = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def _lang_base(self, lang):
        if not lang:
            return 'en'
        return lang.split('-')[0].lower()

    def get_name(self, lang='en'):
        lang = self._lang_base(lang)
        if lang == 'en':
            return self.name
        value = getattr(self, f'name_{lang}', None)
        return value if value else self.name

    def get_description(self, lang='en'):
        lang = self._lang_base(lang)
        if lang == 'en':
            return self.description
        value = getattr(self, f'description_{lang}', None)
        return value if value else self.description

    @property
    def translated_name(self):
        return self.get_name(get_language() or 'en')

    @property
    def translated_description(self):
        return self.get_description(get_language() or 'en')

class Course(models.Model):
    LEVEL_CHOICES = [('beginner','Beginner'),('intermediate','Intermediate'),('advanced','Advanced')]
    AGE_GROUP_CHOICES = [('child','Child (6-12)'),('teen','Teen (13-17)'),('adult','Adult (18+)'),('all','All Ages')]
    APPROACH_CHOICES = [('pedagogic','Pedagogic'),('andragogic','Andragogic'),('heutagogic','Heutagogic'),('cybergogic','Cybergogic')]

    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses')
    description = models.TextField()
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    age_group = models.CharField(max_length=20, choices=AGE_GROUP_CHOICES)
    learning_approach = models.CharField(max_length=20, choices=APPROACH_CHOICES)
    duration_hours = models.PositiveIntegerField(default=10)
    learning_objectives = models.TextField(blank=True)
    prerequisites = models.TextField(blank=True)
    target_audience = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)

    title_en = models.CharField(max_length=200, blank=True, null=True)
    title_fr = models.CharField(max_length=200, blank=True, null=True)
    title_es = models.CharField(max_length=200, blank=True, null=True)
    title_pt = models.CharField(max_length=200, blank=True, null=True)
    title_sw = models.CharField(max_length=200, blank=True, null=True)
    title_ar = models.CharField(max_length=200, blank=True, null=True)

    description_en = models.TextField(blank=True, null=True)
    description_fr = models.TextField(blank=True, null=True)
    description_es = models.TextField(blank=True, null=True)
    description_pt = models.TextField(blank=True, null=True)
    description_sw = models.TextField(blank=True, null=True)
    description_ar = models.TextField(blank=True, null=True)

    learning_objectives_en = models.TextField(blank=True, null=True)
    learning_objectives_fr = models.TextField(blank=True, null=True)
    learning_objectives_es = models.TextField(blank=True, null=True)
    learning_objectives_pt = models.TextField(blank=True, null=True)
    learning_objectives_sw = models.TextField(blank=True, null=True)
    learning_objectives_ar = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['category', 'level', 'title']

    def __str__(self):
        return self.title

    def _lang_base(self, lang):
        if not lang:
            return 'en'
        return lang.split('-')[0].lower()

    def get_title(self, lang='en'):
        lang = self._lang_base(lang)
        if lang == 'en':
            return self.title
        value = getattr(self, f'title_{lang}', None)
        return value if value else self.title

    def get_description(self, lang='en'):
        lang = self._lang_base(lang)
        if lang == 'en':
            return self.description
        value = getattr(self, f'description_{lang}', None)
        return value if value else self.description

    def get_learning_objectives(self, lang='en'):
        lang = self._lang_base(lang)
        if lang == 'en':
            return self.learning_objectives
        value = getattr(self, f'learning_objectives_{lang}', None)
        return value if value else self.learning_objectives

    @property
    def translated_title(self):
        return self.get_title(get_language() or 'en')

    @property
    def translated_description(self):
        return self.get_description(get_language() or 'en')

    @property
    def translated_objectives(self):
        return self.get_learning_objectives(get_language() or 'en')

    @property
    def total_lessons(self):
        return self.lessons.count()

    @property
    def total_enrollments(self):
        return self.enrollments.count()

# === SINGLE MERGED LESSON - ABIAPOLY READY: Video + Audio + PDF ===
class Lesson(models.Model):
    CONTENT_TYPES = [
        ('video', 'Video - Practical Demo'),
        ('audio', 'Audio - Theory / Igbo Explanation'),
        ('pdf', 'PDF - Manual / Diagram'),
        ('text', 'Text - Step by Step'),
    ]
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    duration_minutes = models.PositiveIntegerField(default=30)
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPES, default='video')
    video_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True, help_text="For ABIAPOLY - use YouTube to save server cost")
    video_file = models.FileField(upload_to='lessons/videos/', blank=True, null=True)
    audio_file = models.FileField(upload_to='lessons/audios/', blank=True, null=True)
    pdf_file = models.FileField(upload_to='lessons/pdfs/', blank=True, null=True)
    is_free_preview = models.BooleanField(default=False)

    title_en = models.CharField(max_length=200, blank=True, null=True)
    title_fr = models.CharField(max_length=200, blank=True, null=True)
    title_es = models.CharField(max_length=200, blank=True, null=True)
    title_pt = models.CharField(max_length=200, blank=True, null=True)
    title_sw = models.CharField(max_length=200, blank=True, null=True)
    title_ar = models.CharField(max_length=200, blank=True, null=True)

    content_en = models.TextField(blank=True, null=True)
    content_fr = models.TextField(blank=True, null=True)
    content_es = models.TextField(blank=True, null=True)
    content_pt = models.TextField(blank=True, null=True)
    content_sw = models.TextField(blank=True, null=True)
    content_ar = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

    def _lang_base(self, lang):
        if not lang:
            return 'en'
        return lang.split('-')[0].lower()

    def get_title(self, lang='en'):
        lang = self._lang_base(lang)
        if lang == 'en':
            return self.title
        value = getattr(self, f'title_{lang}', None)
        return value if value else self.title

    def get_content(self, lang='en'):
        lang = self._lang_base(lang)
        if lang == 'en':
            return self.content
        value = getattr(self, f'content_{lang}', None)
        return value if value else self.content

    @property
    def translated_title(self):
        return self.get_title(get_language() or 'en')

    @property
    def translated_content(self):
        return self.get_content(get_language() or 'en')

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)
        if self.title and not self.title_fr:
            try:
                from deep_translator import GoogleTranslator
                langs = ['fr','es','pt','sw','ar']
                updated = False
                for lang in langs:
                    field_name = f'title_{lang}'
                    if not getattr(self, field_name):
                        try:
                            trans = GoogleTranslator(source='en', target=lang).translate(self.title)
                            setattr(self, field_name, trans)
                            updated = True
                        except:
                            pass
                if updated:
                    super().save(update_fields=[f'title_{l}' for l in langs])
            except ImportError:
                pass

class Enrollment(models.Model):
    STATUS_CHOICES = [('enrolled','Enrolled'),('in_progress','In Progress'),('completed','Completed'),('dropped','Dropped')]
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

class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progress')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='progress')
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['user', 'lesson']
        ordering = ['-completed_at']

    def __str__(self):
        status = "OK" if self.completed else "NO"
        return f"{self.user.username} - {self.lesson.title} [{status}]"

# Import quiz models AFTER Lesson is defined
try:
    from.quiz_models import Quiz
except:
    pass