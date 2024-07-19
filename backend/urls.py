from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('display_user/', views.display_obituary),
]