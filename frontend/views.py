from django.shortcuts import render
from backend.models import Obituary
obituaries = Obituary.objects.all()


def home(request):
      return render(request, 'frontend/home.html', {'obituaries': obituaries})
