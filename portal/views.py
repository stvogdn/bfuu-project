from django.utils import timezone
from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from services.models import Service

def home(request):
    now = timezone.now()
    upcoming_services = Service.objects.filter(service_date__gte=now).order_by('service_date')[:4]
    return render(request, 'portal/home.html', {'upcoming_services': upcoming_services})


def about(request):
    return render(request, 'portal/about.html', {'title': 'About'})

