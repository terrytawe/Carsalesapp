from . import views
from django.urls import path

urlpatterns = [
    path('', views.search, name="home"),
    path('browse/', views.results, name="results"),
    path('search-results/', views.ajax_search, name='ajax-search'),
] 
