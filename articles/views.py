from django.shortcuts import render
from .models import Post
from django.utils import timezone


def post_list(request):
    posts = Post.objects.filter(
        publish_at__lte=timezone.now()).order_by('publish_at')
    return render(request, 'articles/post_list.html', {'posts': posts})
