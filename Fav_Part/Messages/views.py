from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

#homepage that will display all the message s
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

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
