from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from supabase import create_client
from io import BytesIO

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html', {'post': post})

SUPABASE_URL = 'https://ltsatdtrtwnvkebvtchq.supabase.co'  # Example: 'https://yourproject.supabase.co'
SUPABASE_API_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imx0c2F0ZHRydHdudmtlYnZ0Y2hxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzI5NTQwNjQsImV4cCI6MjA0ODUzMDA2NH0.A6IxQCXw7x6b4WR4jnlJO-Vui_Dv-T8BCjZVWZpmbEA'
supabase = create_client(SUPABASE_URL, SUPABASE_API_KEY)

@login_required  # Only logged-in users can create a post
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)  # Handle file uploads
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Automatically assign the logged-in user as the author

            # Handle file upload to Supabase
            image = request.FILES.get('image')  # Assuming 'image' is the field name in the form
            if image:
                # Define a path for the file in Supabase storage
                path = f'images/{image.name}'  # Save the image with its original name

                # Upload the file directly to Supabase (no need to wrap it in BytesIO)
                response = supabase.storage.from_('your-bucket-name').upload(path, image)

                # Check if there was an error in the upload
                if response.get('error'):
                    # Handle upload error
                    return HttpResponse(f"Upload error: {response['error']['message']}")

                # After a successful upload, save the file URL in the post model
                post.image_url = f'{SUPABASE_URL}/storage/v1/object/public/your-bucket-name/{path}'

            post.save()  # Save the post to the database
            return redirect('blog')  # Redirect to the list of blog posts

    else:
        form = PostForm()

    return render(request, 'blog/create_post.html', {'form': form})
