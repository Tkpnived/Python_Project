from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogPostForm
from django.contrib.auth import login, logout as django_logout ,authenticate
from django.contrib import messages 
from .forms import RegisterForm


def blog_list(request):
    posts = BlogPost.objects.all().order_by('-publication_date')
    return render(request, 'blog/Blog.html', {'posts': posts})


def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/details.html', {'post': post})


@login_required
def blog_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog_list')
    else:
        form = BlogPostForm()
    return render(request, 'blog/form.html', {'form': form})


@login_required
def blog_update(request, pk):
    post = get_object_or_404(BlogPost, pk=pk, author=request.user)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blog/form.html', {'form': form})


@login_required
def blog_delete(request, pk):
    post = get_object_or_404(BlogPost, pk=pk, author=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('blog_list')
    return render(request, 'blog/conf_delete.html', {'post': post})



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  
            user.save()
            login(request, user)  
            return redirect('blog_list')
    else:
        form = RegisterForm()
    return render(request, 'Registration/register.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            
            login(request, user)
            return redirect('blog_list')
        else:
            
            messages.error(request, 'Invalid username or password.')
            return render(request, 'registration/login.html')
    else:
        
        return render(request, 'registration/login.html')

def custom_logout(request):
    django_logout(request) 
    return redirect('login')  