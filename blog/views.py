from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView

from .models import Post


def posts_list(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, "posts_list.html", context)


def post_detail(request, id):
    # post = Post.objects.get(id=id)
    post = get_object_or_404(Post, pk=id)
    context = {
        "post": post
    }
    return render(request, "posts_detail.html", context)


class PostsListView(ListView):
    model = Post
    paginate_by = 2
    # template_name = "posts_list.html"
    # context_object_name = "posts"
