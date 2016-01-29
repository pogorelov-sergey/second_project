from django.contrib import admin
from home.models import Home, Slider, Feedback


class SliderInline(admin.TabularInline):
	model = Slider
	extra = 0


class HomeAdmin(admin.ModelAdmin):
	list_display = ['title']
	inlines = [SliderInline]
    
    
      
admin.site.register(Home, HomeAdmin)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'create_date']
    
     
admin.site.register(Feedback, FeedbackAdmin)
