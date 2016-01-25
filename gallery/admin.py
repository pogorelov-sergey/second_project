from django.contrib import admin
from gallery.models import Gallery, Picture


class PictureInline(admin.TabularInline):
	model = Picture
	extra = 0


class GalleryAdmin(admin.ModelAdmin):
	search_fields = ['name']
	list_display = ['name']
	inlines = [PictureInline]
    
    
      
admin.site.register(Gallery, GalleryAdmin)
