from . import views

from django.urls import path

urlpatterns = [
    path("register", views.SignupView.as_view(), name="register"),
    path("logout", views.LogoutInterfaceView.as_view(), name="logout"),
    path("login", views.LoginInterfaceView.as_view(), name="login"),
]