from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(request):
    return HttpResponse('login-page')

def signup(request):
    return HttpResponse('signup-page')