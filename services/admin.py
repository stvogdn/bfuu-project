from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Service, Speaker, ScriptElements

class ServiceAdmin(ImportExportModelAdmin):
    pass

class SpeakerAdmin(ImportExportModelAdmin):
    pass

class ScriptElementsAdmin(ImportExportModelAdmin):
    pass

# Register your models here.
admin.site.register(Service, ServiceAdmin)
admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(ScriptElements, ScriptElementsAdmin)

