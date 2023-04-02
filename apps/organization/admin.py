from django.contrib import admin
from apps.organization.models import Entrant, Specialty


@admin.register(Entrant)
class EntrantAdmin(admin.ModelAdmin):
    pass


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    pass
