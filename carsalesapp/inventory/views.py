from django.shortcuts import render, redirect
from django.urls import reverse
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
        searched = request.POST.get('search-term', '').strip()

        import pdb; pdb.set_trace()
        if not searched:
            messages.error(request, "Please enter a search term.")
            return render(request, 'inventory/search.html', {})

        return redirect(f"{reverse('results')}?q={searched}")

    return render(request, 'inventory/search.html')

#Search results
def results(request):
    query = request.GET.get('q', '').strip()

    if query:
        results = VehicleModel.objects.filter(Q(name__icontains=query))

        if not results.exists():
            messages.error(request, f"No results found for '{query}'.")
        
        return render(request, 'inventory/search-results.html', {
            'results': results,
            'query': query,
        })

    messages.error(request, "No search term provided.")
    return render(request, 'inventory/search-results.html', {})  