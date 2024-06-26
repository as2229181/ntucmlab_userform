from django.shortcuts import render, redirect
from .models import *
from django.utils import timezone
import xlwings as xw
from django.http import JsonResponse, HttpResponse
from .utils import convert_to_pdf, IDgenerator, pay_status_change, delete_action
from django.core.cache import cache
from .google_sheet import GoogleSheet
import subprocess
import os


# Create your views here.
def index(request):
    return render(request, "index.html")


def health_monitor(request):
    if request.method == "POST":
        form_number = request.POST["no"]
        department = request.POST["department"]
        pi = request.POST["pi"]
        lab_tel = request.POST["lab-phone"]
        contact = request.POST["contact"]
        contact_tel = request.POST["contact-number"]
        mus_number = request.POST["mus-number"]
        rat_number = request.POST["rat-number"]
        date = request.POST["date"]
        discount = request.POST["discount"]
        tax = request.POST.get("tax", "False")
        description = request.POST["description"]
        Pi, created = Principal_Investigator.objects.get_or_create(
            department=department, pi=pi, lab_tel=lab_tel
        )
        contact1, created = Contact.objects.get_or_create(
            pi=Pi, name=contact, contact_number=contact_tel
        )
        QC.objects.create(
            tax=tax,
            discount=discount,
            qcid=form_number,
            pi=Pi,
            date=date,
            description=description,
            mus_number=mus_number,
            rat_number=rat_number,
            contact=contact1,
        )
        file_path = os.path.join(
            os.path.dirname(__file__), "static", "健康監測手開帳單v3.0.xlsx"
        )
        print(file_path)
        wb = xw.Book(file_path)
        ws = wb.sheets["Sheet1 "]
        ws.range("F2").value = form_number
        ws.range("B4").value = department
        ws.range("B5").value = pi
        ws.range("E5").value = lab_tel
        ws.range("B6").value = contact
        ws.range("E6").value = contact_tel
        ws.range("E11").value = mus_number
        ws.range("E12").value = rat_number
        ws.range("B7").value = date
        ws.range("D14").value = int(discount) / 100
        ws.range("B21").value = description
        if tax == "False":
            ws.range("D17").value = 0
        total_count = ws.range("D18").value
        password = "88516"
        # 使用 Excel VBA 的 Protect 方法
        ws.api.Cells.Locked = True
        ws.api.Protect(Password=password)
        excel_file_path = f"C:/Users/user/Desktop/手開單/健康監測/excel/{form_number}.xlsx"
        pdf_file_path = f"C:/Users/user/Desktop/手開單/健康監測/pdf/{form_number}.pdf"
        wb.save(excel_file_path)
        wb.close()
        convert_to_pdf(excel_file_path, pdf_file_path)
        subprocess.run(["start", pdf_file_path], shell=True)
        qc_file = QC.objects.get(qcid=form_number)
        qc_file.excel_file, qc_file.pdf_file = excel_file_path, pdf_file_path
        qc_file.save()

        # Manpulate health minitor google sheet
        google_sheet = GoogleSheet()
        if mus_number != "0" and rat_number == "0":
            row_data = [form_number, pi, date, department, contact, '','','','','','','','', mus_number,'','','','','','',form_number, total_count ]
        elif rat_number != "0" and mus_number == "0":    
            row_data = [form_number, pi, date, department, contact, '','','','','','','','', rat_number,'','','','','','',form_number, total_count]
        elif mus_number != "0" and rat_number != "0":
            row_data = [form_number, pi, date, department, contact, '','','','','','', '','',f'Mus:{mus_number}, Rat:{rat_number}','','','','','','',form_number, total_count]
        google_sheet.health_monitor_manpulate(row_data)
        return redirect("QC_view")
    return render(request, "health_monitor.html")


