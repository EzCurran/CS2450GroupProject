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

    name = request.GET.get("name")
    if name:
        data["providers"] = data["providers"].filter(full_name=name)
    ins = request.GET.get("insurance")
    if ins:
        data["providers"] = data["providers"].filter(insurance__id=ins)
    specialty = request.GET.get("specialty")
    if specialty:
        data["providers"] = data["providers"].filter(specialty__id=specialty)
    language = request.GET.get("language")
    if language:
        data["providers"] = data["providers"].filter(language__id=language)

    return render(request, "providers/index.html", data)


def delete_provider(request):
    if request.method == "POST":
        providerId = request.POST.get("providerID")
        Provider.objects.filter(id=providerId).delete()

    return redirect("home")


def add_provider(request):
    """New page"""
    if request.method == "POST":
        form = ProviderForm(request.POST)
        if form.is_valid():
            new_provider = form.save()

            # Add many to many fields to the newly created provider.
            insurances = request.POST.getlist("insurances")
            if insurances:
                new_provider.insurance.add(*insurances)

            languages = request.POST.getlist("languages")
            if languages:
                new_provider.language.add(*languages)

            specialties = request.POST.getlist("specialties")
            if specialties:
                new_provider.specialty.add(*specialties)

            return redirect("home")
    else:
        form = ProviderForm()

    data = {
        "specialties": Specialty.objects.all(),
        "languages": Language.objects.all(),
        "insurances": Insurance.objects.all(),
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
