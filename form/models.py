from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils import timezone
# Create your models here.
class Principal_Investigator(models.Model):
    pi = models.CharField(max_length=1000,null=True,blank=True,default=None)
    department = models.CharField(max_length=1000,null=True,blank=True,default=None)
    
    lab_tel = models.CharField(max_length=20,null=True,blank=True,default=None)
    class Meta:
        verbose_name = '實驗室負責人'
        verbose_name_plural = '實驗室負責人'
    
    def __str__(self):
        return self.pi     

class Contact(models.Model):
    pi=models.ForeignKey(Principal_Investigator,on_delete=models.SET_NULL,null=True,blank=True)
    name = models.CharField(max_length=1000,null=True,blank=True,default=None)
    contact_number = models.CharField(max_length=1000,null=True,blank=True,default=None)
    class Meta:
        verbose_name = '聯絡人'
        verbose_name_plural = '聯絡人'

    def __str__(self):
        return self.name       
'''
Health Minitor
'''
class QC(models.Model):
    qcid = models.CharField(unique=True, max_length=11,default=None)
    pi = models.ForeignKey(Principal_Investigator,on_delete=models.SET_NULL,null=True,blank=True,related_name='qc_pi')
    contact = models.ForeignKey(Contact,on_delete=models.SET_NULL,null=True,blank=True,related_name='qc_contact')
    date = models.DateField()
    description= models.CharField(max_length=1000,null=True,blank=True,default=None)
    discount = models.CharField(max_length=6,null=True,blank=True,default='100%')
    mus_number = models.IntegerField(default=0,null=True,blank=True)
    rat_number = models.IntegerField(default=0,null=True,blank=True)
    excel_file = models.CharField(max_length=255, null=True, blank=True)
    pdf_file = models.CharField(max_length=255, null=True, blank=True)
    tax = models.BooleanField(default=False)
    pay = models.BooleanField(default=False)
    class Meta:
        verbose_name = '健康監測手開單'
        verbose_name_plural = '健康監測手開單'

    


'''
serum & blood
'''

class SC(models.Model):
    scid = models.CharField(unique=True, max_length=11,default=None)
    pi = models.ForeignKey(Principal_Investigator,on_delete=models.SET_NULL,null=True,blank=True,related_name='sc_pi')
    contact = models.ForeignKey(Contact,on_delete=models.SET_NULL,null=True,blank=True,related_name='sc_contact')
    date = models.DateField()
    description= models.CharField(max_length=1000,null=True,blank=True,default=None)
    discount = models.CharField(max_length=6,null=True,blank=True,default='100%')
    申請單編號=models.CharField(max_length=1000,null=True,blank=True,default=None)
    serum = models.IntegerField(default=0,null=True,blank=True)
    CBC = models.IntegerField(default=0,null=True,blank=True)
    excel_file = models.CharField(max_length=255, null=True, blank=True)
    pdf_file = models.CharField(max_length=255, null=True, blank=True)
    tax = models.BooleanField(default=False)
    pay = models.BooleanField(default=False)
    class Meta:
        verbose_name = '血液血清手開單'
        verbose_name_plural = '血液血清手開單'
    def save(self, *args, **kwargs):
        if not self.scid:
            # 獲取當前年份
            year = timezone.now().year
            # 獲取當前年份下已有的最大序號
            max_serial_number = Max_ID.objects.filter(SC_max__startswith=str(year)).values_list('SC_max', flat=True).order_by('-SC_max').first()
            #max_serial_number = QC.objects.filter(qcid__startswith=str(year)).values_list('qcid', flat=True).order_by('-qcid').first()
            if max_serial_number:
                # 從最大序号中提取數字部分並加1
                num = int(max_serial_number[6:]) + 1
            else:
                # 如果該年份下没有序號，從001開始
                num = 1
        
            self.scid = f"{year}SC{str(num).zfill(4)}"
            Max_ID.objects.update(SC_max=self.scid)
        super().save(*args, **kwargs)


'''
For inside school
'''


