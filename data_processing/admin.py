from django.contrib import admin

from data_processing.models import WOTalon


class DataProcessingAdmin(admin.ModelAdmin):
    list_display = ('talon_id', 'last_updated')


admin.site.register(WOTalon, DataProcessingAdmin)