def blood_serum(request):
    year = timezone.now().year
    max_id = Max_ID.objects.get().SC_max
    sc_id = IDgenerator(year, max_id, "SC")
    context = {"SC_ID": sc_id}
    if request.method == "POST":
        department = request.POST["department"]
        pi = request.POST["pi"]
        lab_tel = request.POST["lab-phone"]
        contact = request.POST["contact"]
        contact_tel = request.POST["contact-number"]
        serum = request.POST["serum-number"]
        CBC = request.POST["blood-number"]
        date = request.POST["date"]
        description = request.POST["description"]
        discount = request.POST["discount"]
        tax = request.POST.get("tax", "False")
        申請單編號 = request.POST["apply-number"]
        Pi, created = Principal_Investigator.objects.get_or_create(
            department=department, pi=pi, lab_tel=lab_tel
        )
        contact1, created = Contact.objects.get_or_create(
            pi=Pi, name=contact, contact_number=contact_tel
        )
        sc_data = SC.objects.create(
            tax=tax,
            discount=discount,
            申請單編號=申請單編號,
            description=description,
            date=date,
            pi=Pi,
            contact=contact1,
            serum=serum,
            CBC=CBC,
        )
        file_path = os.path.join(
            os.path.dirname(__file__), "static", "血液血清手開帳單v3.0.xlsx"
        )
        wb = xw.Book(file_path)
        ws = wb.sheets["Sheet1 "]
        ws.range("B4").value = department
        ws.range("B5").value = pi
        ws.range("E5").value = lab_tel
        ws.range("B6").value = contact
        ws.range("E6").value = contact_tel
        ws.range("E11").value = serum
        ws.range("E12").value = CBC
        ws.range("B7").value = date
        ws.range("F2").value = sc_id
        ws.range("B21").value = 申請單編號
        ws.range("B20").value = description
        ws.range("D14").value = int(discount) / 100
        if tax == "False":
            ws.range("D17").value = 0
        total_count = ws.range("D18").value    
        password = "88516"
        # 使用 Excel VBA 的 Protect 方法
        ws.api.Cells.Locked = True
        ws.api.Protect(Password=password)
        excel_file_path = f"C:/Users/user/Desktop/手開單/血液血清/excel/{sc_id}.xlsx"
        pdf_file_path = f"C:/Users/user/Desktop/手開單/血液血清/pdf/{sc_id}.pdf"
        wb.save(excel_file_path)
        wb.close()
        convert_to_pdf(excel_file_path, pdf_file_path)
        subprocess.run(["start", pdf_file_path], shell=True)
        sc_file = SC.objects.get(scid=sc_id)
        sc_file.excel_file, sc_file.pdf_file = excel_file_path, pdf_file_path
        sc_file.save()
        cache.set("SC", sc_data)
        
        # Manpulate google sheet
        google_sheet = GoogleSheet()
        row_data = [sc_id, pi, contact, date, department,lab_tel, contact_tel, '', '', total_count]
        google_sheet.blood_serum_manpulate(row_data)    
        return redirect("SC_view")
    return render(request, "blood_serum.html", context)


