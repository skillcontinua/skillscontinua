from django.contrib import admin
from .models import Category, Course, Lesson, Enrollment

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'content_type', 'order', 'is_free_preview']
    list_filter = ['content_type', 'is_free_preview']
    search_fields = ['title']
    list_editable = ['order']