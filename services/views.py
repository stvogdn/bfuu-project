
# Create your views here.
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Service, SegmentType, Segment, ScriptElements
from .forms import SegmentTypeForm, ServiceForm, SegmentForm, ScriptElementsForm

def next_four_services(request):
    now = timezone.now()
    upcoming_services = Service.objects.filter(service_date__gte=now).order_by('service_date')[:4]
    return render(request, 'next_four_services.html', {'upcoming_services': upcoming_services})


def create_segment_type(request):
    if request.method == 'POST':
        form = SegmentTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('segmenttype_list')
    else:
        form = SegmentTypeForm()
    return render(request, 'services/segmenttype_form.html', {'form': form})

def create_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.coordinator = request.user
            service.save()
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request, 'services/service_form.html', {'form': form})

def service_list(request):
    services = Service.objects.all().order_by('-service_date')
    return render(request, 'services/service_list.html', {'services': services})

def segmenttype_list(request):
    services = SegmentType.objects.all().order_by('name')
    return render(request, 'services/segmenttype__list.html', {'services': services})

def add_script_elements(request):
    if request.method == 'POST':
        form = ScriptElementsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('records_list')
    else:
        form = ScriptElementsForm()
    return render(request, 'services/scriptelements_form.html', {'form': form})
