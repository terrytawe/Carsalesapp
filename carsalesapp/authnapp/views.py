from django.shortcuts import render
from django.views import View

# Create your views here.
#--------------------------------------------------------------------------------------------------    
#View to render new password page
#--------------------------------------------------------------------------------------------------    
class PasswordNewView(View):
    def get(self, request):
        return render(request, 'authnapp/password-new.html')