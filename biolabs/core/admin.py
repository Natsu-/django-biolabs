from django.contrib import admin

from biolabs.core.models import Laboratory


class LaboratoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Laboratory, LaboratoryAdmin)
