from django.urls import path
from .views import signup
from .views import user
from .views import all_users

urlpatterns = [
    path("signup/", signup, name='signup'),
    path("user/<int:pk>/", user, name='user'),
    path("all-users/", all_users, name='all-users'),
]