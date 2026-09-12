from django.db import models
from django.conf import settings

class Contributor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    naira_earned = models.IntegerField(default=0)
    full_name = models.CharField(max_length=100, blank=True, help_text="Name for Africa & World")
    country = models.CharField(max_length=100, blank=True, default="Nigeria")
    is_verified = models.BooleanField(default=False)
    def __str__(self): return f"{self.user.username} - {self.points}pts = ₦{self.naira_earned}"

class Contribution(models.Model):
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, choices=[('course','Course'),('translation','Translation'),('forum','Forum Answer')])
    title = models.CharField(max_length=200)
    approved = models.BooleanField(default=False)
    points_given = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"{self.title} - {self.type}"

class Subscription(models.Model):
    email = models.EmailField()
    amount = models.IntegerField(default=2000)
    paid = models.BooleanField(default=False)
    paystack_ref = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"{self.email} - ₦{self.amount} - {'PAID' if self.paid else 'PENDING'}"