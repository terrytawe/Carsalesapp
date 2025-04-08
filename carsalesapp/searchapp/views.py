from django.shortcuts import render
from django.views import View

# Create your views here.
#--------------------------------------------------------------------------------------------------    
#View to render new password page
#--------------------------------------------------------------------------------------------------    
class HomeView(View):
    def get(self, request):
        return render(request, 'searchapp/index.html', {})
# Create your views here.
