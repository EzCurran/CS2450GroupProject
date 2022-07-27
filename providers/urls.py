"""URLs"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("providers/new/", views.add_provider, name="new_provider"),
    path("providers/delete/", views.delete_provider, name="delete_provider"),
    path("languages/new/", views.add_language, name="new_language"),
    path("specialties/new/", views.add_specialty, name="new_specialty"),
    path("insurance/new/", views.add_insurance, name="new_insurance"),
    path("providers/<int:id>/edit/", views.edit_provider, name="edit_provider"),
    path("providers/export", views.export, name="export"),
]
