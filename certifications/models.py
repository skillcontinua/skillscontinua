from django.db import models
from accounts.models import User
from courses.models import Course


class Quiz(models.Model):
    course = models.OneToOneField(
        Course, on_delete=models.CASCADE, related_name='quiz'
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    pass_mark = models.PositiveIntegerField(default=60)
    time_limit_minutes = models.PositiveIntegerField(default=30)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Quiz: {self.title}"

    class Meta:
        verbose_name_plural = 'Quizzes'


class Question(models.Model):
    QUESTION_TYPE_CHOICES = [
        ('multiple_choice', 'Multiple Choice'),
        ('true_false', 'True or False'),
    ]
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name='questions'
    )
    question_text = models.TextField()
    question_type = models.CharField(
        max_length=20,
        choices=QUESTION_TYPE_CHOICES,
        default='multiple_choice'
    )
    order = models.PositiveIntegerField(default=1)
    marks = models.PositiveIntegerField(default=1)
    explanation = models.TextField(
        blank=True,
        help_text='Shown to learner after answering — use this to reinforce learning'
    )

    def __str__(self):
        return f"Q{self.order}: {self.question_text[:60]}"

    class Meta:
        ordering = ['order']


class Answer(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='answers'
    )
    answer_text = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        marker = 'CORRECT' if self.is_correct else 'wrong'
        return f"[{marker}] {self.answer_text[:50]}"


class QuizAttempt(models.Model):
    STATUS_CHOICES = [
        ('in_progress', 'In Progress'),
        ('distinction', 'Distinction'),
        ('merit', 'Merit'),
        ('pass', 'Pass'),
        ('not_yet', 'Not Yet — Keep Going'),
    ]
    learner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='quiz_attempts'
    )
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name='attempts'
    )
    score_percent = models.PositiveIntegerField(default=0)
    status = models.CharField(
        max_length=15, choices=STATUS_CHOICES, default='in_progress'
    )
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    total_marks = models.PositiveIntegerField(default=0)
    marks_obtained = models.PositiveIntegerField(default=0)
    attempt_number = models.PositiveIntegerField(default=1)

    def get_rating(self):
        if self.score_percent >= 90:
            return 'Distinction'
        elif self.score_percent >= 75:
            return 'Merit'
        elif self.score_percent >= 60:
            return 'Pass'
        else:
            return 'Not Yet'

    def get_rating_colour(self):
        if self.score_percent >= 90:
            return 'gold'
        elif self.score_percent >= 75:
            return 'silver'
        elif self.score_percent >= 60:
            return 'bronze'
        else:
            return 'grey'

    def __str__(self):
        return f"{self.learner.username} — {self.quiz.title} ({self.score_percent}%)"

    class Meta:
        ordering = ['-started_at']


class LearnerAnswer(models.Model):
    attempt = models.ForeignKey(
        QuizAttempt, on_delete=models.CASCADE, related_name='learner_answers'
    )
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_answer = models.ForeignKey(
        Answer, on_delete=models.CASCADE, null=True, blank=True
    )
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.attempt.learner.username} — {self.question}"


class Certificate(models.Model):
    RATING_CHOICES = [
        ('distinction', 'Distinction'),
        ('merit', 'Merit'),
        ('pass', 'Pass'),
    ]
    learner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='certificates'
    )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='certificates'
    )
    quiz_attempt = models.ForeignKey(
        QuizAttempt, on_delete=models.CASCADE, null=True, blank=True
    )
    certificate_number = models.CharField(max_length=20, unique=True)
    score_percent = models.PositiveIntegerField(default=0)
    rating = models.CharField(
        max_length=15,
        choices=RATING_CHOICES,
        default='pass'
    )
    issued_at = models.DateTimeField(auto_now_add=True)
    is_valid = models.BooleanField(default=True)

    def get_rating_display_colour(self):
        colours = {
            'distinction': '#FFD700',
            'merit': '#C0C0C0',
            'pass': '#CD7F32',
        }
        return colours.get(self.rating, '#CD7F32')

    def __str__(self):
        return f"SC-{self.certificate_number} — {self.learner.username} — {self.course.title} ({self.rating.upper()})"

    def save(self, *args, **kwargs):
        if not self.certificate_number:
            import random, string
            code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            self.certificate_number = f"SC-{code}"
        # Auto-set rating from score
        if self.score_percent >= 90:
            self.rating = 'distinction'
        elif self.score_percent >= 75:
            self.rating = 'merit'
        else:
            self.rating = 'pass'
        super().save(*args, **kwargs)

    class Meta:
        unique_together = ['learner', 'course']
