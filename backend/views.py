from django.shortcuts import render
from django.http import HttpResponse

def user(request):
    return HttpResponse('User page')
# Create your views here.
