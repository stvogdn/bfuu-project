
# Create your views here.
from django.shortcuts import render
from django.utils import timezone
from .models import Service

def next_four_services(request):
    now = timezone.now()
    upcoming_services = Service.objects.filter(service_date__gte=now).order_by('service_date')[:4]
    return render(request, 'next_four_services.html', {'upcoming_services': upcoming_services})
