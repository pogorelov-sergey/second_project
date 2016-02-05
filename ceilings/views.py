from ceilings.models import Ceiling, DetalnoeOpisanie
from home.models import Slider
from django.shortcuts import render
#from django.views.generic.detail import DetailView


'''
class CeilingDetailView(DetailView):
	model = Ceiling
	template_name = 'ceilings/detail.html'
	
	def get_context_data(self, **kwargs):
		context = super(CeilingDetailView, self).get_context_data(**kwargs)
		context['ceilings'] = Ceiling.objects.all()
		context['detalnoeOpisanies'] = DetalnoeOpisanie.objects.filter(ceiling__slug =self.object)
		context['sliders'] = Slider.objects.all()
		return context
'''

def detail(request, pk):
	ceilings = Ceiling.objects.all()
	detalnoeOpisanies = DetalnoeOpisanie.objects.filter(ceiling__slug=pk)
	title = Ceiling.objects.get(slug=pk)
	sliders = Slider.objects.all()
	return render(request, 'ceilings/detail.html', {'detalnoeOpisanies': detalnoeOpisanies, 'ceilings': ceilings, 'title': title, 'sliders': sliders})
