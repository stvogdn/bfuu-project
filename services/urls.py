from django.urls import path
from . import views

urlpatterns = [
    path('create_segment_type', views.create_segment_type, name='services-create_segment_type'),
    path('create_service', views.create_service, name='services-create_service'),
    path('list', views.service_list, name='services-service_list'),
    path('segmenttype_list', views.segmenttype_list, name='services-segmenttype_list'),
    path('add_script_elements', views.add_script_elements, name='services-add_script_elements'),
]