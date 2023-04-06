from django.urls import path
from . import views

urlpatterns = [
    path('create_service', views.create_service, name='services-create_service'),
    path('list', views.service_list, name='services-service_list'),
    path('add_script_elements', views.add_scriptelements, name='services-add_scriptelements'),
    path('script_elements_list', views.scriptelements_list, name='services-scriptelements_list'),
    path('add_speaker', views.add_speaker, name='services-add_speaker'),
    path('speaker_list', views.speaker_list, name='services-speaker_list'),

]