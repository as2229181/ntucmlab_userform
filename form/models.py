from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils import timezone
# Create your models here.

'''
Health Minitor
'''
class QC(models.Model):
    qcid = models.CharField(unique=True, max_length=10,default=None)
    department = models.CharField(max_length=1000,null=True,blank=True,default=None)
    pi = models.CharField(max_length=1000,null=True,blank=True,default=None)
    lab_tel = models.CharField(max_length=20,null=True,blank=True,default=None)
    contact = models.CharField(max_length=10,null=True,blank=True,default=None)
    date = models.DateField(auto_now_add=True)
    mice = models.IntegerField(default=0,null=True,blank=True)
    def save(self, *args, **kwargs):
        if not self.qcid:
            # 获取当前年份
            year = timezone.now().year
            # 获取当前年份下已有的最大序号
            max_serial_number = Max_ID.objects.filter(QC_max__startswith=str(year)).values_list('qcid', flat=True).order_by('-qcid').first()
            #max_serial_number = QC.objects.filter(qcid__startswith=str(year)).values_list('qcid', flat=True).order_by('-qcid').first()
            if max_serial_number:
                # 从最大序号中提取数字部分并加1
                num = int(max_serial_number[6:]) + 1
            else:
                # 如果该年份下没有序号，从001开始
                num = 1
            # 生成新的qcid
            self.qcid = f"{year}QC{str(num).zfill(3)}"
            Max_ID.QC_max=self.qcid
        super().save(*args, **kwargs)

    


'''
serum & blood
'''

class SC(models.Model):
    scid = models.CharField(unique=True, max_length=10,default=None)
    department = models.CharField(max_length=1000,null=True,blank=True,default=None)
    pi = models.CharField(max_length=1000,null=True,blank=True,default=None)
    lab_tel = models.CharField(max_length=20,null=True,blank=True,default=None)
    contact = models.CharField(max_length=10,null=True,blank=True,default=None)
    date = models.DateField(auto_now_add=True)
    serum = models.IntegerField(default=0,null=True,blank=True)
    bloodcell = models.IntegerField(default=0,null=True,blank=True)
    def save(self, *args, **kwargs):
        if not self.scid:
            # 获取当前年份
            year = timezone.now().year
            # 获取当前年份下已有的最大序号
            max_serial_number = Max_ID.objects.filter(SC_max__startswith=str(year)).values_list('scid', flat=True).order_by('-scid').first()
            #max_serial_number = QC.objects.filter(qcid__startswith=str(year)).values_list('qcid', flat=True).order_by('-qcid').first()
            if max_serial_number:
                # 从最大序号中提取数字部分并加1
                num = int(max_serial_number[6:]) + 1
            else:
                # 如果该年份下没有序号，从001开始
                num = 1
            # 生成新的qcid
            self.qcid = f"{year}SC{str(num).zfill(3)}"
            Max_ID.SC_max=self.qcid
        super().save(*args, **kwargs)


'''
For inside school
'''


class PC_INS(models.Model):
    pc_insid = models.CharField(unique=True, max_length=10,default=None)
    department = models.CharField(max_length=1000,null=True,blank=True,default=None)
    pi = models.CharField(max_length=1000,null=True,blank=True,default=None)
    lab_tel = models.CharField(max_length=20,null=True,blank=True,default=None)
    contact = models.CharField(max_length=10,null=True,blank=True,default=None)
    date = models.DateField(auto_now_add=True)
    A = models.IntegerField(default=0,null=True,blank=True)
    B = models.IntegerField(default=0,null=True,blank=True)
    C = models.IntegerField(default=0,null=True,blank=True)
    D = models.IntegerField(default=0,null=True,blank=True)
    E = models.IntegerField(default=0,null=True,blank=True)
    F = models.IntegerField(default=0,null=True,blank=True)
    G = models.IntegerField(default=0,null=True,blank=True)
    H = models.IntegerField(default=0,null=True,blank=True)
    I = models.IntegerField(default=0,null=True,blank=True)
    J = models.IntegerField(default=0,null=True,blank=True) 
    K = models.IntegerField(default=0,null=True,blank=True)
    def save(self, *args, **kwargs):
        if not self.pc_insid:
            # 获取当前年份
            year = timezone.now().year
            # 获取当前年份下已有的最大序号
            max_serial_number = Max_ID.objects.filter(PC_max__startswith=str(year)).values_list('pc_insid', flat=True).order_by('-pc_insid').first()
            #max_serial_number = QC.objects.filter(qcid__startswith=str(year)).values_list('qcid', flat=True).order_by('-qcid').first()
            if max_serial_number:
                # 从最大序号中提取数字部分并加1
                num = int(max_serial_number[6:]) + 1
            else:
                # 如果该年份下没有序号，从001开始
                num = 1
            # 生成新的qcid
            self.pc_insid = f"{year}PC{str(num).zfill(3)}"
            Max_ID.PC_max=self.pc_insid
        super().save(*args, **kwargs)

