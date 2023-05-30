from django.shortcuts import render,redirect
from .models import *
from django.utils import timezone
import xlwings as xw
from django.template.loader import render_to_string
from django.http import JsonResponse
import os
# Create your views here.
def index(request):
    return render(request,'index.html')


def health_monitor(request):
    year = timezone.now().year
    max_id= Max_ID.objects.get().QC_max   
    print(max_id[:4] ) 
    if year == int(max_id[:4]):
        num = int(max_id[6:])+1
        qc_id =  f"{year}QC{str(num).zfill(4)}"
    else:
        num=1
        qc_id =  f"{year}QC{str(num).zfill(4)}"
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
        # wb= load_workbook('C:/Users/user/ntumclab/venv/userform/form/static/健康監測手開帳單v1.0.xlsx',read_only=False, write_only=False)
        # print(wb.sheetnames)
       
        
        # # Open the template file and create a copy of the worksheet
       
        
        # # Iterate over the cells to copy data and formatting
       
        # ws = wb.get_sheet_by_name('Sheet1 ')
        # ws.cell(row=4,column=2,value=department)
        # ws.cell(row=5,column=2,value=pi)
        # ws.cell(row=5,column=5,value=lab_tel)
        # ws.cell(row=6,column=2,value=contact)
        # ws.cell(row=6,column=5,value=contact_tel)
        # ws.cell(row=11,column=5,value=number)
        # ws.cell(row=7,column=2,value=date)
        # ws.cell(row=2,column=6,value=qc_id)
       
        # new_file_path = (f"C:/Users/user/Desktop/手開單/健康監測/{qc_id}.xlsx")
        # ws.save(new_file_path)       
        wb = xw.Book('C:/Users/user/ntumclab/venv/userform/form/static/健康監測手開帳單v1.0.xlsx')
        ws = wb.sheets['Sheet1 ']
        ws.range('B4').value = department
        ws.range('B5').value = pi
        ws.range('E5').value = lab_tel
        ws.range('B6').value = contact
        ws.range('E6').value = contact_tel
        ws.range('E11').value = number
        ws.range('B7').value = date
        ws.range('F2').value = qc_id
        new_file_path = f"C:/Users/user/Desktop/手開單/健康監測/{qc_id}.xlsx"
        wb.save(new_file_path)
        qc_file=QC.objects.get(qcid=qc_id)
        qc_file.file= new_file_path
        qc_file.save()
        return redirect('QC_view')
    return render(request,'health_monitor.html',context)

def blood_serum(request):
    year = timezone.now().year
    max_id= Max_ID.objects.get().SC_max
    if year == int(max_id[:4]):
        num = int(max_id[6:])+1
        sc_id =  f"{year}SC{str(num).zfill(4)}"
    else:
        num=1
        sc_id =  f"{year}SC{str(num).zfill(4)}"
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
        wb = xw.Book('C:/Users/user/ntumclab/venv/userform/form/static/血液血清手開帳單v1.0.xlsx')
        ws = wb.sheets['Sheet1 ']
        ws.range('B4').value = department
        ws.range('B5').value = pi
        ws.range('E5').value = lab_tel
        ws.range('B6').value = contact
        ws.range('E6').value = contact_tel
        ws.range('E11').value =serum
        ws.range('E12').value =blood
        ws.range('B7').value =date
        ws.range('F2').value =sc_id
        new_file_path = (f"C:/Users/user/Desktop/手開單/血液血清/{sc_id}.xlsx")
        wb.save(new_file_path)
       
        sc_file=SC.objects.get(scid=sc_id)
        sc_file.file= new_file_path
        sc_file.save()
        return redirect('SC_view')
    return render(request,'blood_serum.html',context)

def section_insch(request):
    year = timezone.now().year
    max_id= Max_ID.objects.get().PC_max
    if year == int(max_id[:4]):
        num = int(max_id[6:])+1
        pc_id =  f"{year}PC{str(num).zfill(4)}"
    else:
        num=1
        pc_id =  f"{year}PC{str(num).zfill(4)}"
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
        wb = xw.Book('C:/Users/user/ntumclab/venv/userform/form/static/病理切片校內.xlsx')
        ws = wb.sheets['Sheet1 ']
        ws.range('B4').value = department
        ws.range('B5').value = pi
        ws.range('E5').value = lab_tel
        ws.range('B6').value = contact
        ws.range('E6').value = contact_tel
        ws.range('E11').value =a
        ws.range('E12').value =b
        ws.range('E13').value =c
        ws.range('E14').value =d
        ws.range('E15').value =e
        ws.range('E16').value =f
        ws.range('E17').value =g
        ws.range('E18').value =h
        ws.range('E19').value =i
        ws.range('E20').value =j
        ws.range('E21').value =k
        ws.range('B7').value =date
        ws.range('B27').value =pc_id
        new_file_path = (f"C:/Users/user/Desktop/手開單/校內/{pc_id}.xlsx")
        wb.save(new_file_path)
       
        sc_file=PC_INS.objects.get(pc_ins_id=pc_id)
        sc_file.file= new_file_path
        sc_file.save()
        return redirect('PC_IN_view')

    return render(request,'section_insch.html',context)

