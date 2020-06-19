from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone


def post_list(request):
    posts = Post.objects.filter(
        publish_at__lte=timezone.now()).order_by('publish_at')
    return render(request, 'articles/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'articles/post_detail.html', {'post': post})
