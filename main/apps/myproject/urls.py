from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('dashboard', views.dashboard),
    path('positions', views.positions),
]