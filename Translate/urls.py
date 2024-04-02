# Translation/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Translate/templates/index'),
    path('navigate/', views.navigate, name='navigate'),
    path('translate/', views.translate, name='translate'),
]

