from django.db import models


class Provider(models.Model):
    full_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    email = models.CharField(max_length=250)

    def __str__(self):
        return self.full_name

    def insurance_list(self):
        return [i.name for i in self.insurance.all()]

    def specialty_list(self):
        return [s.name for s in self.specialty.all()]

    def language_list(self):
        return [i.name for i in self.language.all()]


class Insurance(models.Model):
    provider = models.ManyToManyField(Provider, related_name="insurance", blank=True)
    name = models.CharField(max_length=250)
    details = models.TextField()

    def __str__(self):
        return self.name


class Specialty(models.Model):
    provider = models.ManyToManyField(Provider, related_name="specialty", blank=True)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Language(models.Model):
    provider = models.ManyToManyField(Provider, related_name="language", blank=True)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
