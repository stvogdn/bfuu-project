
# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Service, ScriptElements, Speaker

class ServiceListView(ListView):
    model = Service
    template_name = 'services/service_list.html'
    fields = ['service_date', 'speaker', 'topic', 'description', 'coordinator']
    context_object_name = 'services'
    ordering = ['-service_date']

    
class ServiceDetailView(DetailView):
    model = Service
    template_name = 'services/service_detail.html'
    context_object_name = 'service'
    #name = 'services-service_detail'
    
class ServiceCreateView(CreateView):
    model = Service
    template_name = 'services/service_create.html'
    fields = ['service_date', 'speaker', 'topic', 'description', 'coordinator']
    success_url = reverse_lazy('services-list_services')
    #name = 'services-create_service'
    
class ServiceUpdateView(UpdateView):
    model = Service
    template_name = 'services/service_create.html'
    fields = ['service_date', 'speaker', 'topic', 'description', 'coordinator']
    #name = 'update_service'
    
class ServiceDeleteView(DeleteView):
    model = Service
    template_name = 'services/service_confirm_delete.html'
    success_url = reverse_lazy('services-list_services')
    #name = 'services-delete_service'
    
class ScriptElementsListView(ListView):
    model = ScriptElements
    template_name = 'services/script_elements_list.html'
    context_object_name = 'scriptelements'
    ordering = ['-service']
    #name = 'services-list_script_elements'
    
class ScriptElementsDetailView(DetailView):
    model = ScriptElements
    template_name = 'services/script_elements_detail.html'
    context_object_name = 'scriptelement'
    
class ScriptElementsCreateView(CreateView):
    model = ScriptElements
    template_name = 'services/script_elements_create.html'
    fields = ['liturgist_name', 'prelude_hymn_number', 'prelude_hymn_name', 'opening_words', 
              'principle_or_source_number', 'principle_or_source', 'principle_or_source_text', 'first_hymn_number', 
              'first_hymn_name', 'meditation_reading', 'metta_singer', 'second_hymn_number', 'second_hymn_name', 
              'readers_names', 'singers_names', 'zoom_host_name', 'slide_manager_name', 'shared_plate_partner', 
              'final_hymn_number', 'final_hymn_name', 'circle_round_singer']
    #name = 'services-add_script_elements'
    
class ScriptElementsUpdateView(UpdateView):
    model = ScriptElements
    template_name = 'services/script_elements_create.html'
    fields = ['liturgist_name', 'prelude_hymn_number', 'prelude_hymn_name', 'opening_words', 
              'principle_or_source_number', 'principle_or_source', 'principle_or_source_text', 'first_hymn_number', 
              'first_hymn_name', 'meditation_reading', 'metta_singer', 'second_hymn_number', 'second_hymn_name', 
              'readers_names', 'singers_names', 'zoom_host_name', 'slide_manager_name', 'shared_plate_partner', 
              'final_hymn_number', 'final_hymn_name', 'circle_round_singer']   
    #name = 'services-update_script_elements'
    
class ScriptElementsDeleteView(DeleteView):
    model = ScriptElements
    template_name = 'services/script_elements_delete.html'
    success_url = reverse_lazy('services-list_script_elements')
    #name = 'services-delete_script_elements'

class SpeakerListView(ListView):
    model = Speaker
    template_name = 'services/speaker_list.html'
    context_object_name = 'speakers'
    ordering = ['name']
    #name = 'services-list_speakers'
    
class SpeakerDetailView(DetailView):
    model = Speaker
    template_name = 'services/speaker_detail.html'
    context_object_name = 'speaker'
    #name = 'services-speaker_detail'
    
class SpeakerCreateView(CreateView):
    model = Speaker
    template_name = 'services/speaker_create.html'
    fields = ['name', 'email', 'biography']
    success_url = reverse_lazy('services-list_speakers')
    #name = 'services-add_speaker'
    
class SpeakerUpdateView(UpdateView):
    model = Speaker
    template_name = 'services/speaker_create.html'
    fields = ['name', 'email', 'biography']
    #name = 'services-update_speaker'
    
class SpeakerDeleteView(DeleteView):
    model = Speaker
    template_name = 'services/speaker_confirm_delete.html'
    success_url = reverse_lazy('services-list_speakers')
    #name = 'services-delete_speaker'

