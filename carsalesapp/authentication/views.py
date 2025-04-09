from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages, auth

#--------------------------------------------------------------------------------------------------
# Login View
#--------------------------------------------------------------------------------------------------
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
               return redirect('home')
            return render(request, 'authentication/login.html')
        return render(request, 'authentication/login.html')

#--------------------------------------------------------------------------------------------------
# Logout View
#--------------------------------------------------------------------------------------------------
def logout_user(request):
    # Clear any existing messages
    storage = messages.get_messages(request)
    list(storage)  # This consumes the generator and clears it

    auth.logout(request)

    messages.success(request, 'You have been logged out')
    return redirect('home')
   