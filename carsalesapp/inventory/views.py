from django.shortcuts import render, redirect
import os, json
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import auth, messages
from . import utils
from .models import VehicleModel
from django.db.models import Q


# Create your views here.
def search(request):

    if request.method == "POST":
        # import pdb; pdb.set_trace()
        searched = request.POST['search-term']
        results = VehicleModel.objects.filter(Q(name__icontains=searched))
        
        if not results:
            messages.error(request, "No results for selected search. Please try again")
            return render(request, 'inventory/search.html', {})
        
        return render(request, 'inventory/search-results.html', {'results': results})
    else:
        return render(request, 'inventory/search.html', {})

#Search results
def results(request):
    return render(request, 'inventory/search-results.html')