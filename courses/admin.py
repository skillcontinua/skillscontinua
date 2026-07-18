from django.contrib import admin
from .models import Category, Course, Lesson, Enrollment

# Simple registration without custom admin to avoid errors
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Enrollment)