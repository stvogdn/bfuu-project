from django.contrib import admin
from .models import Service, SegmentType, Segment

# Register your models here.
admin.site.register(Service)
admin.site.register(SegmentType)
admin.site.register(Segment)
