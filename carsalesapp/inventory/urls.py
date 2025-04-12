from . import views
from django.urls import path

urlpatterns = [
    path('', views.search, name="home"),
    path('search-results/', views.results, name="results")
] 
