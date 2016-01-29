from django.contrib import admin
from ceilings.models import Ceiling, DetalnoeOpisanie


class DetalnoeOpisanieInline(admin.TabularInline):
	model = DetalnoeOpisanie
	extra = 0


class CeilingAdmin(admin.ModelAdmin):
	search_fields = ['name']
	list_display = ['name']
	inlines = [DetalnoeOpisanieInline]
    
      
admin.site.register(Ceiling, CeilingAdmin)

