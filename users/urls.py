from django.urls import path
from users.views import (
    login_user,
    profiles,
    register_user,
    user_profile,
    logout_user,
)

urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
    path('', profiles, name='profiles'),
    path('profile/<str:pk>/', user_profile, name='user-profile'),
]
