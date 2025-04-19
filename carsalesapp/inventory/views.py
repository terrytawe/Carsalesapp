from django.shortcuts import render, redirect
from django.urls import reverse
import os, json
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import auth, messages
from . import utils
from .models import VehicleModel, Category, Feature
from django.db.models import Q

# ────────────────────────────────────────────────────────────────────────────────────────────────
# Create your views here.
# ────────────────────────────────────────────────────────────────────────────────────────────────
def search(request):
    catergories = Category.objects.all()
    vehichle_models = VehicleModel.objects.all()
    context = {
        "categories": catergories,
        'models': vehichle_models

    }
    if request.method == "POST":
        searched = request.POST.get('search-type', '').strip()
    # import pdb; pdb.set_trace()
        if not searched:
            # messages.error(request, "Please enter a search term.")
            return render(request, 'inventory/search.html', context)

        return redirect(f"{reverse('results')}?q={searched}")

    return render(request, 'inventory/search.html', context)

# ────────────────────────────────────────────────────────────────────────────────────────────────
#Search results
# ────────────────────────────────────────────────────────────────────────────────────────────────
def results(request):

    features = Feature.objects.all()
    query = ''
    if request.GET.get('search-type'):
        query = Q(category=request.GET.get('search-type'))
    
    if request.GET.get('search-model'):
        query = Q(category=request.GET.get('search-type'))
    
    if request.GET.get('search-price'):
        query = Q(category=request.GET.get('search-type'))

    if query:
        results = VehicleModel.objects.filter(query)
        if not results.exists():
            messages.warning(request, f"No results found for search parameters")
    else:
        results = VehicleModel.objects.all()
        print(results)
        # messages.warning(request, "Please enter a search term.")

    return render(request, 'inventory/search-results.html', {
        'results': results,
        'query': query,
        'features': features
    })