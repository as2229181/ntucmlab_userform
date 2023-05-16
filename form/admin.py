from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(QC)
admin.site.register(SC)
admin.site.register(PC_IND)
admin.site.register(PC_OUS)
admin.site.register(PC_INS)
admin.site.register(Max_ID)