from django.views.generic import TemplateView
from ceilings.models import Ceiling


class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['ceilings'] = Ceiling.objects.all()
        return context
        
        
class ContactView(TemplateView):
    template_name = 'contact.html'
    
    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['ceilings'] = Ceiling.objects.all()
        return context
