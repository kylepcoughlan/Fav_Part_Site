import random
from django.shortcuts import render
from .models import Post

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
