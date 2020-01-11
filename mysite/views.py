from django.shortcuts import render
from articles.models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', context={'posts': posts})
