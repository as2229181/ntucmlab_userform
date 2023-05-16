from django.shortcuts import render
from .models import *
from django.utils import timezone

# Create your views here.
def index(request):
    return render(request,'index.html')


def health_monitor(request):
    year = timezone.now().year
    max_id= Max_ID.objects.get().QC_max
    
    if year == int(max_id[:3]):
        num = int(max_id[6:])+1
        qc_id =  f"{year}QC{str(num).zfill(3)}"
    else:
        num=1
        qc_id =  f"{year}QC{str(num).zfill(3)}"
        
    context={'QC_ID':qc_id}

    return render(request,'health_monitor.html',context)

def blood_serum(request):
    return render(request,'blood_serum.html')

def section_insch(request):
    return render(request,'section_insch.html')

def section_outsch(request):
    return render(request,'section_outsch.html')

def section_industry(request):
    return render(request,'section_industry.html')