def section_insch(request):
    if request.method == "POST":
        form_number = request.POST["no"]
        department = request.POST["department"]
        pi = request.POST["pi"]
        lab_tel = request.POST["lab-phone"]
        contact = request.POST["contact"]
        contact_tel = request.POST["contact-number"]
        description = request.POST["description"]
        discount = request.POST["discount"]

        a = request.POST["a"]
        b = request.POST["b"]
        c = request.POST["c"]
        d = request.POST["d"]
        e = request.POST["e"]
        f = request.POST["f"]
        g = request.POST["g"]
        h = request.POST["h"]
        i = request.POST["i"]
        j = request.POST["j"]
        k = request.POST["k"]
        l = request.POST["l"]
        date = request.POST["date"]
        Pi, created = Principal_Investigator.objects.get_or_create(
            department=department, pi=pi, lab_tel=lab_tel
        )
        contact1, created = Contact.objects.get_or_create(
            pi=Pi, name=contact, contact_number=contact_tel
        )
        try:
            pc_ins_id = Pcid.objects.create(pcid=form_number)
        except:
            exist_pc_id = Pcid.objects.get(pcid=form_number)
            context = {"id": exist_pc_id}
            return render(request, "section_insch.html", context)
        PC_INS.objects.create(
            pc_ins_id=pc_ins_id,
            discount=discount,
            description=description,
            date=date,
            pi=Pi,
            contact=contact1,
            A=a,
            B=b,
            C=c,
            D=d,
            E=e,
            F=f,
            G=g,
            H=h,
            I=i,
            J=j,
            K=k,
            L=l
        )
        file_path = os.path.join(
            os.path.dirname(__file__), "static", "病理切片校內 v3.1.xlsx"
        )
        wb = xw.Book(file_path)
        ws = wb.sheets["Sheet1 "]
        ws.range("F2").value = form_number
        ws.range("B4").value = department
        ws.range("B5").value = pi
        ws.range("E5").value = lab_tel
        ws.range("B6").value = contact
        ws.range("E6").value = contact_tel
        ws.range("B29").value = description
        ws.range("E11").value = a
        ws.range("E12").value = b
        ws.range("E13").value = c
        ws.range("E14").value = d
        ws.range("E15").value = e
        ws.range("E16").value = f
        ws.range("E17").value = g
        ws.range("E18").value = h
        ws.range("E19").value = i
        ws.range("E20").value = j
        ws.range("E21").value = k
        ws.range("E22").value = l
        ws.range("B7").value = date
        ws.range("D24").value = int(discount) / 100
        total_count = ws.range("D26").value
        password = "88516"
        # 使用 Excel VBA 的 Protect 方法
        ws.api.Cells.Locked = True
        ws.api.Protect(Password=password)
        excel_file_path = f"C:/Users/user/Desktop/手開單/校內/excel/{form_number}.xlsx"
        pdf_file_path = f"C:/Users/user/Desktop/手開單/校內/pdf/{form_number}.pdf"
        wb.save(excel_file_path)
        wb.close()
        convert_to_pdf(excel_file_path, pdf_file_path)
        subprocess.run(["start", pdf_file_path], shell=True)
        sc_file = PC_INS.objects.get(pc_ins_id=pc_ins_id)
        sc_file.excel_file, sc_file.pdf_file = excel_file_path, pdf_file_path
        sc_file.save()
        # Manpulate google sheet
        google_sheet = GoogleSheet()
        search_value = form_number
        value_to_update = {"B":pi, "C":contact, "D":a, "E":b, "F":c, "G":d, "H":e, "I":f, "J":g, "K":h, "L":i, "M":j, "N":k, "O":l, "P":total_count, "Q":description, "U":date, "V":department}
        google_sheet.section_manpulate(search_value, value_to_update)
        return redirect("PC_IN_view")

    return render(request, "section_insch.html")


