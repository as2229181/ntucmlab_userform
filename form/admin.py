from django.contrib import admin

# Register your models here.
from .models import *
class QCAdmin(admin.ModelAdmin):
    search_fields = ('name', 'category__name',)
    list_display = [
        'qcid',
        'department',
        'pi',
        'lab_tel',
        'contact',
        'contact_tel',
        'date',
        'mus_number',
        'rat_number'
    ] 

class SCAdmin(admin.ModelAdmin):    
    
    list_display=['scid','department','pi','lab_tel','contact','contact_tel','date','serum','CBC','申請單編號']
    def scid(self, obj):
        return obj.scid
    scid.short_description = '單號'

    def department(self, obj):
        return obj.department
    department.short_description = '系所'

    def pi(self, obj):
        return obj.pi
    pi.short_description = '計畫主持人'

    def lab_tel(self, obj):
        return obj.lab_tel
    lab_tel.short_description = '實驗室電話'

    def contact(self, obj):
        return obj.contact
    contact.short_description = '聯絡人'

    def contact_tel(self, obj):
        return obj.contact_tel
    contact_tel.short_description = '聯絡人電話'

    def date(self, obj):
        return obj.date
    date.short_description = '日期'

    def serum(self, obj):
        return obj.number
    serum.short_description = '血清數量'
    
class PC_OUSAdmin(admin.ModelAdmin):   
    
    
    def pc_out_id(self, obj):
        return obj.pc_out_id
    pc_out_id.short_description = '單號'

    def department(self, obj):
        return obj.department
    department.short_description = '系所'

    def pi(self, obj):
        return obj.pi
    pi.short_description = '計畫主持人'

    def lab_tel(self, obj):
        return obj.lab_tel
    lab_tel.short_description = '實驗室電話'

    def contact(self, obj):
        return obj.contact
    contact.short_description = '聯絡人'

    def contact_tel(self, obj):
        return obj.contact_tel
    contact_tel.short_description = '聯絡人電話'

    def date(self, obj):
        return obj.date
    date.short_description = '日期'

    def A_display(self, obj):
        return obj.A
    A_display.short_description = '1'
    def B_display(self, obj):
        return obj.B
    B_display.short_description = '2'
    def C_display(self, obj):
        return obj.C
    C_display.short_description = '3'
    def D_display(self, obj):
        return obj.D
    D_display.short_description = '4'
    def E_display(self, obj):
        return obj.E
    E_display.short_description = '5'
    def F_display(self, obj):
        return obj.F
    F_display.short_description = '6'
    def G_display(self, obj):
        return obj.G
    G_display.short_description = '7'
    def H_display(self, obj):
        return obj.H
    H_display.short_description = '8'
    def I_display(self, obj):
        return obj.I
    I_display.short_description = '9'
    def J_display(self, obj):
        return obj.J
    J_display.short_description = '10'
    def K_display(self, obj):
        return obj.K
    K_display.short_description = '11'
    list_display=['pc_out_id','department','pi','lab_tel','contact','contact_tel','date','A_display','B_display','C_display','D_display','E_display','F_display',
                  'G_display','H_display','I_display','J_display','K_display','申請單編號']
class PC_INSAdmin(admin.ModelAdmin):
    
    list_display=['pc_ins_id','department','pi','lab_tel','contact','contact_tel','date','A_display','B_display','C_display','D_display','E_display','F_display',
                  'G_display','H_display','I_display','J_display','K_display','申請單編號']
    def pc_ins_id(self, obj):
        return obj.pc_ins_id
    pc_ins_id.short_description = '單號'

    def department(self, obj):
        return obj.department
    department.short_description = '系所'

    def pi(self, obj):
        return obj.pi
    pi.short_description = '計畫主持人'

    def lab_tel(self, obj):
        return obj.lab_tel
    lab_tel.short_description = '實驗室電話'

    def contact(self, obj):
        return obj.contact
    contact.short_description = '聯絡人'

    def contact_tel(self, obj):
        return obj.contact_tel
    contact_tel.short_description = '聯絡人電話'

    def date(self, obj):
        return obj.date
    date.short_description = '日期'

    def A_display(self, obj):
        return obj.A
    A_display.short_description = '1'
    def B_display(self, obj):
        return obj.B
    B_display.short_description = '2'
    def C_display(self, obj):
        return obj.C
    C_display.short_description = '3'
    def D_display(self, obj):
        return obj.D
    D_display.short_description = '4'
    def E_display(self, obj):
        return obj.E
    E_display.short_description = '5'
    def F_display(self, obj):
        return obj.F
    F_display.short_description = '6'
    def G_display(self, obj):
        return obj.G
    G_display.short_description = '7'
    def H_display(self, obj):
        return obj.H
    H_display.short_description = '8'
    def I_display(self, obj):
        return obj.I
    I_display.short_description = '9'
    def J_display(self, obj):
        return obj.J
    J_display.short_description = '10'
    def K_display(self, obj):
        return obj.K
    K_display.short_description = '11'

class PC_INDAdmin(admin.ModelAdmin):
   
    list_display=['pc_ind_id','department','contact','contact_tel','date','A_display','B_display','C_display','D_display','E_display','F_display',
                  'G_display','H_display','I_display','J_display','K_display','申請單編號']
    def pc_ind_id(self, obj):
        return obj.pc_ind_id
    pc_ind_id.short_description = '單號'

    def department(self, obj):
        return obj.department
    department.short_description = '系所'


    def contact(self, obj):
        return obj.contact
    contact.short_description = '聯絡人'

    def contact_tel(self, obj):
        return obj.contact_tel
    contact_tel.short_description = '聯絡人電話'

    def date(self, obj):
        return obj.date
    date.short_description = '日期'

    def A_display(self, obj):
        return obj.A
    A_display.short_description = '1'
    def B_display(self, obj):
        return obj.B
    B_display.short_description = '2'
    def C_display(self, obj):
        return obj.C
    C_display.short_description = '3'
    def D_display(self, obj):
        return obj.D
    D_display.short_description = '4'
    def E_display(self, obj):
        return obj.E
    E_display.short_description = '5'
    def F_display(self, obj):
        return obj.F
    F_display.short_description = '6'
    def G_display(self, obj):
        return obj.G
    G_display.short_description = '7'
    def H_display(self, obj):
        return obj.H
    H_display.short_description = '8'
    def I_display(self, obj):
        return obj.I
    I_display.short_description = '9'
    def J_display(self, obj):
        return obj.J
    J_display.short_description = '10'
    def K_display(self, obj):
        return obj.K
    K_display.short_description = '11'



admin.site.register(QC, QCAdmin)
admin.site.register(SC, SCAdmin)
admin.site.register(PC_IND, PC_INDAdmin)
admin.site.register(PC_OUS, PC_OUSAdmin)
admin.site.register(PC_INS, PC_INSAdmin)
admin.site.register(Max_ID)