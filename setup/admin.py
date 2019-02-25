from django.contrib import admin

from .models import Person, Institution


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'identity_num', 'account_number')


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass
