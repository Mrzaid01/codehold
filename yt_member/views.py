from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserAccount

def index(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        if password == password2:
            if UserAccount.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
            elif UserAccount.objects.filter(email=email).exists():
                messages.error(request, "Email already exists")
            else:
                user = UserAccount.objects.create(username=username, email=email, password=password)
                user.save()
                messages.success(request, "Account created successfully")
                return redirect("user") 
        else:
            messages.error(request, "Passwords do not match")
    
    return render(request, "index.html")

def user(request):
    return render(request, "user.html")

def test(request):
    return render(request, "test.html")