from openpyxl import load_workbook
from django.http import HttpResponse
from .models import *
from win32com import client
def convert_to_pdf(input_path, output_path):
    excel = client.Dispatch("Excel.Application")#利用dispatch連接 microsoft 應用程式  這裡是連接到excel
    doc = excel.Workbooks.Open(input_path)
    doc.SaveAs(output_path, FileFormat=57)  # FileFormat = 57 是 PDF 格式
    doc.Close()
    excel.Quit()