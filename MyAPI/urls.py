from django.urls import path, include
from . import views
from rest_framework import routers


urlpatterns = [
    path('', views.translated, name='home'),
    path('about/', views.about, name='about'),
]