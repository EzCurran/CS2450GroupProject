"""Views"""
from cgi import print_form
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ProviderForm, InsuranceForm, SpecialtyForm, LanguageForm
from .models import Specialty, Language, Insurance, Provider


def home(request):
    """Home page"""
    data = {
        "providers": Provider.objects.all(),
        "insurance": Insurance.objects.all(),
        "languages": Language.objects.all(),
        "specialties": Specialty.objects.all(),
    }

    return render(request, "providers/index.html", data)


def add_provider(request):
    """New page"""
    if request.method == "POST":
        form = ProviderForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = ProviderForm()

    specialties = Specialty.objects.all()
    language = Language.objects.all()
    insurance = Insurance.objects.all()

    data = {
        "specialties": specialties,
        "languages": language,
        "insurances": insurance
    }

    return render(request, "providers/add-provider.html", data)


def add_language(request):
    "Add language page"
    if request.method == "POST":
        form = LanguageForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = LanguageForm()
    return render(request, "providers/add-language.html")


def add_specialty(request):
    """Add specialty page"""
    if request.method == "POST":
        form = SpecialtyForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = SpecialtyForm()
    return render(request, "providers/add-specialty.html")


def add_insurance(request):
    """Add insurance page"""
    if request.method == "POST":
        form = InsuranceForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = InsuranceForm()
    return render(request, "providers/add-insurance.html")