def section_outsch(request):
    if request.method == "POST":
        form_number = request.POST["no"]
        department = request.POST["department"]
        pi = request.POST["pi"]
        lab_tel = request.POST["lab-phone"]
        contact = request.POST["contact"]
        contact_tel = request.POST["contact-number"]
        description = request.POST["description"]

        a = request.POST["a"]
        b = request.POST["b"]
        c = request.POST["c"]
        d = request.POST["d"]
        e = request.POST["e"]
        f = request.POST["f"]
        g = request.POST["g"]
        h = request.POST["h"]
        i = request.POST["i"]
        j = request.POST["j"]
        k = request.POST["k"]
        l = request.POST["l"]
        tax = request.POST.get("tax", "False")
        
        discount = request.POST["discount"]
        date = request.POST["date"]
        Pi, created = Principal_Investigator.objects.get_or_create(
            department=department, pi=pi, lab_tel=lab_tel
        )
        contact1, created = Contact.objects.get_or_create(
            pi=Pi, name=contact, contact_number=contact_tel
        )
        try:
            pc_out_id = Pcid.objects.create(pcid=form_number)
        except:
            exist_pc_id = Pcid.objects.get(pcid=form_number)
            context = {"id": exist_pc_id}
            return render(request, "section_insch.html", context)
        NEW_PC_OUS = PC_OUS.objects.create(
            pc_out_id=pc_out_id,
            discount=discount,
            description=description,
            date=date,
            pi=Pi,
            contact=contact1,
            tax=tax,
            A=a,
            B=b,
            C=c,
            D=d,
            E=e,
            F=f,
            G=g,
            H=h,
            I=i,
            J=j,
            K=k,
            L=l
        )
        if tax == "True":
            file_path = os.path.join(
                os.path.dirname(__file__), "static", "病理切片校外含稅 v3.1.xlsx"
            )
        else:
            file_path = os.path.join(
                os.path.dirname(__file__), "static", "病理切片校外 v3.1.xlsx"
            )
        wb = xw.Book(file_path)
        ws = wb.sheets["Sheet1 "]
        ws.range("B4").value = department
        ws.range("B5").value = pi
        ws.range("E5").value = lab_tel
        ws.range("B6").value = contact
        ws.range("E6").value = contact_tel
        ws.range("E11").value = a
        ws.range("E12").value = b
        ws.range("E13").value = c
        ws.range("E14").value = d
        ws.range("E15").value = e
        ws.range("E16").value = f
        ws.range("E17").value = g
        ws.range("E18").value = h
        ws.range("E19").value = i
        ws.range("E20").value = j
        ws.range("E21").value = k
        ws.range("E22").value = l
        ws.range("B7").value = date

        ws.range("B27").value = description
        ws.range("F2").value = form_number
        total_count = ws.range("D24").value
        password = "88516"
        # 使用 Excel VBA 的 Protect 方法
        ws.api.Cells.Locked = True
        ws.api.Protect(Password=password)
        excel_file_path = f"C:/Users/user/Desktop/手開單/校外/excel/{form_number}.xlsx"
        pdf_file_path = f"C:/Users/user/Desktop/手開單/校外/pdf/{form_number}.pdf"
        wb.save(excel_file_path)
        wb.close()
        convert_to_pdf(excel_file_path, pdf_file_path)
        subprocess.run(["start", pdf_file_path], shell=True)

        sc_file = PC_OUS.objects.get(pc_out_id=pc_out_id)
        sc_file.excel_file, sc_file.pdf_file = excel_file_path, pdf_file_path
        sc_file.save()

        google_sheet = GoogleSheet()
        search_value = form_number
        value_to_update = {"B":pi, "C":contact, "D":a, "E":b, "F":c, "G":d, "H":e, "I":f, "J":g, "K":h, "L":i, "M":j, "N":k, "O":l, "P":total_count, "Q":description, "U":date, "V":department}
        google_sheet.section_manpulate(search_value, value_to_update)
        return redirect("PC_OUT_view")
    return render(request, "section_outsch.html")


