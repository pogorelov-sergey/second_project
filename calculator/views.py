# -*- coding: utf-8 -*-
from django.shortcuts import render
from calculator.models import Calculator
from ceilings.models import Ceiling
from calculator.forms import CalculatorForm


def calculator(request):
	context = {}
	context['ceilings'] = Ceiling.objects.all()
	context['contents'] = Calculator.objects.all()
	if request.method == 'POST':
		form = CalculatorForm(request.POST)
		context['form'] = form
		if form.is_valid():
			material = form.cleaned_data['material']
			area = form.cleaned_data['area']
			angles = form.cleaned_data['angles']
			lamp = form.cleaned_data['lamp']
			chandelier = form.cleaned_data['chandelier']
			trumpet = form.cleaned_data['trumpet']
			baguette = form.cleaned_data['baguette']
			print material, area
			if int(material) == 1 and area < 5:
				context['result'] = 350
			elif int(material) == 1 and area >= 5 and area < 10:
				context['result'] = 250
			elif int(material) == 1 and area >= 10:
				context['result'] = 210			
			if int(material) == 2 and area < 5:
				context['result'] = 350
			elif int(material) == 2 and area >= 5 and area < 10:
				context['result'] = 240
			elif int(material) == 2 and area >= 10:
				context['result'] = 190	
			if int(material) == 3 and area < 5:
				context['result'] = 380
			elif int(material) == 3 and area >= 5 and area < 10:
				context['result'] = 290
			elif int(material) == 3 and area >= 10:
				context['result'] = 250
			if int(material) == 4 and area < 5:
				context['result'] = 390
			elif int(material) == 4 and area >= 5 and area < 10:
				context['result'] = 300
			elif int(material) == 4 and area >= 10:
				context['result'] = 260
			if int(material) == 5 and area < 5:
				context['result'] = 400
			elif int(material) == 5 and area >= 5 and area < 10:
				context['result'] = 320
			elif int(material) == 5 and area >= 10:
				context['result'] = 280
			if int(material) == 6 and area < 5:
				context['result'] = 350
			elif int(material) == 6 and area >= 5 and area < 10:
				context['result'] = 260
			elif int(material) == 6 and area >= 10:
				context['result'] = 220
			if int(material) == 7 and area < 5:
				context['result'] = 350
			elif int(material) == 7 and area >= 5 and area < 10:
				context['result'] = 240
			elif int(material) == 7 and area >= 10:
				context['result'] = 200
			if int(material) == 9:
				context['result'] = 540
			if int(material) == 8:
				context['result'] = 0
			if int(material) == 0:
				context['result'] = 0
			if int(material) == 10:
				context['result'] = 0			
			if area != 0 and area != None:
				context['result'] = context['result'] * area
			if angles != 0 and angles != None:
				context['result'] = context['result'] + angles * 40
			if lamp != 0 and lamp != None:
				context['result'] = context['result'] + lamp * 80
			if chandelier != 0 and chandelier != None:
				context['result'] = context['result'] + chandelier * 80
			if trumpet != 0 and trumpet != None:
				context['result'] = context['result'] + trumpet * 80
			if baguette != 0 and baguette != None:
				context['result'] = context['result'] + baguette * 35		
	else:
		form = CalculatorForm()
		context['form'] = form
	return render(request, 'calculator/calculator.html', context)


    
    
