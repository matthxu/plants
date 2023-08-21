from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Plant

# Create your views here.

def home (request):
    return render(request, 'home.html')

def about (request):
    return render(request, 'about.html')

class PlantList (ListView):
    model = Plant

class PlantCreate (CreateView):
    model = Plant
    # age is not included because it can be calculated using date-planted instead
    fields = ['name', 'date', 'description']