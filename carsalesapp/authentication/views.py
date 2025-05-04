from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm
from django.contrib.auth.views import PasswordChangeView
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse_lazy

# ────────────────────────────────────────────────────────────────────────────────────────────────
# Login View
# ────────────────────────────────────────────────────────────────────────────────────────────────
#
def login_user(request):

    if request.method == 'GET':
        return render(request, 'authentication/login.html')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # import pdb; pdb.set_trace()

        if username and password:
            user = auth.authenticate(username=username, password=password)

            if user.is_authenticated:
               login(request, user)

               if user.is_staff:
                return redirect('dashboard')
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


# ────────────────────────────────────────────────────────────────────────────────────────────────
# Password change
# ────────────────────────────────────────────────────────────────────────────────────────────────
#
class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'authentication/password-change.html'  
    success_url = reverse_lazy('change_password_done')    

    def form_valid(self, form):
        # Save the new password
        response = super().form_valid(form)

        # Keep the user logged in
        update_session_auth_hash(self.request, form.user)

        # Send email confirmation
        send_mail(
            subject='Your Password Was Changed',
            message=(
                f"Hello {form.user.username},\n\n"
                f"This is a confirmation that your password was changed successfully."
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[form.user.email],
            fail_silently=False,
        )

        # Add Django message framework feedback
        messages.success(self.request, 'Password changed successfully. A confirmation email has been sent.')
        return response