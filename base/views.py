from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import User
from .models import Post
from django.views.generic import ListView

def home(request):

    posts = Post.objects.all()
    user_exists = User.objects.filter(username=request.user.username)

    context = {
        'user_exists':user_exists,
        'posts':posts
    }
    return render(request,'base/index.html', context=context)
