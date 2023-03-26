from django.contrib import admin

from apps.organization.models import Entrant


@admin.register(Entrant)
class EntrantAdmin(admin.ModelAdmin):
    pass
