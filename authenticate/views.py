from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


def login(request):
    return render(request, 'authenticate/login.html')


def signup(request):
    form = UserCreationForm()
    return render(request, 'authenticate/signup.html', {'form': form})

# def signup(request):
#  return render(request, 'authenticate/signup.html')
