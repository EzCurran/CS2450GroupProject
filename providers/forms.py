from dataclasses import fields
from django import forms
from .models import Insurance, Language, Provider, Specialty


class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = ["full_name", "phone", "email"]


class InsuranceForm(forms.ModelForm):
    class Meta:
        model = Insurance
        fields = ["name", "details"]


class SpecialtyForm(forms.ModelForm):
    class Meta:
        model = Specialty
        fields = ["name"]


class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ["name"]
