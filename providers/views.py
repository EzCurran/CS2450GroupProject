"""Views"""
from cgi import print_form
import email
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ProviderForm, InsuranceForm, SpecialtyForm, LanguageForm
from .models import Specialty, Language, Insurance, Provider


def home(request):
    """Home page"""    
        # Provider.objects.delete(request.DELETE.get("providerID"))
    
    data = {
        "providers": Provider.objects.all(),
        "insurance": Insurance.objects.all(),
        "languages": Language.objects.all(),
        "specialties": Specialty.objects.all(),
    }
    
    name = request.GET.get('name')
    if name:
        data["providers"]=data["providers"].filter(full_name=name)
    ins = request.GET.get('insurance')
    if ins:
        data["providers"]=data["providers"].filter(insurance__id=ins)
    specialty = request.GET.get('specialty')
    if specialty:
        data["providers"]=data["providers"].filter(specialty__id=specialty)
    language = request.GET.get('language')
    if language:
        data["providers"]=data["providers"].filter(language__id=language)

    print(language)
    
    
    return render(request, "providers/index.html", data)

def delete_provider(request):
    if request.method == "POST":
        form = (request.POST)
        providerId = (form.get("providerID"))

        Provider.objects.filter(id=providerId).delete()

    return redirect("home")

def edit_provider(request):
    """Edit page (same as new page)"""
    if request.method == "POST":
        form = ProviderForm(request.POST)
        if form.is_valid():
            obj = Provider.objects.get(full_name=(request.POST).get("full_name"))
            obj.email = (request.POST).get("email")
            obj.phone = (request.POST).get("phone")
            obj.save()
            obj.insurance.clear()
            obj.specialty.clear()
            obj.language.clear()
            for i in request.POST.get('insurances'):
                obj.insurance.add(i)
            for s in request.POST.get('specialties'):
                obj.specialty.add(s)
            for l in request.POST.get('languages'):
                obj.language.add(l)
            return redirect("home")
    else:
        form = ProviderForm()

    providerId = ((request.POST).get("providerID"))
    obj = Provider.objects.get(id=providerId)

    specialties = Specialty.objects.all()
    language = Language.objects.all()
    insurance = Insurance.objects.all()

    specialtiesSelected = obj.specialty.all()
    languagesSelected = obj.language.all()
    insurancesSelected = obj.insurance.all()

    data = {
        "provider": obj,
        "specialties": specialties,
        "languages": language,
        "insurances": insurance,
        "selectedSpec": specialtiesSelected,
        "selectedLang": languagesSelected,
        "selectedIns": insurancesSelected
    }
    return render(request, "providers/edit-provider.html", data)

def add_provider(request):
    """New page"""
    if request.method == "POST":
        form = ProviderForm(request.POST)

        if form.is_valid():
            new_provider = form.save()
            for i in request.POST.get('insurances'):
                new_provider.insurance.add(i)
            for s in request.POST.get('specialties'):
                new_provider.specialty.add(s)
            for l in request.POST.get('languages'):
                new_provider.language.add(l)
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