class PC_INS(models.Model):
    pc_ins_id = models.CharField(unique=True, max_length=11,default=None)
    pi = models.ForeignKey(Principal_Investigator,on_delete=models.SET_NULL,null=True,blank=True,related_name='pc_ins_pi')
    contact = models.ForeignKey(Contact,on_delete=models.SET_NULL,null=True,blank=True,related_name='pc_ins_contact')
    date = models.DateField()
    description= models.CharField(max_length=1000,null=True,blank=True,default=None)
    discount = models.CharField(max_length=6,null=True,blank=True,default='100%')
    
    excel_file = models.CharField(max_length=255, null=True, blank=True)
    pdf_file = models.CharField(max_length=255, null=True, blank=True)
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


'''
For outside school
'''

class PC_OUS(models.Model):
    pc_out_id = models.CharField(unique=True, max_length=11,default=None)
    pi = models.ForeignKey(Principal_Investigator,on_delete=models.SET_NULL,null=True,blank=True,related_name='pc_ous_pi')
    contact = models.ForeignKey(Contact,on_delete=models.SET_NULL,null=True,blank=True,related_name='pc_ous_contact')
    date = models.DateField()
    description= models.CharField(max_length=1000,null=True,blank=True,default=None)
    discount = models.CharField(max_length=6,null=True,blank=True,default='100%')
    excel_file = models.CharField(max_length=255, null=True, blank=True)
    pdf_file = models.CharField(max_length=255, null=True, blank=True)
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

'''
For industry
'''

class PC_IND(models.Model):
    pc_ind_id = models.CharField(unique=True, max_length=11,default=None)
    contact = models.ForeignKey(Contact,on_delete=models.SET_NULL,null=True,blank=True,related_name='pc_ind_contact')
    date = models.DateField()
    description= models.CharField(max_length=1000,null=True,blank=True,default=None)
    discount = models.CharField(max_length=6,null=True,blank=True,default='100%')
    excel_file = models.CharField(max_length=255, null=True, blank=True)
    pdf_file = models.CharField(max_length=255, null=True, blank=True)
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


class MS(models.Model):
    pc_id = models.CharField(unique=True, max_length=20,default=None)
    pi = models.ForeignKey(Principal_Investigator,on_delete=models.SET_NULL,null=True,blank=True,related_name='pc_pi')
    contact = models.ForeignKey(Contact,on_delete=models.SET_NULL,null=True,blank=True,related_name='pc_contact')
    date = models.DateField()
    description= models.CharField(max_length=1000,null=True,blank=True,default=None)
    discount = models.CharField(max_length=6,null=True,blank=True,default='100%')
    excel_file = models.CharField(max_length=255, null=True, blank=True)
    pdf_file = models.CharField(max_length=255, null=True, blank=True)
    申請單編號=models.CharField(max_length=1000,null=True,blank=True,default=None)
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
        verbose_name = '校內月結'
        verbose_name_plural = '校內月結'
    def save(self, *args, **kwargs):
        if not self.pc_id:
            # 獲取當前年分
            year = timezone.now().year
            # 獲取當前年份下已有的最大序號
            max_serial_number = Max_ID.objects.filter(PC_max__startswith=str(year)).values_list('PC_max', flat=True).order_by('-PC_max').first()
            #max_serial_number = QC.objects.filter(qcid__startswith=str(year)).values_list('qcid', flat=True).order_by('-qcid').first()
            print(max_serial_number)
            if max_serial_number:
                # 從最大序號中提取數字部分并加1
                num = int(max_serial_number[10:]) + 1
            else:
                # 如果該年份下没有序號，從0001開始
                num = 1
            # 生成新的qcid
            self.pc_id = f"{year}校內病理月結{str(num).zfill(4)}"
            Max_ID.objects.update(PC_max=self.pc_id)
        super().save(*args, **kwargs)
    

class Max_ID(models.Model):
    QC_max = models.CharField(max_length=1000,null=True,blank=True,default=None)
    SC_max = models.CharField(max_length=1000,null=True,blank=True,default=None)
    PC_max = models.CharField(max_length=1000,null=True,blank=True,default=None)



