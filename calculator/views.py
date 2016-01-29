from django.shortcuts import render
from calculator.models import Calculator
from ceilings.models import Ceiling
from calculator.forms import CalculatorForm


def calculator(request):
	context = {}
	context['ceilings'] = Ceiling.objects.all()
	context['contents'] = Calculator.objects.all()
	if request.POST:
		form = CalculatorForm(request.POST)
		context['form'] = form
		if form.is_valid():
			a = form.cleaned_data['a']
			b = form.cleaned_data['b']
			c = form.cleaned_data['c']	
			d = b * b - 4 * a * c
			if d < 0:
				context['d'] = d
			elif d == 0:
				x = (-b + d**(1/2.0)) / 2*a
				context['x1'] = round(x, 1)
				context['d'] = d
			else:
				x1 = (-b + d**(1/2.0)) / 2*a
				x2 = (-b - d**(1/2.0)) / 2*a
				context['x1'] = round(x1, 1)
				context['x2'] = round(x2, 1)
				context['d'] = d			
	else:
		form = CalculatorForm()
		context['form'] = form
	return render(request, 'calculator/calculator.html', context)


    
    
