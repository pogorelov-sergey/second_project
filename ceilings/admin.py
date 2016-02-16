from django.contrib import admin
from ceilings.models import Ceiling, DetalnoeOpisanie


class DetalnoeOpisanieInline(admin.StackedInline):
	model = DetalnoeOpisanie
	extra = 0


class CeilingAdmin(admin.ModelAdmin):
	search_fields = ['name']
	list_display = ['name']
	prepopulated_fields = {"slug": ("name",)}
	inlines = [DetalnoeOpisanieInline]
    
      
admin.site.register(Ceiling, CeilingAdmin)

