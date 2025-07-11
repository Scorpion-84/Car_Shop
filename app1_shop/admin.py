from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.CarChoice)
class CarChoiceAdmin(admin.ModelAdmin):
    pass
