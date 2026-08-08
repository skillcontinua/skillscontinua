from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q
from .models import BlogPost, Category, Tag, Comment, ForumTopic, ForumReply, ContributorProfile, Feedback
from .forms import BlogPostForm, CommentForm, ForumTopicForm, ForumReplyForm, FeedbackForm

def blog_home(request):
    posts = BlogPost.objects.filter(status='published').order_by('-published_at')
    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = {
        'posts': posts,
        'categories': categories,
        'tags': tags,
    }
    return render(request, 'blog/home.html', context)

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, status='published')
    post.views += 1
    post.save()
    comments = post.comments.filter(is_approved=True)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, 'Comment added successfully!')
            return redirect('blog:detail', slug=post.slug)
    else:
        form = CommentForm()
    
    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }
    return render(request, 'blog/detail.html', context)

def forum_home(request):
    topics = ForumTopic.objects.all().order_by('-is_pinned', '-created_at')
    context = {'topics': topics}
    return render(request, 'blog/forum_home.html', context)

def forum_topic(request, slug):
    topic = get_object_or_404(ForumTopic, slug=slug)
    topic.views += 1
    topic.save()
    replies = topic.replies.all()
    
    if request.method == 'POST':
        form = ForumReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.topic = topic
            reply.author = request.user
            reply.save()
            topic.replies_count += 1
            topic.save()
            messages.success(request, 'Reply added successfully!')
            return redirect('blog:forum_topic', slug=topic.slug)
    else:
        form = ForumReplyForm()
    
    context = {
        'topic': topic,
        'replies': replies,
        'form': form,
    }
    return render(request, 'blog/forum_topic.html', context)

@login_required
def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_at = timezone.now()
            post.save()
            form.save_m2m()
            messages.success(request, 'Post created successfully!')
            return redirect('blog:detail', slug=post.slug)
    else:
        form = BlogPostForm()
    return render(request, 'blog/create_post.html', {'form': form})

@login_required
def create_topic(request):
    if request.method == 'POST':
        form = ForumTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.author = request.user
            topic.save()
            messages.success(request, 'Topic created successfully!')
            return redirect('blog:forum_topic', slug=topic.slug)
    else:
        form = ForumTopicForm()
    return render(request, 'blog/create_topic.html', {'form': form})

def contributors_list(request):
    contributors = ContributorProfile.objects.filter(is_active=True)
    return render(request, 'blog/contributors.html', {'contributors': contributors})

@login_required
def feedback_submit(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            messages.success(request, 'Feedback submitted successfully!')
            return redirect('blog:feedback')
    else:
        form = FeedbackForm()
    return render(request, 'blog/feedback.html', {'form': form})

def category_view(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = BlogPost.objects.filter(category=category, status='published')
    return render(request, 'blog/category.html', {'category': category, 'posts': posts})

def tag_view(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = BlogPost.objects.filter(tags=tag, status='published')
    return render(request, 'blog/tag.html', {'tag': tag, 'posts': posts})