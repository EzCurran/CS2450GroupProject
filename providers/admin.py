from django.contrib import admin
from . import models

admin.site.register(models.Provider)
admin.site.register(models.Insurance)
admin.site.register(models.Specialty)
admin.site.register(models.Language)
