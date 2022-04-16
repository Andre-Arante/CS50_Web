import re
import time
import datetime

from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.core.paginator import Paginator

from .models import *
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
    return render(request, "network/profile.html")

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
