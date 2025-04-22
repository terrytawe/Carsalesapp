from . import views
from django.urls import path

urlpatterns = [
    path('', views.search, name="home"),
    path('browse/', views.results, name="results")
] 
