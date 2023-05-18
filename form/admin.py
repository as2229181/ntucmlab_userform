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
        'number',
    ]

    def qcid(self, obj):
        return obj.qcid

    def department(self, obj):
        return obj.department

    def pi(self, obj):
        return obj.pi

    def lab_tel(self, obj):
        return obj.lab_tel

    def contact(self, obj):
        return obj.contact

    def contact_tel(self, obj):
        return obj.contact_tel

    def date(self, obj):
        return obj.date

    def number(self, obj):
        return obj.number

    # 設置列表欄位的標題
    qcid.short_description = '單號'
    department.short_description = '系所'
    pi.short_description = '計畫主持人'
    lab_tel.short_description = '實驗室電話'
    contact.short_description = '聯絡人'
    contact_tel.short_description = '聯絡人電話'
    date.short_description = '日期'
    number.short_description = '數量'

class SCAdmin(admin.ModelAdmin):    
    
    list_display=['scid','department','pi','lab_tel','contact','contact_tel','date','serum','bloodcell']
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
    def bloodcell(self, obj):
        return obj.number
    bloodcell.short_description = '血液數量'
class PC_OUSAdmin(admin.ModelAdmin):   
    
    list_display=['pc_out_id','department','pi','lab_tel','contact','contact_tel','date','A','B','C','D','E','F','G','H','I','J','K']
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

    def a(self, obj):
        return obj.number
    a.short_description = '組織包埋(蠟)'
    def b(self, obj):
        return obj.number
    b.short_description = '蠟切片(組織空白片)'
    def c(self, obj):
        return obj.number
    c.short_description = '蠟切片(免疫組織空白片)'
    def d(self, obj):
        return obj.number
    d.short_description = 'H&E染色'
    def e(self, obj):
        return obj.number
    e.short_description = 'H&E以外染色'
    def f(self, obj):
        return obj.number
    f.short_description = '脫鈣'
    def g(self, obj):
        return obj.number
    g.short_description = '冷凍切片'
    def h(self, obj):
        return obj.number
    h.short_description = '冷凍包埋'
    def i(self, obj):
        return obj.number
    i.short_description = '免疫組織染色(不含抗體)'
    def j(self, obj):
        return obj.number
    j.short_description = '病理切片一般判讀'
    def k(self, obj):
        return obj.number
    k.short_description = '病理切片照相'
class PC_INSAdmin(admin.ModelAdmin):
    
    list_display=['pc_ins_id','department','pi','lab_tel','contact','contact_tel','date','A','B','C','D','E','F','G','H','I','J','K']
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

    def a(self, obj):
        return obj.number
    a.short_description = '組織包埋(蠟)'
    def b(self, obj):
        return obj.number
    b.short_description = '蠟切片(組織空白片)'
    def c(self, obj):
        return obj.number
    c.short_description = '蠟切片(免疫組織空白片)'
    def d(self, obj):
        return obj.number
    d.short_description = 'H&E染色'
    def e(self, obj):
        return obj.number
    e.short_description = 'H&E以外染色'
    def f(self, obj):
        return obj.number
    f.short_description = '脫鈣'
    def g(self, obj):
        return obj.number
    g.short_description = '冷凍切片'
    def h(self, obj):
        return obj.number
    h.short_description = '冷凍包埋'
    def i(self, obj):
        return obj.number
    i.short_description = '免疫組織染色(不含抗體)'
    def j(self, obj):
        return obj.number
    j.short_description = '病理切片一般判讀'
    def k(self, obj):
        return obj.number
    k.short_description = '病理切片照相'

class PC_INDAdmin(admin.ModelAdmin):
   
    list_display=['pc_ind_id','department','pi','lab_tel','contact','contact_tel','date','A','B','C','D','E','F','G','H','I','J','K']
    def pc_ind_id(self, obj):
        return obj.pc_ind_id
    pc_ind_id.short_description = '單號'

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

    def a(self, obj):
        return obj.a
    a.short_description = '組織包埋(蠟)'
    def b(self, obj):
        return obj.b
    b.short_description = '蠟切片(組織空白片)'
    def c(self, obj):
        return obj.c
    c.short_description = '蠟切片(免疫組織空白片)'
    def d(self, obj):
        return obj.d
    d.short_description = 'H&E染色'
    def e(self, obj):
        return obj.e
    e.short_description = 'H&E以外染色'
    def f(self, obj):
        return obj.f
    f.short_description = '脫鈣'
    def g(self, obj):
        return obj.g
    g.short_description = '冷凍切片'
    def h(self, obj):
        return obj.h
    h.short_description = '冷凍包埋'
    def i(self, obj):
        return obj.i
    i.short_description = '免疫組織染色(不含抗體)'
    def j(self, obj):
        return obj.j
    j.short_description = '病理切片一般判讀'
    def k(self, obj):
        return obj.k
    k.short_description = '病理切片照相'
admin.site.register(QC, QCAdmin)
admin.site.register(SC, SCAdmin)
admin.site.register(PC_IND, PC_INDAdmin)
admin.site.register(PC_OUS, PC_OUSAdmin)
admin.site.register(PC_INS, PC_INSAdmin)
admin.site.register(Max_ID)