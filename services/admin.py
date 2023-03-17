from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Service, SegmentType, Segment

class ServiceAdmin(ImportExportModelAdmin):
    pass

class SegmentTypeAdmin(ImportExportModelAdmin):
    pass

class SegmentAdmin(ImportExportModelAdmin):
    pass

# Register your models here.
admin.site.register(Service, ServiceAdmin)
admin.site.register(SegmentType, SegmentTypeAdmin)
admin.site.register(Segment, SegmentAdmin)

