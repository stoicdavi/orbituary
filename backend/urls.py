from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('display_user/', views.display_obituary),
    path('add_obituary/', views.add_obituary, name='add_obituary'),
]