def section_industry(request):
    if request.method == "POST":
        form_number = request.POST["no"]
        department = request.POST["department"]
        contact = request.POST["contact"]
        contact_tel = request.POST["contact-number"]
        description = request.POST["description"]
        
        a = request.POST["a"]
        b = request.POST["b"]
        c = request.POST["c"]
        d = request.POST["d"]
        e = request.POST["e"]
        f = request.POST["f"]
        g = request.POST["g"]
        h = request.POST["h"]
        i = request.POST["i"]
        j = request.POST["j"]
        k = request.POST["k"]
        l = request.POST["l"]
        tax = request.POST.get("tax", "False")
        date = request.POST["date"]
        contact1, created = Contact.objects.get_or_create(
            pi=None, name=contact, contact_number=contact_tel
        )
        try:
            pc_ind_id = Pcid.objects.create(pcid=form_number)
        except:
            exist_pc_id = Pcid.objects.get(pcid=form_number)
            context = {"id": exist_pc_id}
            return render(request, "section_insch.html", context)
        NEW_PC_IND = PC_IND.objects.create(
            pc_ind_id=pc_ind_id,
            tax=tax,
            description=description,
            date=date,
            contact=contact1,
            A=a,
            B=b,
            C=c,
            D=d,
            E=e,
            F=f,
            G=g,
            H=h,
            I=i,
            J=j,
            K=k,
            L=l
        )

        file_path = os.path.join(os.path.dirname(__file__), "static", "病理產業價 v3.1.xlsx")
        wb = xw.Book(file_path)
        ws = wb.sheets["Sheet1 "]
        ws.range("B4").value = department
        ws.range("B5").value = contact
        ws.range("E5").value = contact_tel
        ws.range("E10").value = a
        ws.range("E11").value = b
        ws.range("E12").value = c
        ws.range("E13").value = d
        ws.range("E14").value = e
        ws.range("E15").value = f
        ws.range("E16").value = g
        ws.range("E17").value = h
        ws.range("E18").value = i
        ws.range("E19").value = j
        ws.range("E20").value = k
        ws.range("E21").value = l
        ws.range("B6").value = date
        if tax == "False":
            ws.range("E24").value = 0
        ws.range("B28").value = description
        ws.range("F2").value = form_number
        total_count = ws.range("D25").value
        password = "88516"
        # 使用 Excel VBA 的 Protect 方法
        ws.api.Cells.Locked = True
        ws.api.Protect(Password=password)
        excel_file_path = f"C:/Users/user/Desktop/手開單/產業/excel/{form_number}.xlsx"
        pdf_file_path = f"C:/Users/user/Desktop/手開單/產業/pdf/{form_number}.pdf"
        wb.save(excel_file_path)
        wb.close()
        convert_to_pdf(excel_file_path, pdf_file_path)
        subprocess.run(["start", pdf_file_path], shell=True)
        sc_file = PC_IND.objects.get(pc_ind_id=pc_ind_id)
        sc_file.excel_file, sc_file.pdf_file = excel_file_path, pdf_file_path
        sc_file.save()

        google_sheet = GoogleSheet()
        search_value = form_number
        value_to_update = {"C":contact, "D":a, "E":b, "F":c, "G":d, "H":e, "I":f, "J":g, "K":h, "L":i, "M":j, "N":k, "O":l, "P":total_count, "Q":description, "U":date, "V":department}
        google_sheet.section_manpulate(search_value, value_to_update)
        return redirect("PC_IND_view")
    return render(request, "section_industry.html")


def monthly_settlement(request):
    year = timezone.now().year
    max_id = Max_ID.objects.get().PC_max
    ms_id = IDgenerator(year, max_id, "校內病理月結")
    context = {"MS_ID": ms_id}
    if request.method == "POST":
        pi = request.POST["pi"]
        lab_tel = request.POST["lab-phone"]
        department = request.POST["department"]
        contact = request.POST["contact"]
        contact_tel = request.POST["contact-number"]
        description = request.POST["description"]
        discount = request.POST["discount"]
        申請單編號 = request.POST["apply-number"]
        a = request.POST["a"]
        b = request.POST["b"]
        c = request.POST["c"]
        d = request.POST["d"]
        e = request.POST["e"]
        f = request.POST["f"]
        g = request.POST["g"]
        h = request.POST["h"]
        i = request.POST["i"]
        j = request.POST["j"]
        k = request.POST["k"]
        date = request.POST["date"]
        Pi, created = Principal_Investigator.objects.get_or_create(
            department=department, pi=pi, lab_tel=lab_tel
        )
        contact1, created = Contact.objects.get_or_create(
            name=contact, contact_number=contact_tel, pi=Pi
        )
        new_ms = MS.objects.create(
            pi=Pi,
            discount=discount,
            description=description,
            date=date,
            contact=contact1,
            A=a,
            B=b,
            C=c,
            D=d,
            E=e,
            F=f,
            G=g,
            H=h,
            I=i,
            J=j,
            K=k,
            申請單編號=申請單編號,
        )
        file_path = os.path.join(
            os.path.dirname(__file__), "static", "病理切片校內-月結版本 v1.0.xlsx"
        )
        wb = xw.Book(file_path)
        ws = wb.sheets["Sheet1 "]
        ws.range("B4").value = department
        ws.range("B5").value = pi
        ws.range("E5").value = lab_tel
        ws.range("B6").value = contact
        ws.range("E6").value = contact_tel
        ws.range("E11").value = a
        ws.range("E12").value = b
        ws.range("E13").value = c
        ws.range("E14").value = d
        ws.range("E15").value = e
        ws.range("E16").value = f
        ws.range("E17").value = g
        ws.range("E18").value = h
        ws.range("E19").value = i
        ws.range("E20").value = j
        ws.range("E21").value = k
        ws.range("B7").value = date
        ws.range("D23").value = int(discount) / 100
        ws.range("B27").value = description
        ws.range("F2").value = ms_id
        ws.range("B28").value = 申請單編號
        password = "88516"
        # 使用 Excel VBA 的 Protect 方法
        ws.api.Cells.Locked = True
        ws.api.Protect(Password=password)
        excel_file_path = f"C:/Users/user/Desktop/手開單/校內月結/excel/{ms_id}.xlsx"
        pdf_file_path = f"C:/Users/user/Desktop/手開單/校內月結/pdf/{ms_id}.pdf"
        wb.save(excel_file_path)
        wb.close()
        convert_to_pdf(excel_file_path, pdf_file_path)
        subprocess.run(["start", pdf_file_path], shell=True)
        ms_file = MS.objects.get(pc_id=ms_id)
        ms_file.excel_file, ms_file.pdf_file = excel_file_path, pdf_file_path
        ms_file.save()
        return redirect("monthly_settlement_view")
    return render(request, "month_section_insch_list.html", context)


