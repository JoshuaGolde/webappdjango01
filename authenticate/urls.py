from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView

urlpatterns = [
    # path('', views.login),
    path('signup', views.signup, name='signup'),
    path('login', auth_views.LoginView.as_view(template_name='authenticate/login2.html'), name='login2'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.login, name='login'),
]
