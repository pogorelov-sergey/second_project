from django.contrib import admin
from calculator.models import Calculator


class CalculatorAdmin(admin.ModelAdmin):
    list_display = ['order', 'name']
    
     
admin.site.register(Calculator, CalculatorAdmin)


