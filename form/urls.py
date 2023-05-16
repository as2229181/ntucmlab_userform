from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('health_monitor',views.health_monitor,name='health_monitor'),
    path('blood_serum',views.blood_serum,name='blood_serum'),
    path('section_insch',views.section_insch,name='section_insch'),
    path('section_outsch',views.section_outsch,name='section_outsch'),
    path('section_industry',views.section_industry,name='section_industry'),
]