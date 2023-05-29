from django.contrib import admin
from core import models

# Register your models here.
@admin.register(models.Group)
class Group(admin.ModelAdmin):
    list_display = ('name',)
