from django.contrib import admin
from . import models


@admin.register(models.Cafe)
class CafeAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "name",
    )
