import random
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Post
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json 
import logging

def home(request):
    # Fetch all posts
    posts = list(Post.objects.all())
    
    # Get up to 36 random posts
    random_posts = random.sample(posts, min(len(posts), 36))
    
    return render(request, 'home.html', {'posts': random_posts})
    
    
@csrf_exempt
def create_post(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title', '')
        content = data.get('content', '')
        signed = data.get('signed', '')

        # Log incoming data
        print(f"Creating post with title: {title}, content: {content}, signed: {signed}")

        # Create a new Post instance
        post = Post(title=title, content=content, signed=signed)
        post.save()
        
        print(f"Post created with incremental ID: {post.incremental_id}")
        return JsonResponse({'success': True, 'post_id': post.incremental_id})

    print("Invalid request method")
    return JsonResponse({'success': False, 'error': 'Invalid request method'})



@csrf_exempt
def toggle_like(request, post_id):
    if request.method == 'POST':
        logger.info("Received POST request to toggle like for post ID: %s", post_id)
        try:
            post = get_object_or_404(Post, id=post_id)
            data = json.loads(request.body)
            is_liked = data.get('isLiked', False)

            if is_liked:
                post.likes += 1
            else:
                post.likes = max(0, post.likes - 1)

            post.save()
            return JsonResponse({"success": True, "likes": post.likes})
        except Post.DoesNotExist:
            return JsonResponse({"success": False, "error": "Post not found"})
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
