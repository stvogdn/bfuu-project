from django.urls import path
from .views import (
    ServiceListView, 
    ServiceDetailView,
    ServiceCreateView,
    ServiceUpdateView,
    ServiceDeleteView,
    ScriptElementsListView, 
    ScriptElementsDetailView, 
    ScriptElementsCreateView, 
    ScriptElementsUpdateView,
    ScriptElementsDeleteView,
    SpeakerListView,
    SpeakerDetailView,
    SpeakerCreateView,
    SpeakerUpdateView,
    SpeakerDeleteView
)
#app_name = 'services'
urlpatterns = [
    path('create_service', ServiceCreateView.as_view(), name='services-create_service'),
    path('list_services', ServiceListView.as_view(), name='services-list_services'),
    path('update_service/<int:pk>/', ServiceUpdateView.as_view(), name='services-update_service'),
    path('delete_service/<int:pk>/', ServiceDeleteView.as_view(), name='services-delete_service'),
    path('service_detail/<int:pk>/', ServiceDetailView.as_view(), name='services-service_detail'),
    path('add_script_elements', ScriptElementsCreateView.as_view(), name='services-add_script_elements'),
    path('list_script_elements', ScriptElementsListView.as_view(), name='services-list_script_elements'),
    path('add_speaker', SpeakerCreateView.as_view(), name='services-add_speaker'),
    path('list_speakers', SpeakerListView.as_view(), name='services-list_speakers'),
    path('update_speaker/<int:pk>/', SpeakerUpdateView.as_view(), name='services-update_speaker'),
    path('delete_speaker/<int:pk>/', SpeakerDeleteView.as_view(), name='services-delete_speaker'),
    path('speaker_detail/<int:pk>/', SpeakerDetailView.as_view(), name='services-speaker_detail'),

]