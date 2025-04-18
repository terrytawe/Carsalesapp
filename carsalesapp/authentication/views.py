from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm

# ────────────────────────────────────────────────────────────────────────────────────────────────
# Login View
# ────────────────────────────────────────────────────────────────────────────────────────────────
def login_user(request):

    if request.method == 'GET':
        return render(request, 'authentication/login.html')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if username and password:
            user = auth.authenticate(username=username, password=password)

            if user.is_authenticated:
               login(request, user)

               if user.is_staff:
                return redirect('dashboard-employee')
               else:
                return redirect('home')
            return render(request, 'authentication/login.html')
        return render(request, 'authentication/login.html')

# ────────────────────────────────────────────────────────────────────────────────────────────────
# Logout View
# ────────────────────────────────────────────────────────────────────────────────────────────────
def logout_user(request):
    # Clear any existing messages
    storage = messages.get_messages(request)
    list(storage)  # This consumes the generator and clears it

    auth.logout(request)

    messages.success(request, 'You have been logged out')
    return redirect('home')

# ────────────────────────────────────────────────────────────────────────────────────────────────
# Logout View
# ────────────────────────────────────────────────────────────────────────────────────────────────
def register_user(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid:
            try:
                form.save()
            except:
                return render(request, 'authentication/register.html', {'form': form})
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = auth.authenticate(username=username, password=password)
            login(request, user)

            if user:
                messages.success(request, 'Account registered successfully')
                return redirect('home')
            else:
                messages.error(request, 'There was a problem registering, please try again')
                return render(request, 'authentication/register.html')
        else:
            messages.error(request, 'There was a problem registering, please try again')
            return render(request, 'authentication/register.html')
    else:
        return render(request, 'authentication/register.html', {'form': form})
   