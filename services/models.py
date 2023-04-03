from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DateTimeField

# Create your models here.


class Speaker(models.Model):
    name = models.CharField(verbose_name="Name", max_length=50)
    biography = models.TextField(verbose_name="Biography")
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Service(models.Model):
    service_date = models.DateTimeField(verbose_name="Date and Time of Service")
    speaker = models.CharField(verbose_name="Speaker", max_length=50)
    topic = models.CharField(verbose_name="Title", max_length=200)
    description = models.TextField(verbose_name="Description", default="")
    coordinator = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.service_date.isoformat()

class SegmentType(models.Model):
    name = models.CharField(verbose_name="Name", max_length=50)
    description = models.CharField(verbose_name="Description", max_length=200)
    template = models.TextField("Template", default="")
    variables = models.TextField("Variables", default="{}")
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Segment(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    segment_type = models.ForeignKey(SegmentType, on_delete=models.CASCADE)
    sequence = models.IntegerField(verbose_name="Sequence", default=0)
    variables = models.TextField("Variables", default="{}")
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '{self.service.service_date.isoformat()} {self.sequence} {self.segment_type.name}'
    
class ScriptElements(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    liturgist_name = models.CharField(max_length=100)
    prelude_hymn_number = models.IntegerField()
    prelude_hymn_name = models.CharField(max_length=100)
    opening_words = models.TextField()
    principle_or_source_number = models.IntegerField()
    principle_or_source = models.CharField(max_length=100)
    principle_or_source_text = models.TextField()
    first_hymn_number = models.IntegerField()
    first_hymn_name = models.CharField(max_length=100)
    meditation_reading = models.TextField()
    metta_singer = models.CharField(max_length=100)
    second_hymn_number = models.IntegerField()
    second_hymn_name = models.CharField(max_length=100)
    readers_names = models.CharField(max_length=100)
    singers_names = models.CharField(max_length=100)
    zoom_host_name = models.CharField(max_length=100)
    slide_manager_name = models.CharField(max_length=100)
    shared_plate_partner = models.CharField(max_length=100)
    final_hymn_number = models.IntegerField()
    final_hymn_name = models.CharField(max_length=100)
    circle_round_singer = models.CharField(max_length=100)

    def __str__(self):
        return f'{{self.service.dervice_date}} {{self.liturgist_name}}'
