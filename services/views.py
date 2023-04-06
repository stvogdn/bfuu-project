
# Create your views here.
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Service, ScriptElements, Speaker
from .forms import ServiceForm, ScriptElementsForm, SpeakerForm

def create_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.coordinator = request.user
            service.save()
            return redirect('services-service_list')
    else:
        form = ServiceForm()
    return render(request, 'services/service_form.html', {'form': form})

def service_list(request):
    services = Service.objects.all().order_by('-service_date')
    return render(request, 'services/service_list.html', {'services': services})

def add_scriptelements(request):
    if request.method == 'POST':
        form = ScriptElementsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('services-scriptelements_list')
    else:
        form = ScriptElementsForm()
    return render(request, 'services/scriptelements_form.html', {'form': form})

def scriptelements_list(request):
    services = ScriptElements.objects.all().order_by('-service_date')
    return render(request, 'services/service_list.html', {'services': services})

def add_speaker(request):
    if request.method == 'POST':
        form = SpeakerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('services-speaker_list')
    else:
        form = SpeakerForm()
    return render(request, 'services/add_speaker.html', {'form': form})

def speaker_list(request):
    speakers = Speaker.objects.all()
    return render(request, 'services/speaker_list.html', {'speakers': speakers})