"""URLs"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("providers/new/", views.add_provider, name="new_provider"),
    path("languages/new/", views.add_language, name="new_language"),
]
