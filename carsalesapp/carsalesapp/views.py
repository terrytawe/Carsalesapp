from django.shortcuts import render, redirect
import os, json
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import auth

def index(request):
    data_years = []
    data_price = []
    fp_years = os.path.join(settings.BASE_DIR, "data-files/years.json")
    fp_price = os.path.join(settings.BASE_DIR, "data-files/prices.json")

    with open(fp_years) as year_file:
        data = json.load(year_file)

        for k,v in data.items():
            data_years.append({"key": k, "value": v})
    
    with open(fp_price) as price_file:
        data = json.load(price_file)

        for k,v in data.items():
            data_price.append({"key": k, "value": v})
    
    context = {
        'years'  : data_years,
        'prices' : data_price, 
    }
    
    return render(request, 'index.html', context)