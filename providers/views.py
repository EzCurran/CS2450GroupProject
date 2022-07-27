"""Views"""
import csv
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .forms import ProviderForm, InsuranceForm, SpecialtyForm, LanguageForm
from .models import Specialty, Language, Insurance, Provider


def export(request):
    selected = request.POST.getlist("selected")

    if len(selected) == 0:
        # No providers selected, return to home page.
        return redirect("home")

    # Build HTTP response to return a csv.
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="providers.csv"'

    # Create a csv writer writing to the response object and write the headers.
    writer = csv.writer(response, quoting=csv.QUOTE_ALL)
    writer.writerow(["Name", "Phone", "Email", "Insurance", "Specialties", "Languages"])

    # Build the CSV file with the selected providers.
    providers = Provider.objects.filter(id__in=selected).all()
    for provider in providers:
        writer.writerow(
            [
                provider.full_name,
                provider.phone,
                provider.email,
                ", ".join(provider.insurance_list()),
                ", ".join(provider.specialty_list()),
                ", ".join(provider.language_list()),
            ]
        )

    return response


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
        data["providers"] = data["providers"].filter(full_name__icontains=name)
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


def delete_provider(request, id):
    provider = get_object_or_404(Provider, id=id)
    provider.delete()

    return redirect("home")


def edit_provider(request, id):
    print(id)
    """Edit page (same as new page)"""
    if request.method == "POST":
        form = ProviderForm(request.POST)
        if form.is_valid():
            obj = Provider.objects.get(id=id)
            obj.email = request.POST.get("email")
            obj.phone = request.POST.get("phone")
            obj.save()

            # Clear the old many to many fields
            obj.insurance.clear()
            obj.specialty.clear()
            obj.language.clear()

            # Add the many to many fields to the object
            insurances = request.POST.getlist("insurances")
            if insurances:
                obj.insurance.add(*insurances)
            languages = request.POST.getlist("languages")
            if languages:
                obj.language.add(*languages)
            specialties = request.POST.getlist("specialties")
            if specialties:
                obj.specialty.add(*specialties)

            return redirect("home")
    else:
        form = ProviderForm()

    obj = Provider.objects.get(id=id)

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
        "selectedIns": insurancesSelected,
    }

    return render(request, "providers/edit-provider.html", data)


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
