from django.contrib import admin
from .models import Inhabitant

@admin.register(Inhabitant)
class InhabitantAdmin(admin.ModelAdmin):
    pass