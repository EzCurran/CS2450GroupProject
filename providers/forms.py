from django import forms

class ProviderForm(forms.Form):
    full_name = forms.CharField(max_length=250, label="Full Name")
    phone = forms.CharField(max_length=250, label="Phone")
    email = forms.CharField(max_length=250, label="Email")

class InsuranceForm(forms.Form):
    name = forms.CharField(max_length=250, label="Name")
    details = forms.CharField(max_length=250, label="Details")

class SpecialtyForm(forms.Form):
    name = forms.CharField(max_length=250, label="Name")

class LanguageForm(forms.Form):
    name = forms.CharField(max_length=250, label="Name")