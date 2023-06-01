from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils import timezone
# Create your models here.

'''
Health Minitor
'''
class QC(models.Model):
    qcid = models.CharField(unique=True, max_length=11,default=None)
    department = models.CharField(max_length=1000,null=True,blank=True,default=None)
    pi = models.CharField(max_length=1000,null=True,blank=True,default=None)
    lab_tel = models.CharField(max_length=20,null=True,blank=True,default=None)
    contact = models.CharField(max_length=10,null=True,blank=True,default=None)
    contact_tel = models.CharField(max_length=10,null=True,blank=True,default=None)
    date = models.DateField()
    description= models.CharField(max_length=1000,null=True,blank=True,default=None)
    
    mus_number = models.IntegerField(default=0,null=True,blank=True)
    rat_number = models.IntegerField(default=0,null=True,blank=True)
    file = models.CharField(max_length=255, null=True, blank=True)
    pay = models.BooleanField(default=False)
    class Meta:
        verbose_name = '健康監測手開單'
        verbose_name_plural = '健康監測手開單'
    
    def save(self, *args, **kwargs):
        if not self.qcid:
            # 获取当前年份
            year = timezone.now().year
            # 获取当前年份下已有的最大序号
            max_serial_number = Max_ID.objects.filter(QC_max__startswith=str(year)).values_list('QC_max', flat=True).order_by('-QC_max').first()
            #max_serial_number = QC.objects.filter(qcid__startswith=str(year)).values_list('qcid', flat=True).order_by('-qcid').first()
            if max_serial_number:
                # 从最大序号中提取数字部分并加1
                num = int(max_serial_number[6:]) + 1
            else:
                # 如果该年份下没有序号，从001开始
                num = 1
            # 生成新的qcid
            self.qcid = f"{year}QC{str(num).zfill(4)}"
            Max_ID.objects.update(QC_max=self.qcid)
        super().save(*args, **kwargs)

    


'''
serum & blood
'''

class SC(models.Model):
    scid = models.CharField(unique=True, max_length=11,default=None)
    department = models.CharField(max_length=1000,null=True,blank=True,default=None)
    pi = models.CharField(max_length=1000,null=True,blank=True,default=None)
    lab_tel = models.CharField(max_length=20,null=True,blank=True,default=None)
    contact = models.CharField(max_length=10,null=True,blank=True,default=None)
    contact_tel = models.CharField(max_length=10,null=True,blank=True,default=None)
    date = models.DateField()
    description= models.CharField(max_length=1000,null=True,blank=True,default=None)
    申請單編號=models.CharField(max_length=1000,null=True,blank=True,default=None)
    serum = models.IntegerField(default=0,null=True,blank=True)
    CBC = models.IntegerField(default=0,null=True,blank=True)
    file = models.CharField(max_length=255, null=True, blank=True)
    pay = models.BooleanField(default=False)
    class Meta:
        verbose_name = '血液血清手開單'
        verbose_name_plural = '血液血清手開單'
    def save(self, *args, **kwargs):
        if not self.scid:
            # 获取当前年份
            year = timezone.now().year
            # 获取当前年份下已有的最大序号
            max_serial_number = Max_ID.objects.filter(SC_max__startswith=str(year)).values_list('SC_max', flat=True).order_by('-SC_max').first()
            #max_serial_number = QC.objects.filter(qcid__startswith=str(year)).values_list('qcid', flat=True).order_by('-qcid').first()
            if max_serial_number:
                # 从最大序号中提取数字部分并加1
                num = int(max_serial_number[6:]) + 1
            else:
                # 如果该年份下没有序号，从001开始
                num = 1
        
            self.scid = f"{year}SC{str(num).zfill(4)}"
            Max_ID.objects.update(SC_max=self.scid)
        super().save(*args, **kwargs)


'''
For inside school
'''


