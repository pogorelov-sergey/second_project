from django.contrib import admin
from prices.models import PriceTable, SecondPriceTable


class PriceTableAdmin(admin.ModelAdmin):
    list_display = ['first_field', 'name']
    
     
admin.site.register(PriceTable, PriceTableAdmin)


class SecondPriceTableAdmin(admin.ModelAdmin):
    list_display = ['first_field', 'name']
    
     
admin.site.register(SecondPriceTable, SecondPriceTableAdmin)
