from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Hymn, Verse

class HymnAdmin(ImportExportModelAdmin):
    pass

class VerseAdmin(ImportExportModelAdmin):
    pass

# Register your models here.
admin.site.register(Hymn, HymnAdmin)
admin.site.register(Verse, VerseAdmin)
