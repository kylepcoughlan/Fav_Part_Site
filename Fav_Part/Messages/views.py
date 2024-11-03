import random
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Post
from django.http import JsonResponse

def home(request):
    # Fetch all posts
    posts = list(Post.objects.all())
    
    # Get up to 36 random posts
    random_posts = random.sample(posts, min(len(posts), 36))
    
    return render(request, 'home.html', {'posts': random_posts})
    
    
#view for creating a post 
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

def toggle_like(request, post_id):
    if request.method == "POST":
        post = Post.objects.get(id=post_id)

        # Toggle like count
        post.likes += 1
        post.save()

        return JsonResponse({
            "success": True,
            "likes": post.likes
        })
    
    return JsonResponse({"success": False, "error": "Invalid request"})

def get_post_data(request, post_id):
    post = get_object_or_404(Post, incremental_id=post_id)
    post_data = {
        'id': post.incremental_id,
        'title': post.title,
        'content': post.content,
        'created_at': post.created_at.strftime('%Y-%m-%d %H:%M:%S'),
        'likes': post.likes,
    }
    return JsonResponse(post_data)
