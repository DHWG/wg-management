from django.contrib import admin
from .models import Inhabitant, Expense

@admin.register(Inhabitant)
class InhabitantAdmin(admin.ModelAdmin):
    exclude = ('password',)

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    pass