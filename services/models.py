from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DateTimeField

# Create your models here.

class Service(models.Model):
    service_date = models.DateTimeField(verbose_name="Date and Time of Service")
    speaker = models.CharField(verbose_name="Speaker", max_length=50)
    topic = models.CharField(verbose_name="Topic", max_length=200)
    coordinator = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.service_date.isoformat()
    
class SegmentType(models.Model):
    name = models.CharField(verbose_name="Name", max_length=50)
    description = models.CharField(verbose_name="Description", max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Segment(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    segment_type = models.ForeignKey(SegmentType, on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Title", max_length=200)
    description = models.CharField(verbose_name="Description", max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title