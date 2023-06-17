from django.shortcuts import render,redirect
from .models import *
from django.utils import timezone
import xlwings as xw
from django.template.loader import render_to_string
from django.http import JsonResponse,HttpResponse
from .utils import convert_to_pdf,IDgenerator,pay_status_change
import subprocess
import os
# Create your views here.
def index(request):
    return render(request,'index.html')


def health_monitor(request):
    year = timezone.now().year
    max_id= Max_ID.objects.get().QC_max   
    print(max_id[:4] ) 
    qc_id=IDgenerator(year,max_id,'QC')
    print(qc_id)
    context={'QC_ID':qc_id}
    if request.method == 'POST':
        department=request.POST['department']
        pi=request.POST['pi']
        lab_tel=request.POST['lab-phone']
        contact=request.POST['contact']
        contact_tel=request.POST['contact-number']
        mus_number=request.POST['mus-number']
        rat_number=request.POST['rat-number']
        date= request.POST['date']
        description =request.POST['description']
        Pi,created = Principal_Investigator.objects.get_or_create(department=department,pi=pi,lab_tel=lab_tel)
        contact1,created =Contact.objects.get_or_create(pi=Pi,name=contact,contact_number=contact_tel)      
        QC.objects.create(pi=Pi,date=date,description=description,mus_number=mus_number,rat_number=rat_number,contact=contact1)    
        wb = xw.Book('C:/Users/user/ntumclab/venv/userform/form/static/健康監測手開帳單v1.0.xlsx')
        ws = wb.sheets['Sheet1 ']
        ws.range('B4').value = department
        ws.range('B5').value = pi
        ws.range('E5').value = lab_tel
        ws.range('B6').value = contact
        ws.range('E6').value = contact_tel
        ws.range('E11').value = mus_number
        ws.range('E12').value = rat_number
        ws.range('B7').value = date
        ws.range('F2').value = qc_id
        ws.range('B17').value=description
        password='88516'
        # 使用 Excel VBA 的 Protect 方法
        ws.api.Cells.Locked = True
        ws.api.Protect(Password=password)
        excel_file_path = f"C:/Users/user/Desktop/手開單/健康監測/excel/{qc_id}.xlsx"
        pdf_file_path = f"C:/Users/user/Desktop/手開單/健康監測/pdf/{qc_id}.pdf"
        wb.save(excel_file_path)
        wb.close()
        convert_to_pdf(excel_file_path,pdf_file_path)
        subprocess.run(['start', pdf_file_path], shell=True)
        qc_file=QC.objects.get(qcid=qc_id)
        qc_file.excel_file,qc_file.pdf_file= excel_file_path,pdf_file_path
        qc_file.save()
        return redirect('QC_view')
    return render(request,'health_monitor.html',context)

def blood_serum(request):
    year = timezone.now().year
    max_id= Max_ID.objects.get().SC_max
    sc_id=IDgenerator(year,max_id,'SC')
    context={'SC_ID':sc_id}
    if request.method == 'POST':
        department=request.POST['department']
        pi=request.POST['pi']
        lab_tel=request.POST['lab-phone']
        contact=request.POST['contact1']
        contact_tel=request.POST['contact-number']
        serum=request.POST['serum-number']
        CBC=request.POST['blood-number']
        date= request.POST['date']
        description =request.POST['description']
        申請單編號 =request.POST['apply-number']
        Pi,created = Principal_Investigator.objects.get_or_create(department=department,pi=pi,lab_tel=lab_tel)
        contact1,created =Contact.objects.get_or_create(pi=Pi,name=contact,contact_number=contact_tel)   
        SC.objects.create(申請單編號=申請單編號,description=description,date=date,pi=Pi,contact=contact1,serum=serum,CBC=CBC)
        wb = xw.Book('C:/Users/user/ntumclab/venv/userform/form/static/血液血清手開帳單v1.0.xlsx')
        ws = wb.sheets['Sheet1 ']
        ws.range('B4').value = department
        ws.range('B5').value = pi
        ws.range('E5').value = lab_tel
        ws.range('B6').value = contact
        ws.range('E6').value = contact_tel
        ws.range('E11').value =serum
        ws.range('E12').value =CBC
        ws.range('B7').value =date
        ws.range('F2').value =sc_id
        ws.range('B18').value =申請單編號
        ws.range('B17').value=description
        password='88516'
        # 使用 Excel VBA 的 Protect 方法
        ws.api.Cells.Locked = True
        ws.api.Protect(Password=password)
        excel_file_path = (f"C:/Users/user/Desktop/手開單/血液血清/excel/{sc_id}.xlsx")
        pdf_file_path= (f"C:/Users/user/Desktop/手開單/血液血清/pdf/{sc_id}.pdf")
        wb.save(excel_file_path)
        wb.close()
        convert_to_pdf(excel_file_path,pdf_file_path)
        subprocess.run(['start', pdf_file_path], shell=True)
        sc_file=SC.objects.get(scid=sc_id)
        sc_file.excel_file,sc_file.pdf_file= excel_file_path,pdf_file_path
        sc_file.save()
        return redirect('SC_view')
    return render(request,'blood_serum.html',context)