class PC_INS(models.Model):
    pc_ins_id = models.CharField(unique=True, max_length=11,default=None)
    department = models.CharField(max_length=1000,null=True,blank=True,default=None)
    pi = models.CharField(max_length=1000,null=True,blank=True,default=None)
    lab_tel = models.CharField(max_length=20,null=True,blank=True,default=None)
    contact = models.CharField(max_length=10,null=True,blank=True,default=None)
    contact_tel = models.CharField(max_length=10,null=True,blank=True,default=None)
    date = models.DateField()
    description= models.CharField(max_length=1000,null=True,blank=True,default=None)
    申請單編號=models.CharField(max_length=1000,null=True,blank=True,default=None)
    file = models.CharField(max_length=255, null=True, blank=True)
    pay = models.BooleanField(default=False)
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
    class Meta:
        verbose_name = '組織切片校內手開單'
        verbose_name_plural = '組織切片校內手開單'
    def save(self, *args, **kwargs):
        if not self.pc_ins_id:
            # 获取当前年份
            year = timezone.now().year
            # 获取当前年份下已有的最大序号
            max_serial_number = Max_ID.objects.filter(PC_max__startswith=str(year)).values_list('PC_max', flat=True).order_by('-PC_max').first()
            #max_serial_number = QC.objects.filter(qcid__startswith=str(year)).values_list('qcid', flat=True).order_by('-qcid').first()
            if max_serial_number:
                # 从最大序号中提取数字部分并加1
                num = int(max_serial_number[6:]) + 1
            else:
                # 如果该年份下没有序号，从001开始
                num = 1
            # 生成新的qcid
            self.pc_ins_id = f"{year}PC{str(num).zfill(4)}"
            Max_ID.objects.update(PC_max=self.pc_ins_id)
        super().save(*args, **kwargs)

'''
For outside school
'''

class PC_OUS(models.Model):
    pc_out_id = models.CharField(unique=True, max_length=11,default=None)
    department = models.CharField(max_length=1000,null=True,blank=True,default=None)
    pi = models.CharField(max_length=1000,null=True,blank=True,default=None)
    lab_tel = models.CharField(max_length=20,null=True,blank=True,default=None)
    contact = models.CharField(max_length=10,null=True,blank=True,default=None)
    contact_tel = models.CharField(max_length=10,null=True,blank=True,default=None)
    date = models.DateField()
    description= models.CharField(max_length=1000,null=True,blank=True,default=None)
    申請單編號=models.CharField(max_length=1000,null=True,blank=True,default=None)
    file = models.CharField(max_length=255, null=True, blank=True)
    pay = models.BooleanField(default=False)
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
    class Meta:
        verbose_name = '組織切片校外手開單'
        verbose_name_plural = '組織切片校外手開單'
    def save(self, *args, **kwargs):
        if not self.pc_out_id:
            # 获取当前年份
            year = timezone.now().year
            # 获取当前年份下已有的最大序号
            max_serial_number = Max_ID.objects.filter(PC_max__startswith=str(year)).values_list('PC_max', flat=True).order_by('-PC_max').first()
            #max_serial_number = QC.objects.filter(qcid__startswith=str(year)).values_list('qcid', flat=True).order_by('-qcid').first()
            if max_serial_number:
                # 从最大序号中提取数字部分并加1
                num = int(max_serial_number[6:]) + 1
            else:
                # 如果该年份下没有序号，从001开始
                num = 1
            # 生成新的qcid
            self.pc_out_id = f"{year}PC{str(num).zfill(4)}"
            Max_ID.objects.update(PC_max=self.pc_out_id)
        super().save(*args, **kwargs)
'''
For industry
'''

class PC_IND(models.Model):
    pc_ind_id = models.CharField(unique=True, max_length=11,default=None)
    department = models.CharField(max_length=1000,null=True,blank=True,default=None)
    contact = models.CharField(max_length=10,null=True,blank=True,default=None)
    contact_tel = models.CharField(max_length=10,null=True,blank=True,default=None)
    date = models.DateField()
    description= models.CharField(max_length=1000,null=True,blank=True,default=None)
    申請單編號=models.CharField(max_length=1000,null=True,blank=True,default=None)
    file = models.CharField(max_length=255, null=True, blank=True)
    pay = models.BooleanField(default=False)
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
    class Meta:
        verbose_name = '組織切片產業價手開單'
        verbose_name_plural = '組織切片產業價手開單'
    def save(self, *args, **kwargs):
        if not self.pc_ind_id:
            # 获取当前年份
            year = timezone.now().year
            # 获取当前年份下已有的最大序号
            max_serial_number = Max_ID.objects.filter(PC_max__startswith=str(year)).values_list('PC_max', flat=True).order_by('-PC_max').first()
            #max_serial_number = QC.objects.filter(qcid__startswith=str(year)).values_list('qcid', flat=True).order_by('-qcid').first()
            if max_serial_number:
                # 从最大序号中提取数字部分并加1
                num = int(max_serial_number[6:]) + 1
            else:
                # 如果该年份下没有序号，从001开始
                num = 1
            # 生成新的qcid
            self.pc_ind_id = f"{year}PC{str(num).zfill(4)}"
            Max_ID.objects.update(PC_max=self.pc_ind_id)
        super().save(*args, **kwargs)


class Max_ID(models.Model):
    QC_max = models.CharField(max_length=1000,null=True,blank=True,default=None)
    SC_max = models.CharField(max_length=1000,null=True,blank=True,default=None)
    PC_max = models.CharField(max_length=1000,null=True,blank=True,default=None)
    