from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserSignupForm
from django.contrib.auth.decorators import login_required


# Create your views here.


def welcome(request):
    return render(request, 'authenticate/welcome.html')


def login(request):
    return render(request, 'authenticate/login.html')


def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username} now you can login')
            return redirect('login')

    else:
        form = UserSignupForm()
    return render(request, 'authenticate/signup.html', {'form': form})



@login_required
def profile(request):
    return render(request, 'authenticate/profile.html')



