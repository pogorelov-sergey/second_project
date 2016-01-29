# -*- coding: utf-8 -*- 
from django.views.generic import TemplateView
from ceilings.models import Ceiling
from home.models import Home, Slider
from home.forms import FeedbackForm


class IndexView(TemplateView):
	template_name = 'index.html'
	
	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context['ceilings'] = Ceiling.objects.all()
		context['sliders'] = Slider.objects.all()
		context['home'] = Home.objects.all()
		return context
        
        
class ContactView(TemplateView):
    template_name = 'contact.html'
    
    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['ceilings'] = Ceiling.objects.all()
        return context
