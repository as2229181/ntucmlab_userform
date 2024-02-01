import os
import shutil
import random
from .models import *
from win32com import client
from django.template.loader import render_to_string
from django.core.cache import cache
from django.core.exceptions import PermissionDenied
from .google_sheet import GoogleSheet
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


def move_file(src, dst):
    """Move a file from src to dst and overwrite if file already exists."""
    if not os.path.exists(src):
        print(f"Source file does not exist: {src}")
        return False
    if os.path.exists(dst):
        print(f"Destination file already exists, overwriting: {dst}")
        os.remove(dst)
    try:
        shutil.move(src, dst)
        print(f"File moved successfully from {src} to {dst}")
        return True
    except Exception as e:
        print(f"Failed to move file: {e}")
        return False

def delete_action(model_class, id):
    object_data = model_class.objects.get(id=id)
    dest_folder = 'C://Users//user//Desktop//手開單//刪除'
    files_moved = []
    # 移動 Excel 檔案
    excel_file_path = object_data.excel_file if object_data.excel_file else None
    pdf_file_path = object_data.pdf_file if object_data.pdf_file else None


    if excel_file_path and move_file(excel_file_path, os.path.join(dest_folder, os.path.basename(excel_file_path))):
        files_moved.append('excel')
    if pdf_file_path and move_file(pdf_file_path, os.path.join(dest_folder, os.path.basename(pdf_file_path))):
        files_moved.append('pdf')
    # 檢查兩個文件是否都已成功移動
    if len(files_moved) == 2:
        if excel_file_path:
            try:
                os.remove(excel_file_path)
            except OSError as e:
                print(f"無法刪除 Excel 文件：{e}")
        if pdf_file_path:
            try:
                os.remove(pdf_file_path)
            except OSError as e:
                print(f"無法刪除 PDF 文件：{e}")
    else:
        # 如果任何文件移動失敗，則將已移動的文件移回原位
        for file_type in files_moved:
            if file_type == 'excel':
                shutil.move(os.path.join(dest_folder, os.path.basename(excel_file_path)), excel_file_path)
            if file_type == 'pdf':
                shutil.move(os.path.join(dest_folder, os.path.basename(pdf_file_path)), pdf_file_path)
        raise PermissionDenied("無法刪除文件，請確保文件未被打開並且您有足夠的權限。")
    object_data.delete()
    cache.delete(f"{model_class.__name__}:{object_data.id}")
    rest_form = model_class.objects.all().order_by("-date")
    prefix = str(model_class.__name__)[:2] + "s"
    prefix_lower = (str(model_class.__name__)[:2]).lower()
    data = render_to_string(f"back/async/{prefix_lower}list.html", {prefix: rest_form, "pc_type": model_class})
    return data       

def pay_status_change(type, id):
    object_data = type.objects.get(id=id)
    google_sheet = GoogleSheet()
    if object_data.pay == False:
        object_data.pay = True
        object_data.save()
        all_form = type.objects.all().order_by("-date")
        prefix = str(type.__name__)[:2]
        id_number = object_data.__str__()
        google_sheet.sheet_payment_change(id_number, prefix)
        prefix = prefix + "s"
        prefix_lower = str(type.__name__).lower()
        prefix_lower = prefix_lower[:2]
        data = render_to_string(
            f"back/async/{prefix_lower}list.html", {prefix: all_form}
        )
        return data
    else:
        object_data.pay = False
        object_data.save()
        all_form = type.objects.all().order_by("-date")
        prefix = str(type.__name__)[:2]
        id_number = object_data.__str__()
        google_sheet.sheet_payment_change(id_number, prefix)
        prefix = prefix + "s"
        prefix_lower = str(type.__name__).lower()
        prefix_lower = prefix_lower[:2]
        data = render_to_string(
            f"back/async/{prefix_lower}list.html", {prefix: all_form}
        )
        return data

