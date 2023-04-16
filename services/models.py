from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DateTimeField
from django.urls import reverse
from phone_field import PhoneField


# Create your models here.

class Speaker(models.Model):
    name = models.CharField(verbose_name="Name", max_length=50)
    email = models.EmailField(verbose_name="Email", max_length=254, blank=True, null=True)
    phone = PhoneField(verbose_name="Phone", blank=True, null=True)
    biography = models.TextField(verbose_name="Biography", default="")
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('services-speaker_detail', kwargs={'pk': self.pk})


class Service(models.Model):
    service_date = models.DateTimeField(verbose_name="Date and Time of Service")
    speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE)
    topic = models.CharField(verbose_name="Title", max_length=200)
    description = models.TextField(verbose_name="Description", default="")
    coordinator = models.ForeignKey(User, on_delete=models.CASCADE)
    in_person_attendance = models.IntegerField(verbose_name="In Person Attendance", default=0)
    zoom_attendance = models.IntegerField(verbose_name="Zoom Attendance", default=0)
    offering = models.DecimalField(verbose_name="Offering", max_digits=10, decimal_places=2, default=0.00)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-service_date']
    
    def __str__(self):
        return self.service_date.isoformat()
    
    def get_absolute_url(self):
        return reverse('services-service_detail', kwargs={'pk': self.pk})


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
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{{self.service.dervice_date}} {{self.liturgist_name}}'