def section_insch(request):
    year = timezone.now().year
    max_id= Max_ID.objects.get().PC_max
    pc_id=IDgenerator(year,max_id,'PC')
    context={'PC_ID':pc_id}
    if request.method == 'POST':
        department=request.POST['department']
        pi=request.POST['pi']
        lab_tel=request.POST['lab-phone']
        contact=request.POST['contact']
        contact_tel=request.POST['contact-number']
        description=request.POST['description']
        申請單編號 =request.POST['apply-number']
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
        Pi,created = Principal_Investigator.objects.get_or_create(department=department,pi=pi,lab_tel=lab_tel)
        contact1,created =Contact.objects.get_or_create(pi=Pi,name=contact,contact_number=contact_tel)   
        PC_INS.objects.create(申請單編號=申請單編號,description=description,date=date,pi=Pi,contact=contact1,A=a,B=b,C=c,D=d,E=e,F=f,G=g,H=h,I=i,J=j,K=k)
        wb = xw.Book('C:/Users/user/ntumclab/venv/userform/form/static/病理切片校內 v2.0.xlsx')
        ws = wb.sheets['Sheet1 ']
        ws.range('B4').value = department
        ws.range('B5').value = pi
        ws.range('E5').value = lab_tel
        ws.range('B6').value = contact
        ws.range('E6').value = contact_tel
        ws.range('B26').value = description
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
        ws.range('B27').value =申請單編號
        ws.range('F2').value =pc_id
        password='88516'
        # 使用 Excel VBA 的 Protect 方法
        ws.api.Cells.Locked = True
        ws.api.Protect(Password=password)
        excel_file_path = (f"C:/Users/user/Desktop/手開單/校內/excel/{pc_id}.xlsx")
        pdf_file_path = (f"C:/Users/user/Desktop/手開單/校內/pdf/{pc_id}.pdf")
        wb.save(excel_file_path)
        wb.close()
        convert_to_pdf(excel_file_path,pdf_file_path)
        subprocess.run(['start', pdf_file_path], shell=True)
        sc_file=PC_INS.objects.get(pc_ins_id=pc_id)
        sc_file.excel_file,sc_file.pdf_file= excel_file_path,pdf_file_path
        sc_file.save()
        return redirect('PC_IN_view')

    return render(request,'section_insch.html',context)

def section_outsch(request):
    year = timezone.now().year
    max_id= Max_ID.objects.get().PC_max
    pc_id=IDgenerator(year,max_id,'PC')
    context={'PC_ID':pc_id}
    if request.method == 'POST':
        department=request.POST['department']
        pi=request.POST['pi']
        lab_tel=request.POST['lab-phone']
        contact=request.POST['contact']
        contact_tel=request.POST['contact-number']
        description=request.POST['description']
        申請單編號 =request.POST['apply-number']
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
        Pi,created = Principal_Investigator.objects.get_or_create(department=department,pi=pi,lab_tel=lab_tel)
        contact1,created =Contact.objects.get_or_create(pi=Pi,name=contact,contact_number=contact_tel)   
        NEW_PC_OUS = PC_OUS.objects.create(申請單編號=申請單編號,description=description,date=date,pi=Pi,contact=contact1,A=a,B=b,C=c,D=d,E=e,F=f,G=g,H=h,I=i,J=j,K=k)
        
        wb = xw.Book('C:/Users/user/ntumclab/venv/userform/form/static/病理切片校外 v2.0.xlsx')
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
        ws.range('B29').value =申請單編號
        ws.range('B28').value =description
        ws.range('F2').value =pc_id
        password='88516'
        # 使用 Excel VBA 的 Protect 方法
        ws.api.Cells.Locked = True
        ws.api.Protect(Password=password)
        excel_file_path = (f"C:/Users/user/Desktop/手開單/校外/excel/{pc_id}.xlsx")
        pdf_file_path = (f"C:/Users/user/Desktop/手開單/校外/pdf/{pc_id}.pdf")
        wb.save(excel_file_path)
        wb.close()
        convert_to_pdf(excel_file_path,pdf_file_path)
        subprocess.run(['start', pdf_file_path], shell=True)

        sc_file=PC_OUS.objects.get(pc_out_id=pc_id)
        sc_file.excel_file,sc_file.pdf_file= excel_file_path,pdf_file_path
        sc_file.save()
        return redirect('PC_OUT_view')
    return render(request,'section_outsch.html',context)

