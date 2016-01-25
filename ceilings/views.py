from ceilings.models import Ceiling, DetalnoeOpisanie
from django.views.generic.detail import DetailView


class CeilingDetailView(DetailView):
	model = Ceiling
	template_name = 'ceilings/detail.html'
	
	def get_context_data(self, **kwargs):
		context = super(CeilingDetailView, self).get_context_data(**kwargs)
		context['ceilings'] = Ceiling.objects.all()
		context['detalnoeOpisanies'] = DetalnoeOpisanie.objects.filter(ceiling = self.object)
		return context
