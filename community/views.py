from django.shortcuts import render
from .models import Post
def feed(request):
    posts = Post.objects.order_by('-created_at')[:50]
    return render(request, 'community/feed.html', {'posts': posts})