## img links for testing purposes

# https://drive.google.com/uc?export=view&id=1na64Wmn8-Op3T2oEThpXK-Bel-Sg10za (bell)
# https://drive.google.com/uc?export=view&id1ATJQq3-QNp0l8NynOsYADY-2QmRgeStj (toaster)

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create/", views.create, name="create"),
    path("<int:listing_id>", views.listing, name="listing"),
    path("watchlist", views.watchlist, name="watchlist")
]
