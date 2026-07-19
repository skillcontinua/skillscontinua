from modeltranslation.translator import register, TranslationOptions
from .models import Category, Course, Lesson

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'learning_objectives', 'prerequisites', 'target_audience')

@register(Lesson)
class LessonTranslationOptions(TranslationOptions):
    fields = ('title', 'content')