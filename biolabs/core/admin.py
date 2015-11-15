from django.contrib import admin

from biolabs.core.models import Laboratory


class LaboratoryAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'url', 'adress', 'is_moderated', 'latitude', 'longitude', 'country',
              'created', 'updated')

admin.site.register(Laboratory, LaboratoryAdmin)
