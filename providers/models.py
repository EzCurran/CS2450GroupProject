from django.db import models

# Create your models here.

class Provider(models.Model):
    full_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    email = models.CharField(max_length=250)

    def __str__(self):
        return self.full_name

class Insurance(models.Model):
    provider = models.ManyToManyField(Provider, related_name="insurance")
    name = models.CharField(max_length=250)
    details = models.TextField()

    def __str__(self):
        return self.name

class Specialty(models.Model):
    provider = models.ManyToManyField(Provider, related_name="specialty")
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Language(models.Model):
    provider = models.ManyToManyField(Provider, related_name="language")
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name