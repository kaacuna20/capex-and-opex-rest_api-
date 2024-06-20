from django.contrib import admin
from .models import CapexContractor, OpexContractor, CapexTransaction, OpexTransaction, CapexRevenue, OpexRevenue

# Register your models here.


class CapexContractorAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

class OpexContractorAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

admin.site.register(CapexContractor, CapexContractorAdmin)
admin.site.register(OpexContractor, OpexContractorAdmin)
admin.site.register(CapexTransaction)
admin.site.register(OpexTransaction)
admin.site.register(CapexRevenue)
admin.site.register(OpexRevenue)