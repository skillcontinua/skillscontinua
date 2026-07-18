from django.contrib import admin
from .models import Quiz, Question, Answer, QuizAttempt, LearnerAnswer, Certificate


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 4
    fields = ('answer_text', 'is_correct')


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1
    fields = ('question_text', 'question_type', 'order', 'marks', 'explanation')


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'pass_mark', 'time_limit_minutes', 'is_active')
    list_filter = ('is_active',)
    inlines = [QuestionInline]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'quiz', 'question_type', 'order', 'marks')
    list_filter = ('question_type', 'quiz')
    inlines = [AnswerInline]


@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ('learner', 'quiz', 'score_percent', 'status', 'started_at')
    list_filter = ('status',)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('certificate_number', 'learner', 'course', 'score_percent', 'issued_at', 'is_valid')
    list_filter = ('is_valid',)
    search_fields = ('certificate_number', 'learner__username')


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('answer_text', 'question', 'is_correct')
    list_filter = ('is_correct',)