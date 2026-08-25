from django.db import models
from django.conf import settings

POST_TYPES = [
    ('blog', '📝 Blog'),
    ('reel', '🎬 Reel'),
    ('thread', '🧵 Thread'),
    ('forum', '💬 Forum Question'),
    ('achievement', '🏆 Achievement'),
    ('job', '💼 Job / Opportunity'),
    ('podcast', '🎙️ Podcast'),
    ('poll', '📊 Poll'),
    ('event', '📅 Event'),
]

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    post_type = models.CharField(max_length=20, choices=POST_TYPES, default='blog')
    title = models.CharField(max_length=200)
    content = models.TextField()
    video_url = models.URLField(blank=True, help_text="YouTube / Loom / Drive link for Reel/Podcast")
    image = models.ImageField(upload_to='community/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    likes_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post','user')