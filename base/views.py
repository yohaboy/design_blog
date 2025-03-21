from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import User
from .models import Post
from django.views.generic import ListView
from django.db.models import Q

def home(request):

    results = []
    posts = Post.objects.all()
    user_exists = User.objects.filter(username=request.user.username)

    filter_value = request.GET.get('filter')

    if filter_value:
        posts = posts.filter(category__icontains=filter_value)
    
    if 'search' in request.GET:
        query = request.GET['search']
        results = Post.objects.filter(Q(user__username__icontains=query)| Q(category__icontains=query))
        if not results :
            posts = []
        posts = results

    context = {
        'user_exists':user_exists,
        'posts':posts
    }
    return render(request,'base/index.html', context=context)

