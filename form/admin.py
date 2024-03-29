from django.contrib import admin

# Register your models here.
from .models import *

class Pc_ins(admin.TabularInline):
    model = PC_INS

class PC_out(admin.TabularInline):
    model = PC_OUS   

class PC_ind(admin.TabularInline):
    model = PC_IND 

class PcidAdmin(admin.ModelAdmin):
    inlines=[Pc_ins,PC_out,PC_ind]
    list_display = ["pcid_display"]
    
    def pcid_display(self, obj):
        return obj.pcid
    pcid_display.short_description = '組織切片編號'
class ContactAdmin(admin.ModelAdmin):

    list_display = [        
        'pi',
        'name',
        'contact_number',
    ] 
    def A_display(self, obj):
        return obj.pi.name

class Principal_InvestigatorAdmin(admin.ModelAdmin):
    list_display = [
        'pi',
        'department',
       
        'lab_tel',
    ] 

class QCAdmin(admin.ModelAdmin):
    search_fields = ('name', 'category__name',)
    list_display = [
        'qcid',
        'pi',
        'contact',
        'date',
        'mus_number',
        'rat_number',
        'tax',
        'pay'

    ] 

class SCAdmin(admin.ModelAdmin):    
    
    list_display=['scid','pi','contact','date','serum','CBC','申請單編號']
    
    
class PC_OUSAdmin(admin.ModelAdmin):   
    
    def pc_out_id_display(self, obj):
        return obj.pc_out_id.pcid
    pc_out_id_display.short_description = '編號'
    
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
    list_display=['pc_out_id_display','pi','contact','date','A_display','B_display','C_display','D_display','E_display','F_display',
                  'G_display','H_display','I_display','J_display','K_display']
class PC_INSAdmin(admin.ModelAdmin):
    
    list_display=['pc_ins_id_display','pi','contact','date','A_display','B_display','C_display','D_display','E_display','F_display',
                  'G_display','H_display','I_display','J_display','K_display']
    

    def pc_ins_id_display(self, obj):
        return obj.pc_ins_id.pcid
    pc_ins_id_display.short_description = '編號'
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

class  PC_INDAdmin(admin.ModelAdmin):
    
    list_display=['pc_ind_id_display','contact','date','A_display','B_display','C_display','D_display','E_display','F_display',
                  'G_display','H_display','I_display','J_display','K_display']
    
    def pc_ind_id_display(self, obj):
        return obj.pc_ind_id.pcid
    pc_ind_id_display.short_description = '編號'
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

class MSAdmin(admin.ModelAdmin):
    list_display=['pc_id','pi','contact','date','A_display','B_display','C_display','D_display','E_display','F_display',
                  'G_display','H_display','I_display','J_display','K_display','申請單編號']
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

admin.site.register(Principal_Investigator,Principal_InvestigatorAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(QC, QCAdmin)
admin.site.register(SC, SCAdmin)
admin.site.register(PC_IND, PC_INDAdmin)
admin.site.register(PC_OUS, PC_OUSAdmin)
admin.site.register(PC_INS, PC_INSAdmin)
admin.site.register(Max_ID)
admin.site.register(MS, MSAdmin)
admin.site.register(Pcid, PcidAdmin)