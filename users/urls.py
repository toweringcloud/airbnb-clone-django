from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views


urlpatterns = [
    path("", views.Users.as_view()),
    path("login", views.LogIn.as_view()),
    path("logout", views.LogOut.as_view()),
    path("me", views.Me.as_view()),
    path("password", views.ChangePassword.as_view()),
    path("token-login", obtain_auth_token),
    path("@<str:username>", views.UserDetail.as_view()),
]
