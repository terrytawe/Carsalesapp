import os, json
from . import utils
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import auth, messages
from .models import VehicleModel, Category, Feature, VehicleBrand
from django.db.models import Q


# ────────────────────────────────────────────────────────────────────────────────────────────────
# Create your views here.
# ────────────────────────────────────────────────────────────────────────────────────────────────
def search(request):
    catergories = Category.objects.all()
    vehicle_models = VehicleModel.objects.all()
    context = {
        "categories": catergories,
        'models': vehicle_models

    }

    if request.method == "POST":
        searched = request.POST.get('search-type', '').strip()
        print(searched)
        if not searched:
            return render(request, 'inventory/search.html', context)
        return redirect(f"{reverse('results')}?q={searched}")

    return render(request, 'inventory/search.html', context)

# ────────────────────────────────────────────────────────────────────────────────────────────────
#Search results
# ────────────────────────────────────────────────────────────────────────────────────────────────
def results(request):

    make       = VehicleBrand.objects.all()
    models     = VehicleModel.objects.all()
    categories = Category.objects.all()
    features   = Feature.objects.all()
    query      = Q()

    # import pdb; pdb.set_trace()
    if request.GET.get('search-type'):
        query &= Q(category_id=request.GET.get('search-type'))
    
    if request.GET.get('search-model'):
        query &= Q(name__icontains=request.GET.get('search-model'))
    
    if request.GET.get('search-make'):
        query &= Q(brand_id=request.GET.get('search-make'))

    if request.GET.getlist('features'):
        query &= Q(features__in=request.GET.getlist('features'))


    results = VehicleModel.objects.filter(query) #.select_related('category')

    return render(request, 'inventory/search-results.html', {
        'results'   : results,
        'query'     : query,
        'features'  : features,
        'categories': categories,
        'brands'    : make,
        'models'    : models,
        'search'    : True
    })

# ────────────────────────────────────────────────────────────────────────────────────────────────
#Search results
# ────────────────────────────────────────────────────────────────────────────────────────────────

def ajax_search(request):
    if not request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'error': 'Invalid request'}, status=400)

    query = Q()

    # Dynamic filters from combined forms
    if request.GET.get('search-type'):
        query &= Q(category_id=request.GET.get('search-type'))

    if request.GET.get('search-model'):
        query &= Q(name__icontains=request.GET.get('search-model'))

    if request.GET.get('search-make'):
        query &= Q(brand_id=request.GET.get('search-make'))

    if request.GET.getlist('features'):
        query &= Q(features__in=request.GET.getlist('features'))

    results = VehicleModel.objects.filter(query).distinct()

    html = render_to_string('partials/vehicle-card-list.html', {'results': results})
    return JsonResponse({'html': html})