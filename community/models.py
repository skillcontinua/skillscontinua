from django.db import models
from django.conf import settings

class Post(models.Model):
    POST_TYPES = [
        ('blog','Blog'),
        ('forum','Forum Question'),
        ('podcast','Podcast'),
        ('reel','Skill Reel (Video)'),
        ('thread','Thread/Story'),
        ('achievement','Achievement'),
    ]
    post_type = models.CharField(max_length=20, choices=POST_TYPES, default='blog')
    title = models.CharField(max_length=200)
    content = models.TextField()
    video_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title