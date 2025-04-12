from django.shortcuts import render, redirect
import os, json
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import auth
from . import utils


# Create your views here.
def search(request):

    file_data = utils.fileData()

    if request.method == "POST":
        pass
    else:
        return render(request, 'inventory/search.html', file_data)

#Search results
def results(request):
    return render(request, 'inventory/search-results.html')