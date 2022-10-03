from . import views

from django.urls import path

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("profile/<int:pk>", views.UserDetailView.as_view(), name='profile.view'),
    path("profile/<int:pk>/edit", views.UserUpdateView.as_view(), name='profile.edit'),
    path("all-profiles", views.ProfileListView.as_view(), name='profile.list'),
]