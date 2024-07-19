from django.shortcuts import render
from django.http import HttpResponse
from .models import Obituary
def home(request):
    return render(request, 'frontend/home.html')
def display_obituary(request):
    obituary = Obituary.objects.all()
    return render(request, 'frontend/home.html', {'obituary': obituary})