def QC_view(request):
    QC_cache = cache.get("QC")
    QCs = QC.objects.all().order_by("-date")
    if not QC_cache:  
        cache.set("QC", QCs, 120)
    context = {"QCs": QCs}

    return render(request, "back/health_monitor_list.html", context)



def SC_view(request):
    SC_cache = cache.get("SC")
    SCs = SC.objects.all().order_by("-date")
    if not SC_cache:
        cache.set("SC", SCs, 120)
       
    form_type = SC
    context = {"SCs": SCs, "form_type": form_type}

    return render(request, "back/blood&serun_list.html", context)



def PC_IN_view(request):
    PC_cache = cache.get("PC")
    PCs = PC_INS.objects.all().order_by("-date")
    if not PC_cache:  
        cache.set("PC", PCs, 120)
    context = {"PCs": PCs}
    return render(request, "back/section_insch_list.html", context)



def PC_OUT_view(request):
    PC_cache = cache.get("PC")
    PCs = PC_OUS.objects.all().order_by("-date")
    if not PC_cache: 
        cache.set("PC", PCs, 120)
    context = {"PCs": PCs}
    return render(request, "back/section_outsch_list.html", context)


def PC_IND_view(request):
    PC_cache = cache.get("PC")
    PCs = PC_IND.objects.all().order_by("-date")
    if not PC_cache: 
        cache.set("PC", PCs, 120)
    context = {"PCs": PCs}
    return render(request, "back/section_ind_list.html", context)


def monthly_settlement_view(request):
    """校內病理月結 List"""

    ms = MS.objects.all().order_by("-date")
    context = {"MSs": ms}
    return render(request, "back/ms_list.html", context)


def delete_form(request):
    form_type = request.GET["form_type"]
    form_id = request.GET["id"]
    model_type = eval(form_type)
    message = " "
    try:
        data = delete_action(model_type, form_id)
    except Exception as e:
        print(e)
        message = f"無法刪除檔案，請關閉檔案在嘗試刪除，錯誤訊息: {str(e)}"
        return HttpResponse(message)
    return JsonResponse({"data": data,"message":message})


def update_pay(request):
    """Change the payment status!
    Form_type params:
    Serum and blood :SC
    Health monitor: QC
    Section insch: PC_INS
    Section outsch: PC_OUS
    Section industry: PC_IND
    """
    form_type = request.GET["form_type"]
    form_id = request.GET["id"]
    model_type = eval(form_type)
    data = pay_status_change(model_type, form_id)
    return JsonResponse({"data": data})

