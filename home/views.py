from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def login(request):
    return render(request, 'home/login.html')

#create logout and signup functions here

def logout(request):
    return render(request, 'home/logout.html')

def signup(request):
    return render(request, 'home/signup.html')