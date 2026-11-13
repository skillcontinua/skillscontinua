# courses/admin.py
from django.contrib import admin
from .models import Category, Course, Lesson, Enrollment, UserProgress

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'pillar', 'order')
    search_fields = ('name', 'pillar')
    ordering = ('order', 'name')

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 1
    fields = ('title', 'order', 'duration_minutes', 'content_type', 'youtube_url', 'content', 'is_free_preview')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'level', 'learning_approach', 'duration_hours', 'is_active', 'featured')
    list_filter = ('level', 'learning_approach', 'is_active', 'featured', 'category')
    search_fields = ('title', 'description', 'learning_objectives')
    inlines = [LessonInline]
    list_editable = ('is_active', 'featured')
    ordering = ('category', 'level', 'title')

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order', 'duration_minutes', 'content_type', 'is_free_preview')
    list_filter = ('content_type', 'is_free_preview', 'course__category')
    search_fields = ('title', 'content')

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'status', 'progress_percent', 'started_at')
    list_filter = ('status', 'certificate_issued')
    search_fields = ('student__username', 'course__title')

@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'lesson', 'completed', 'completed_at')
    list_filter = ('completed',)
    search_fields = ('user__username', 'lesson__title')