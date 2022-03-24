import re
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *

    
def index(request):
    return render(request, "auctions/index.html", {
        "listings": Auction_Listings.objects.all()
    })

def create(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Create_Form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # fetch username in order
            username = None
            if request.user.is_authenticated:
                username = request.user

            # process the data in form.cleaned_data as required
            category_name = form.cleaned_data.get("category")
            listing = Auction_Listings(
                name=form.cleaned_data.get("name"), 
                selling_price=form.cleaned_data.get("selling_price"), 
                image=form.cleaned_data.get("image"), 
                creator=username,
                category=Category.objects.get(name=category_name))
            listing.save()

            # redirect to a new URL:
            return render(request, 'auctions/index.html', {
                "message": "Active Listings",
                "listings": Auction_Listings.objects.all()
            })
    # if a GET (or any other method) we'll create a blank form
    else:
        form = Create_Form()

    return render(request, 'auctions/create.html', {'form': form})

@login_required
def listing(request, listing_id):

    ## Handle form input via POST
    listing = Auction_Listings.objects.get(id=listing_id)
    if request.method == "POST":
        # Bid Form
        bid_form = Bid_Form(request.POST)
        if bid_form.is_valid():
            bid = bid_form.cleaned_data.get("bid")
            if bid > listing.selling_price:
                listing.selling_price = bid
            
        # Edit Form
        edit_form = Edit_Form(request.POST)
        if edit_form.is_valid():
            closed = edit_form.cleaned_data.get("closed")
            listing.closed = closed

        listing.save()
        return render(request, 'auctions/index.html', {
                "listings": Auction_Listings.objects.all()
            })


    else:
        try:
            listing = Auction_Listings.objects.get(id=listing_id)
        except Auction_Listings.DoesNotExist:
            raise Http404("Flight not found.")

        ## Generate correct form based on user's logged in status
        edit_form = "Must be owner to edit."
        bid_form = Bid_Form()
        if request.user == listing.creator:
            edit_form = Edit_Form()

        return render(request, 'auctions/listing.html', {
            "listing": listing,
            "edit_form": edit_form,
            "bid_form": bid_form
        })

@login_required
def category(request):
    if request.method == "POST":
        form = Category_Form(request.POST)
        if form.is_valid():
            requested_category = form.cleaned_data["category"]
            listings = []

            for listing in Auction_Listings.objects.all():
                if listing.category == requested_category:
                    listings.append(listing)

            return render(request, 'auctions/index.html', {
                "listings": listings,
                "message": f"Results for {requested_category}"

            })
    else:
        form = Category_Form()
    
    return render(request, 'auctions/category.html', { "category_form": form })

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
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


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
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def watchlist(request):
    return render(request, "auctions/watchlist.html")
