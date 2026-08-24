from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()

class Post(models.Model):
    TYPE=[('blog','Blog'),('forum','Forum Question'),('podcast','Podcast'),('reel','Skill Reel (Video)'),('thread','Thread/Story'),('achievement','Achievement')]
    author=models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    post_type=models.CharField(max_length=20,choices=TYPE, default='blog')
    title=models.CharField(max_length=200)
    content=models.TextField()
    video_url=models.URLField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    is_featured=models.BooleanField(default=False)
    def __str__(self): return f"{self.post_type}: {self.title[:40]}"