def section_outsch(request):
    year = timezone.now().year
    max_id= Max_ID.objects.get().PC_max
    if year == int(max_id[:4]):
        num = int(max_id[6:])+1
        pc_id =  f"{year}PC{str(num).zfill(4)}"
    else:
        num=1
        pc_id =  f"{year}PC{str(num).zfill(4)}"
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
        wb = xw.Book('C:/Users/user/ntumclab/venv/userform/form/static/病理切片校外.xlsx')
        ws = wb.sheets['Sheet1 ']
        ws.range('B4').value = department
        ws.range('B5').value = pi
        ws.range('E5').value = lab_tel
        ws.range('B6').value = contact
        ws.range('E6').value = contact_tel
        ws.range('E11').value =a
        ws.range('E12').value =b
        ws.range('E13').value =c
        ws.range('E14').value =d
        ws.range('E15').value =e
        ws.range('E16').value =f
        ws.range('E17').value =g
        ws.range('E18').value =h
        ws.range('E19').value =i
        ws.range('E20').value =j
        ws.range('E21').value =k
        ws.range('B7').value =date
        ws.range('B29').value =pc_id
        new_file_path = (f"C:/Users/user/Desktop/手開單/校外/{pc_id}.xlsx")
        wb.save(new_file_path)
       
        sc_file=PC_OUS.objects.get(pc_out_id=pc_id)
        sc_file.file= new_file_path
        sc_file.save()
        return redirect('PC_OUT_view')
    return render(request,'section_outsch.html',context)

def section_industry(request):
    year = timezone.now().year
    max_id= Max_ID.objects.get().PC_max
    if year == int(max_id[:4]):
        num = int(max_id[6:])+1
        pc_id =  f"{year}PC{str(num).zfill(4)}"
    else:
        num=1
        pc_id =  f"{year}PC{str(num).zfill(4)}"
    context={'PC_ID':pc_id}
    if request.method == 'POST':
        department=request.POST['department']
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
        NEW_PC_IND = PC_IND.objects.create(department=department,date=date,contact=contact,contact_tel=contact_tel,A=a,B=b,C=c,D=d,E=e,F=f,G=g,H=h,I=i,J=j,K=k)
        NEW_PC_IND.save()
        wb = xw.Book('C:/Users/user/ntumclab/venv/userform/form/static/病理產業價.xlsx')
        ws = wb.sheets['Sheet1 ']
        ws.range('B4').value = department
        ws.range('B5').value = contact
        ws.range('E5').value = contact_tel
        ws.range('E10').value =a
        ws.range('E11').value =b
        ws.range('E12').value =c
        ws.range('E13').value =d
        ws.range('E14').value =e
        ws.range('E15').value =f
        ws.range('E16').value =g
        ws.range('E17').value =h
        ws.range('E18').value =i
        ws.range('E19').value =j
        ws.range('E20').value =k
        ws.range('B6').value =date
        ws.range('B26').value =pc_id
        new_file_path = (f"C:/Users/user/Desktop/手開單/產業/{pc_id}.xlsx")
        wb.save(new_file_path)
        sc_file=PC_IND.objects.get(pc_ind_id=pc_id)
        sc_file.file= new_file_path
        sc_file.save()
        return redirect('PC_IND_view')
    return render(request,'section_industry.html',context)


def  QC_view(request):
    
    QCs=QC.objects.all().order_by('-date')
    
    context={
        'QCs':QCs
    }

    return render(request,'back/health_monitor_list.html',context)
def  SC_view(request):
    
    SCs=SC.objects.all().order_by('-date')
    form_type=SC
    context={
        'SCs':SCs,
        'form_type':form_type
    }

    return render(request,'back/blood&serun_list.html',context)
def  PC_IN_view(request):
    PCs=PC_INS.objects.all().order_by('-date')
    context={
        'PCs':PCs
    }
    return render(request,'back/section_insch_list.html',context)
def  PC_OUT_view(request):
    PCs=PC_OUS.objects.all().order_by('-date')
    context={
        'PCs':PCs
    }
    return render(request,'back/section_outsch_list.html',context)

def  PC_IND_view(request):
    PCs=PC_IND.objects.all().order_by('-date')
    context={
        'PCs':PCs
    }
    return render(request,'back/section_ind_list.html',context)

def delete_form(request):
    form_type=request.GET['form_type']
    form_id =request.GET['id']
    if form_type == 'QC':
        object_data = QC.objects.get(qcid=form_id)
        file_path = os.path.abspath(object_data.file)
        os.remove(file_path)
        object_data.delete()        
        all_form=QC.objects.all().order_by('-date')
        data= render_to_string('back/async/qclist.html',{'QCs':all_form})
        return JsonResponse({'data':data})
    elif form_type == 'SC':
        object_data = SC.objects.get(scid=form_id)
        file_path = os.path.abspath(object_data.file)
        os.remove(file_path)
        object_data.delete()        
        all_form=SC.objects.all().order_by('-date')
        data= render_to_string('back/async/qclist.html',{'SCs':all_form})
        return JsonResponse({'data':data})
    elif form_type == 'PC_INS':
        object_data = PC_INS.objects.get(pc_ins_id=form_id)
        file_path = os.path.abspath(object_data.file)
        os.remove(file_path)
        object_data.delete()        
        all_form=PC_INS.objects.all().order_by('-date')
        data= render_to_string('back/async/pcinslist.html',{'PCs':all_form})
        return JsonResponse({'data':data})
    elif form_type == 'PC_OUS':
        object_data = PC_OUS.objects.get(pc_out_id=form_id)
        file_path = os.path.abspath(object_data.file)
        os.remove(file_path)
        object_data.delete()        
        all_form=PC_OUS.objects.all().order_by('-date')
        data= render_to_string('back/async/pcinslist.html',{'PCs':all_form,'pc_type':PC_OUS})
        return JsonResponse({'data':data})
    else:
        object_data = PC_IND.objects.get(pc_ind_id=form_id)
        file_path = os.path.abspath(object_data.file)
        os.remove(file_path)
        object_data.delete()        
        all_form=PC_IND.objects.all().order_by('-date')
        data= render_to_string('back/async/pcinslist.html',{'PCs':all_form,'pc_type':PC_IND})
        return JsonResponse({'data':data})












