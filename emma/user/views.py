from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def register_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password  = form.cleaned_data.get('password1')
            messages.success(request, 'Account was created for ' + username)
            
            return redirect('login')
        
        context = {"form":form}
        return render(request, 'user/register.html', context)

def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')
                return render(request, 'user/login.html')
 
        return render(request, 'user/login.html')

def logout_page(request):
    logout(request)
    return redirect('login')