from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView

urlpatterns = [
    # path('', views.login),
    path('signup', views.signup, name='signup'),
    path('', views.login, name='login'),
]
