from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('health_monitor',views.health_monitor,name='health_monitor'),
    path('blood_serum',views.blood_serum,name='blood_serum'),
    path('section_insch',views.section_insch,name='section_insch'),
    path('section_outsch',views.section_outsch,name='section_outsch'),
    path('section_industry',views.section_industry,name='section_industry'),
    path('monthly_settlement',views.monthly_settlement,name='monthly_settlement'),
    path('QC_view',views.QC_view,name='QC_view'),
    path('SC_view',views.SC_view,name='SC_view'),
    path('PC_IN_view',views.PC_IN_view,name='PC_IN_view'),
    path('PC_OUT_view',views.PC_OUT_view,name='PC_OUT_view'),
    path('PC_IND_view',views.PC_IND_view,name='PC_IND_view'),
    path('monthly_settlement_view',views.monthly_settlement_view,name='monthly_settlement_view'),
    
    path('delete_form',views.delete_form,name='delete_form'),

    path('update_pay',views.update_pay,name='update_pay'),

]   