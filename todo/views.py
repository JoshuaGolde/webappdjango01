from django.shortcuts import render

def todoView(request):
    return render(request, 'todo.html')
# Create your views here.
