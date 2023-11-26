from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('user/<str:username>/', views.get_user, name='user-profile'),
    path('user/<str:username>/edit/', views.edit_profile, name='edit_profile'),
]