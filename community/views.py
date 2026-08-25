from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

def feed(request):
    posts = Post.objects.order_by('-created_at')[:100]
    featured = Post.objects.filter(is_featured=True).order_by('-created_at')[:5]
    return render(request, 'community/feed.html', {'posts': posts, 'featured': featured})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            p = form.save(commit=False)
            p.author = request.user
            p.save()
            return redirect('/en/community/')
    else:
        form = PostForm()
    return render(request, 'community/create.html', {'form': form})