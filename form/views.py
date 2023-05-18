from django.shortcuts import render,redirect
from .models import *
from django.utils import timezone


# Create your views here.
def index(request):
    return render(request,'index.html')


def health_monitor(request):
    year = timezone.now().year
    max_id= Max_ID.objects.get().QC_max   
    print(max_id[:4] ) 
    if year == int(max_id[:4]):
        num = int(max_id[6:])+1
        qc_id =  f"{year}QC{str(num).zfill(3)}"
    else:
        num=1
        qc_id =  f"{year}QC{str(num).zfill(3)}"
    print(qc_id)
    context={'QC_ID':qc_id}
    if request.method == 'POST':
        department=request.POST['department']
        pi=request.POST['pi']
        lab_tel=request.POST['lab-phone']
        contact=request.POST['contact']
        contact_tel=request.POST['contact-number']
        number=request.POST['sample-number']
        date= request.POST['date']
        NEW_QC=QC.objects.create(department=department,date=date,pi=pi,lab_tel=lab_tel,contact=contact,contact_tel=contact_tel,number=number)
        NEW_QC.save()
        return redirect('index')
    return render(request,'health_monitor.html',context)

def blood_serum(request):
    year = timezone.now().year
    max_id= Max_ID.objects.get().SC_max
    if year == int(max_id[:4]):
        num = int(max_id[6:])+1
        sc_id =  f"{year}SC{str(num).zfill(3)}"
    else:
        num=1
        sc_id =  f"{year}SC{str(num).zfill(3)}"
    context={'SC_ID':sc_id}
    if request.method == 'POST':
        department=request.POST['department1']
        pi=request.POST['pi1']
        lab_tel=request.POST['lab-phone1']
        contact=request.POST['contact1']
        contact_tel=request.POST['contact-number1']
        serum=request.POST['serum-number']
        blood=request.POST['blood-number']
        date= request.POST['date']
        NEW_SC = SC.objects.create(department=department,date=date,pi=pi,lab_tel=lab_tel,contact=contact,contact_tel=contact_tel,serum=serum,bloodcell=blood)
        NEW_SC.save()
        return redirect('index')
    return render(request,'blood_serum.html',context)

def section_insch(request):
    year = timezone.now().year
    max_id= Max_ID.objects.get().PC_max
    if year == int(max_id[:4]):
        num = int(max_id[6:])+1
        pc_id =  f"{year}PC{str(num).zfill(3)}"
    else:
        num=1
        pc_id =  f"{year}PC{str(num).zfill(3)}"
    context={'PC_ID':pc_id}
    if request.method == 'POST':
        department=request.POST['department']
        pi=request.POST['pi']
        lab_tel=request.POST['lab-phone']
        contact=request.POST['contact']
        contact_tel=request.POST['contact-number']
        a=request.POST['a']
        b=request.POST['b']
        c=request.POST['c']
        d=request.POST['d']
        e=request.POST['e']
        f=request.POST['f']
        g=request.POST['g']
        h=request.POST['h']
        i=request.POST['i']
        j=request.POST['j']
        k=request.POST['k']
        date= request.POST['date']
        NEW_PC_INS = PC_INS.objects.create(department=department,date=date,pi=pi,lab_tel=lab_tel,contact=contact,contact_tel=contact_tel,A=a,B=b,C=c,D=d,E=e,F=f,G=g,H=h,I=i,J=j,K=k)
        NEW_PC_INS.save()
        return redirect('index')

    return render(request,'section_insch.html',context)

def section_outsch(request):
    year = timezone.now().year
    max_id= Max_ID.objects.get().PC_max
    if year == int(max_id[:4]):
        num = int(max_id[6:])+1
        pc_id =  f"{year}PC{str(num).zfill(3)}"
    else:
        num=1
        pc_id =  f"{year}PC{str(num).zfill(3)}"
    context={'PC_ID':pc_id}
    if request.method == 'POST':
        department=request.POST['department']
        pi=request.POST['pi']
        lab_tel=request.POST['lab-phone']
        contact=request.POST['contact']
        contact_tel=request.POST['contact-number']
        a=request.POST['a']
        b=request.POST['b']
        c=request.POST['c']
        d=request.POST['d']
        e=request.POST['e']
        f=request.POST['f']
        g=request.POST['g']
        h=request.POST['h']
        i=request.POST['i']
        j=request.POST['j']
        k=request.POST['k']
        date= request.POST['date']
        NEW_PC_OUS = PC_OUS.objects.create(department=department,date=date,pi=pi,lab_tel=lab_tel,contact=contact,contact_tel=contact_tel,A=a,B=b,C=c,D=d,E=e,F=f,G=g,H=h,I=i,J=j,K=k)
        NEW_PC_OUS.save()
        return redirect('index')
    return render(request,'section_outsch.html',context)

def section_industry(request):
    year = timezone.now().year
    max_id= Max_ID.objects.get().PC_max
    if year == int(max_id[:4]):
        num = int(max_id[6:])+1
        pc_id =  f"{year}PC{str(num).zfill(3)}"
    else:
        num=1
        pc_id =  f"{year}PC{str(num).zfill(3)}"
    context={'PC_ID':pc_id}
    if request.method == 'POST':
        department=request.POST['department']
        pi=request.POST['pi']
        lab_tel=request.POST['lab-phone']
        contact=request.POST['contact']
        contact_tel=request.POST['contact-number']
        a=request.POST['a']
        b=request.POST['b']
        c=request.POST['c']
        d=request.POST['d']
        e=request.POST['e']
        f=request.POST['f']
        g=request.POST['g']
        h=request.POST['h']
        i=request.POST['i']
        j=request.POST['j']
        k=request.POST['k']
        date= request.POST['date']
        NEW_PC_IND = PC_IND.objects.create(department=department,date=date,pi=pi,lab_tel=lab_tel,contact=contact,contact_tel=contact_tel,A=a,B=b,C=c,D=d,E=e,F=f,G=g,H=h,I=i,J=j,K=k)
        NEW_PC_IND.save()
        return redirect('index')
    return render(request,'section_industry.html',context)
