
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile/<user>", views.profile, name="profile"),
    path("edit/<user>", views.edit, name="edit"),
    path("like/<int:id>", views.like, name="like"),
]
