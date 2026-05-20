from django.shortcuts import render, get_object_or_400
from django.contrib.auth.models import User
from .models import Post

def index(request):
    posts = Post.objects.all().order_by('-criado_em')
    return render(request, 'index.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_400(Post, id=post_id)
    return render(request, 'post_detail.html', {'post': post})

def user_profile(request, username):
    user = get_object_or_400(User, username=username)
    posts = user.posts.all().order_by('-criado_em')
    return render(request, 'profile.html', {'profile_user': user, 'posts': posts})