def section_industry(request):
    year = timezone.now().year
    max_id= Max_ID.objects.get().PC_max
    pc_id=IDgenerator(year,max_id,'PC')
    context={'PC_ID':pc_id}
    if request.method == 'POST':
        department=request.POST['department']
        contact=request.POST['contact']
        contact_tel=request.POST['contact-number']
        description=request.POST['description']
        申請單編號 =request.POST['apply-number']
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
        contact1,created =Contact.objects.get_or_create(name=contact,contact_number=contact_tel)   
        NEW_PC_IND = PC_IND.objects.create(申請單編號=申請單編號,description=description,date=date,contact=contact1,A=a,B=b,C=c,D=d,E=e,F=f,G=g,H=h,I=i,J=j,K=k)
        
        wb = xw.Book('C:/Users/user/ntumclab/venv/userform/form/static/病理產業價 v2.0.xlsx')
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
        ws.range('B26').value =申請單編號
        ws.range('B25').value =description
        ws.range('F2').value =pc_id
        password='88516'
        # 使用 Excel VBA 的 Protect 方法
        ws.api.Cells.Locked = True
        ws.api.Protect(Password=password)
        excel_file_path = (f"C:/Users/user/Desktop/手開單/產業/excel/{pc_id}.xlsx")
        pdf_file_path = (f"C:/Users/user/Desktop/手開單/產業/pdf/{pc_id}.pdf")
        wb.save(excel_file_path)
        wb.close()
        convert_to_pdf(excel_file_path,pdf_file_path)
        subprocess.run(['start', pdf_file_path], shell=True)
        sc_file=PC_IND.objects.get(pc_ind_id=pc_id)
        sc_file.excel_file,sc_file.pdf_file= excel_file_path,pdf_file_path
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
        excel_file_path = os.path.abspath(object_data.excel_file)
        pdf_file_path = os.path.abspath(object_data.pdf_file)
        os.remove(excel_file_path); os.remove(pdf_file_path)
        object_data.delete()        
        all_form=QC.objects.all().order_by('-date')
        data= render_to_string('back/async/qclist.html',{'QCs':all_form})
        return JsonResponse({'data':data})
    elif form_type == 'SC':
        object_data = SC.objects.get(scid=form_id)
        excel_file_path = os.path.abspath(object_data.excel_file)
        pdf_file_path = os.path.abspath(object_data.pdf_file)
        os.remove(excel_file_path); os.remove(pdf_file_path)
        object_data.delete()        
        all_form=SC.objects.all().order_by('-date')
        data= render_to_string('back/async/qclist.html',{'SCs':all_form})
        return JsonResponse({'data':data})
    elif form_type == 'PC_INS':
        object_data = PC_INS.objects.get(pc_ins_id=form_id)
        print(object_data)
        excel_file_path = os.path.abspath(object_data.excel_file)
        pdf_file_path = os.path.abspath(object_data.pdf_file)
        os.remove(excel_file_path); os.remove(pdf_file_path)
        object_data.delete()        
        all_form=PC_INS.objects.all().order_by('-date')
        data= render_to_string('back/async/pcinslist.html',{'PCs':all_form,'pc_type':PC_INS})
        return JsonResponse({'data':data})
    elif form_type == 'PC_OUS':
        object_data = PC_OUS.objects.get(pc_out_id=form_id)
        excel_file_path = os.path.abspath(object_data.excel_file)
        pdf_file_path = os.path.abspath(object_data.pdf_file)
        os.remove(excel_file_path); os.remove(pdf_file_path)
        object_data.delete()        
        all_form=PC_OUS.objects.all().order_by('-date')
        data= render_to_string('back/async/pcinslist.html',{'PCs':all_form,'pc_type':PC_OUS})
        return JsonResponse({'data':data})
    else:
        object_data = PC_IND.objects.get(pc_ind_id=form_id)
        excel_file_path = os.path.abspath(object_data.excel_file)
        pdf_file_path = os.path.abspath(object_data.pdf_file)
        os.remove(excel_file_path); os.remove(pdf_file_path)
        object_data.delete()        
        all_form=PC_IND.objects.all().order_by('-date')
        data= render_to_string('back/async/pcinslist.html',{'PCs':all_form,'pc_type':PC_IND})
        return JsonResponse({'data':data})

