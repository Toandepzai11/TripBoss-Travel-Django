from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html', {'post': post})
@login_required  # Only logged-in users can create a post
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)  # Handle file uploads
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Automatically assign the logged-in user as the author
            post.save()
            return redirect('blog')  # Redirect to the list of blog posts
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})