'''
For outside school
'''

class PC_OUS(models.Model):
    pc_outid = models.CharField(unique=True, max_length=10,default=None)
    department = models.CharField(max_length=1000,null=True,blank=True,default=None)
    pi = models.CharField(max_length=1000,null=True,blank=True,default=None)
    lab_tel = models.CharField(max_length=20,null=True,blank=True,default=None)
    contact = models.CharField(max_length=10,null=True,blank=True,default=None)
    date = models.DateField(auto_now_add=True)
    A = models.IntegerField(default=0,null=True,blank=True)
    B = models.IntegerField(default=0,null=True,blank=True)
    C = models.IntegerField(default=0,null=True,blank=True)
    D = models.IntegerField(default=0,null=True,blank=True)
    E = models.IntegerField(default=0,null=True,blank=True)
    F = models.IntegerField(default=0,null=True,blank=True)
    G = models.IntegerField(default=0,null=True,blank=True)
    H = models.IntegerField(default=0,null=True,blank=True)
    I = models.IntegerField(default=0,null=True,blank=True)
    J = models.IntegerField(default=0,null=True,blank=True) 
    K = models.IntegerField(default=0,null=True,blank=True)
    def save(self, *args, **kwargs):
        if not self.pc_outid:
            # 获取当前年份
            year = timezone.now().year
            # 获取当前年份下已有的最大序号
            max_serial_number = Max_ID.objects.filter(PC_max__startswith=str(year)).values_list('pc_outid', flat=True).order_by('-pc_outid').first()
            #max_serial_number = QC.objects.filter(qcid__startswith=str(year)).values_list('qcid', flat=True).order_by('-qcid').first()
            if max_serial_number:
                # 从最大序号中提取数字部分并加1
                num = int(max_serial_number[6:]) + 1
            else:
                # 如果该年份下没有序号，从001开始
                num = 1
            # 生成新的qcid
            self.pc_outid = f"{year}PC{str(num).zfill(3)}"
            Max_ID.PC_max=self.pc_outid
        super().save(*args, **kwargs)
'''
For industry
'''

class PC_IND(models.Model):
    pc_indid = models.CharField(unique=True, max_length=10,default=None)
    department = models.CharField(max_length=1000,null=True,blank=True,default=None)
    pi = models.CharField(max_length=1000,null=True,blank=True,default=None)
    lab_tel = models.CharField(max_length=20,null=True,blank=True,default=None)
    contact = models.CharField(max_length=10,null=True,blank=True,default=None)
    date = models.DateField(auto_now_add=True)
    A = models.IntegerField(default=0,null=True,blank=True)
    B = models.IntegerField(default=0,null=True,blank=True)
    C = models.IntegerField(default=0,null=True,blank=True)
    D = models.IntegerField(default=0,null=True,blank=True)
    E = models.IntegerField(default=0,null=True,blank=True)
    F = models.IntegerField(default=0,null=True,blank=True)
    G = models.IntegerField(default=0,null=True,blank=True)
    H = models.IntegerField(default=0,null=True,blank=True)
    I = models.IntegerField(default=0,null=True,blank=True)
    J = models.IntegerField(default=0,null=True,blank=True) 
    K = models.IntegerField(default=0,null=True,blank=True)
    def save(self, *args, **kwargs):
        if not self.pc_indid:
            # 获取当前年份
            year = timezone.now().year
            # 获取当前年份下已有的最大序号
            max_serial_number = Max_ID.objects.filter(PC_max__startswith=str(year)).values_list('pc_indid', flat=True).order_by('-pc_indid').first()
            #max_serial_number = QC.objects.filter(qcid__startswith=str(year)).values_list('qcid', flat=True).order_by('-qcid').first()
            if max_serial_number:
                # 从最大序号中提取数字部分并加1
                num = int(max_serial_number[6:]) + 1
            else:
                # 如果该年份下没有序号，从001开始
                num = 1
            # 生成新的qcid
            self.pc_indid = f"{year}PC{str(num).zfill(3)}"
            Max_ID.PC_max=self.pc_indid
        super().save(*args, **kwargs)


class Max_ID(models.Model):
    QC_max = models.CharField(max_length=1000,null=True,blank=True,default=None)
    SC_max = models.CharField(max_length=1000,null=True,blank=True,default=None)
    PC_max = models.CharField(max_length=1000,null=True,blank=True,default=None)
    