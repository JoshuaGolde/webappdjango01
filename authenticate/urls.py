from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('signup', views.signup, name='signup'),
    path('login', auth_views.LoginView.as_view(template_name='authenticate/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='authenticate/logout.html'), name='logout'),
    path('profile', views.profile, name='profile'),
]
