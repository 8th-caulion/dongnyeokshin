from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone

# Create your views here.
def main(request):
    blogs = Blog.objects
    return render(request, 'main.html', {'blogs':blogs})

def profile(request):
    return render(request, 'profile.html')

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'details':details})
