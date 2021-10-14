from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


def index(request):
    return HttpResponse("Hello, world. You're at the blog index page.")

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})
