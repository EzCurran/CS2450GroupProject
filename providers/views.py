"""Views"""
from cgi import print_form
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ProviderForm, InsuranceForm, SpecialtyForm, LanguageForm
from .models import Specialty


def home(request):
    """Home page"""
    providers = [
        {
            "id": 1,
            "comments": "Comments here.",
            "insurance": ["insurance a", "insurance b", "insurance c"],
            "name": "Provider 1",
            "phone": "801-123-4567",
            "email": "provider@mail.com",
            "licenses": ["license a", "license b", "license c"],
            "specialties": ["specialty a", "specialty b", "specialty c"],
            "languages": ["English", "Spanish", "French"],
        },
        {
            "id": 3,
            "comments": "Comments here.",
            "insurance": ["insurance a", "insurance b", "insurance c"],
            "name": "Provider 2",
            "phone": "801-123-4567",
            "email": "provider2@mail.com",
            "licenses": ["license a", "license b", "license c"],
            "specialties": ["specialty a", "specialty b", "specialty c"],
            "languages": ["English", "Spanish", "French", "German"],
        },
        {
            "id": 3,
            "comments": "Comments here.",
            "insurance": ["insurance a", "insurance b", "insurance c"],
            "name": "Provider 3",
            "phone": "801-123-4567",
            "email": "provider3@mail.com",
            "licenses": ["license a", "license b", "license c"],
            "specialties": ["specialty a", "specialty b", "specialty c"],
            "languages": ["Italian", "Portuguese"],
        },
    ]

    insurance = [
        {"id": 1, "name": "insurance A"},
        {"id": 2, "name": "insurance B"},
        {"id": 3, "name": "insurance C"},
    ]

    languages = [
        {"id": 1, "name": "language A"},
        {"id": 2, "name": "language B"},
        {"id": 3, "name": "language C"},
    ]

    specialties = [
        {"id": 1, "name": "specialty A"},
        {"id": 2, "name": "specialty B"},
        {"id": 3, "name": "specialty C"},
    ]

    licenses = [
        {"id": 1, "name": "license A"},
        {"id": 2, "name": "license B"},
        {"id": 3, "name": "license C"},
    ]

    data = {
        "providers": providers,
        "insurance": insurance,
        "languages": languages,
        "specialties": specialties,
        "licenses": licenses,
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

    data = {
        "specialties": specialties,
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
