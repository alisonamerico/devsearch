from django.urls import path
from users.views import login_user, profiles, user_profile, logout_user

urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('', profiles, name='profiles'),
    path('profile/<str:pk>/', user_profile, name='user-profile'),
]
