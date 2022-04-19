import re
import time
import datetime

from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator

from .models import Post, User, UserProfile, Friendship
from .forms import CreatePost


def index(request):

    users = User.objects.all()

    ## Fetch all posts and display using Paginator
    objects = Post.objects.all().order_by('-timestamp')
    num_items = 10

    p = Paginator(objects, num_items)

    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)

    ## Handles New Post Submission
    if request.method == "POST":
        form = CreatePost(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = CreatePost(user=request.user)

    return render(request, "network/index.html", {
        'all_users': users,
        'page_obj': page_obj,
        'form': form
    })

def profile(request, user):
    # Generates correct user profile
    user = User.objects.get(username=user)
    user_profile = UserProfile.objects.get(user=user)

    # Fetches friend list
    friends = user_profile.get_following()
    friend_list = []

    for friend in friends:
        name = User.objects.get(username=friend.following)
        friend_list.append(name)

    # Creates a friendship between two users if user pressed "follow"
    if request.method == "POST":

        profile = UserProfile.objects.get(user=user)

        if Friendship.objects.filter(root=request.user, following=user).exists():
            Friendship.objects.filter(root=request.user, following=user).delete()
            profile.followers += 1
            profile.save()
        else:
            new_friendship = Friendship(root=request.user, following=user)
            new_friendship.save()
            profile.followers -= 1

        profile.save()
        

    # Displays correct button
    if request.user == user:
        button = 'edit'
    elif Friendship.objects.filter(root=request.user, following=user).exists():
        button = 'unfollow'
    else:
        button = 'follow'


    return render(request, "network/profile.html", {
        'user': user,
        'button': button,  
        'profile': user_profile,
        'friends': friend_list
    })

def edit(request, user):
    return render(request, "network/edit.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            user_profile = UserProfile(user=user)
            user_profile.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
