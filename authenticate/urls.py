from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView

urlpatterns = [
    # path('', views.login),
    path('signup', views.signup, name='signup'),
    path('', auth_views.LoginView.as_view(template_name='authenticate/login2.html'), name='login2'),
    path('logout', auth_views.LogoutView.as_view(template_name='authenticate/logout.html'), name='logout'),
    path('login', views.login, name='login'),
    path('profile', views.profile, name='profile'),
]