def update_pay(request):
    form_type=request.GET['form_type']

    form_id =request.GET['id']
    model_type=eval(form_type)
    data=pay_status_change(model_type,form_id)
    return JsonResponse({'data':data})
    # if form_type == 'QC':
    #     object_data = QC.objects.get(qcid=form_id)
    #     if object_data.pay == False:
    #         object_data.pay=True
    #         object_data.save()
    #         all_form=QC.objects.all().order_by('-date')
    #         data= render_to_string('back/async/qclist.html',{'QCs':all_form})
    #         return JsonResponse({'data':data})
    #     else:
    #         object_data.pay=False
    #         object_data.save()
    #         all_form=QC.objects.all().order_by('-date')
    #         data= render_to_string('back/async/qclist.html',{'QCs':all_form})
    #         return JsonResponse({'data':data})    
        
    # elif form_type == 'SC':
    #     object_data = SC.objects.get(scid=form_id)
    #     if object_data.pay == False:
    #         object_data.pay=True
    #         object_data.save()
    #         all_form=SC.objects.all().order_by('-date')
    #         data= render_to_string('back/async/sclist.html',{'SCs':all_form})
    #         return JsonResponse({'data':data})
    #     else:
    #         object_data.pay=False
    #         object_data.save()               
    #         all_form=SC.objects.all().order_by('-date')
    #         data= render_to_string('back/async/sclist.html',{'SCs':all_form})
    #         return JsonResponse({'data':data})
    # elif form_type == 'PC_INS':
    #     object_data = PC_INS.objects.get(pc_ins_id=form_id)
    #     if object_data.pay == False:
    #         object_data.pay=True
    #         object_data.save()
    #         all_form=PC_INS.objects.all().order_by('-date')
    #         data= render_to_string('back/async/pcinslist.html',{'PCs':all_form})
    #         return JsonResponse({'data':data})
    #     else:
    #         object_data.pay=False
    #         object_data.save()      
    #         all_form=PC_INS.objects.all().order_by('-date')
    #         data= render_to_string('back/async/pcinslist.html',{'PCs':all_form})
    #         return JsonResponse({'data':data})
    # elif form_type == 'PC_OUS':
    #     object_data = PC_OUS.objects.get(pc_out_id=form_id)
    #     print(object_data)
    #     if object_data.pay == False:
    #         object_data.pay=True
    #         print(1)
    #         object_data.save()
    #         all_form=PC_OUS.objects.all().order_by('-date')
    #         data= render_to_string('back/async/pcinslist.html',{'PCs':all_form,'pc_type':PC_OUS})
    #         return JsonResponse({'data':data})
    #     else:
    #         print(2)
    #         object_data.pay=False
    #         object_data.save()
    #         all_form=PC_OUS.objects.all().order_by('-date')
    #         data= render_to_string('back/async/pcinslist.html',{'PCs':all_form,'pc_type':PC_OUS})
    #         return JsonResponse({'data':data})
    # else:
    #     object_data = PC_IND.objects.get(pc_ind_id=form_id)
    #     if object_data.pay == False:
    #         object_data.pay=True
    #         object_data.save()
    #         all_form=PC_IND.objects.all().order_by('-date')
    #         data= render_to_string('back/async/pcinslist.html',{'PCs':all_form,'pc_type':PC_IND})
    #         return JsonResponse({'data':data})

    #     else:
    #         object_data.pay=False
    #         object_data.save()          
    #         all_form=PC_IND.objects.all().order_by('-date')
    #         data= render_to_string('back/async/pcinslist.html',{'PCs':all_form,'pc_type':PC_IND})
    #         return JsonResponse({'data':data})







