from django.views.generic import TemplateView
from prices.models import PriceTable, SecondPriceTable
from ceilings.models import Ceiling


class PriceView(TemplateView):
    template_name = 'prices/price.html'
    
    def get_context_data(self, **kwargs):
        context = super(PriceView, self).get_context_data(**kwargs)
        context['ceilings'] = Ceiling.objects.all()
        context['price_one'] = PriceTable.objects.all()
        context['fields_two'] = SecondPriceTable.objects.all() 
        return context

