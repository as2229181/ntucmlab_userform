import os

from openpyxl import load_workbook
from django.http import HttpResponse
from .models import *
from win32com import client
from django.template.loader import render_to_string
from django.core.cache import cache


def convert_to_pdf(input_path, output_path):
    excel = client.Dispatch(
        "Excel.Application"
    )  # 利用dispatch連接 microsoft 應用程式  這裡是連接到excel
    doc = excel.Workbooks.Open(input_path)
    doc.SaveAs(output_path, FileFormat=57)  # FileFormat = 57 是 PDF 格式
    doc.Close()
    excel.Quit()


def IDgenerator(year, Max_id, prefix):
    if year == int(Max_id[:4]):
        num = int(Max_id[-4:]) + 1
        ID = f"{year}{prefix}{str(num).zfill(4)}"
    else:
        num = 1
        ID = f"{year}{prefix}{str(num).zfill(4)}"
    return ID


def delete_action(type, id):
    object_data = type.objects.get(id=id)
    excel_file_path = os.path.abspath(object_data.excel_file)
    pdf_file_path = os.path.abspath(object_data.pdf_file)
    print(excel_file_path, pdf_file_path)
    if excel_file_path:
        try:
            os.remove(excel_file_path)
        except:
            pass
    if pdf_file_path:
        try:
            os.remove(pdf_file_path)
        except:
            pass
    object_data.delete()
    cache.delete(f"{type.__name__}:{object_data.id}")
    rest_form = type.objects.all().order_by("-date")
    prefix = str(type.__name__)[:2] + "s"
    prefix_lower = (str(type.__name__)[:2]).lower()
    data = render_to_string(f"back/async/{prefix_lower}list.html", {prefix: rest_form})
    return data


def pay_status_change(type, id):
    object_data = type.objects.get(id=id)
    if object_data.pay == False:
        object_data.pay = True
        object_data.save()
        all_form = type.objects.all().order_by("-date")
        prefix = str(type.__name__)[:2]
        prefix = prefix + "s"
        print(prefix)
        prefix_lower = str(type.__name__).lower()
        prefix_lower = prefix_lower[:2]
        print(prefix_lower)
        data = render_to_string(
            f"back/async/{prefix_lower}list.html", {prefix: all_form}
        )
        return data
    else:
        object_data.pay = False
        object_data.save()
        all_form = type.objects.all().order_by("-date")
        prefix = str(type.__name__)[:2]
        prefix = prefix + "s"
        print(prefix)
        prefix_lower = str(type.__name__).lower()
        prefix_lower = prefix_lower[:2]
        data = render_to_string(
            f"back/async/{prefix_lower}list.html", {prefix: all_form}
        )
        return data
