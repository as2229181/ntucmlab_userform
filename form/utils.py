from openpyxl import load_workbook
from django.http import HttpResponse
from .models import *
def add_to_excel(request):
    wb= load_workbook('userform/form/static/健康監測手開帳單v1.0.xls')
    ws = wb['sheet1']
    form_data = QC.objects.all().values()
