from django.contrib import admin
from .models import ShiftPeriod, Roster

@admin.register(ShiftPeriod)
class ShiftPeriodAdmin(admin.ModelAdmin):
	pass

@admin.register(Roster)
class RosterAdmin(admin.ModelAdmin):
	pass
