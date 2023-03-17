from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Profile

class ProfileAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)

