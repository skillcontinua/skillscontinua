from django.db import models
from django.contrib.auth import get_user_model
from courses.models import Course
User=get_user_model()

class Post(models.Model):
    TYPE=[('blog','Blog'),('forum','Forum Question'),('podcast','Podcast'),('reel','Skill Reel (Video)'),('thread','Thread/Story'),('achievement','Achievement')]
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    post_type=models.CharField(max_length=20,choices=TYPE)
    title=models.CharField(max_length=200)
    content=models.TextField()
    course=models.ForeignKey(Course,on_delete=models.SET_NULL,null=True,blank=True)
    video_url=models.URLField(blank=True)
    audio_url=models.URLField(blank=True)
    image=models.ImageField(upload_to='community/',blank=True)
    likes=models.ManyToManyField(User,related_name='liked_posts',blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    is_featured=models.BooleanField(default=False)
    def __str__(self): return f"{self.post_type}: {self.title[:40]}"

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)