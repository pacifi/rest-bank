from django.contrib import admin

from .models import Person, Institution


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    pass


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass
