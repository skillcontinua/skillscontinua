from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from.models import Post, Like
from.forms import PostForm, CommentForm

def feed(request):
    type_filter = request.GET.get('type')
    posts = Post.objects.all()
    if type_filter:
        posts = posts.filter(post_type=type_filter)
    posts = posts.order_by('-created_at')[:100]
    featured = Post.objects.filter(is_featured=True).order_by('-created_at')[:3]
    cform = CommentForm()
    return render(request, 'community/feed.html', {'posts': posts, 'featured': featured, 'cform': cform, 'active_type': type_filter})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            p = form.save(commit=False)
            p.author = request.user
            p.save()
            return redirect('/en/community/')
    else:
        form = PostForm()
    return render(request, 'community/create.html', {'form': form})

@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like, created = Like.objects.get_or_create(post=post, user=request.user)
    if not created:
        like.delete()
        post.likes_count = max(0, post.likes_count-1)
    else:
        post.likes_count += 1
    post.save()
    return redirect(f'/en/community/#{post.id}')

@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            post.comments.create(author=request.user, text=text)
    return redirect(f'/en/community/#{post.id}')

def embed_youtube(url):
    if not url: return None
    if 'youtu.be' in url:
        return url.split('/')[-1].split('?')[0]
    if 'v=' in url:
        return url.split('v=')[1].split('&')[0]
    return None