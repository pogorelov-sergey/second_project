# -*- coding: utf-8 -*- 
from django import forms

MATERIAL_CHOICES = (
	('0', 'Выберите Материал'),
    ('Бельгия', (
            ('1', 'Глянцевая (54 цвета)'),
            ('2', 'Матовая (120 цветов)'),
            ('3', 'Сатин (10 цветов)'),
        )
    ),
    ('Франция', (
            ('4', 'Глянцевая (32 цвета)'),
            ('5', 'Фактурная (12 цветов)'),
        )
    ),
    ('Германия', (
            ('6', 'Глянцевая (60 цветов)'),
            ('7', 'Матовая (32 цвета)'),
        )
    ),
    ('Дизайнерские решения', (
            ('8', 'Звездное небо (цена договорная)'),
            ('9', 'Фотопечать (540 грн. за м.кв.)'),
            ('10', 'Двух уровневые (по договоренности)'),
        )
    ),
)

class CalculatorForm(forms.Form):
	material = forms.ChoiceField(label="Материал", choices=MATERIAL_CHOICES)
	area = forms.IntegerField(required=False, label="Укажите Вашу площадь")
	angles = forms.IntegerField(required=False, label="Введите количество углов (всех)")
	lamp = forms.IntegerField(required=False, label="Количество точечных светильников")
	chandelier = forms.IntegerField(required=False, label="Установка люстры")
	trumpet = forms.IntegerField(required=False, label="Обход трубы")
	baguette = forms.IntegerField(required=False, label="Багет (вставка)")
	
	def clean_area(self):
		area = self.cleaned_data['area']
		c = str(area)
		if c[0] == '-':
			raise forms.ValidationError("Введите пожалуйста положительное число! ")
		return area
		
	def clean_angles(self):
		angles = self.cleaned_data['angles']
		c = str(angles)
		if c[0] == '-':
			raise forms.ValidationError("Введите пожалуйста положительное число! ")
		return angles
		
	def clean_lamp(self):
		lamp = self.cleaned_data['lamp']
		c = str(lamp)
		if c[0] == '-':
			raise forms.ValidationError("Введите пожалуйста положительное число! ")
		return lamp
		
	def clean_chandelier(self):
		chandelier = self.cleaned_data['chandelier']
		c = str(chandelier)
		if c[0] == '-':
			raise forms.ValidationError("Введите пожалуйста положительное число! ")
		return chandelier
		
	def clean_trumpet(self):
		trumpet = self.cleaned_data['trumpet']
		c = str(trumpet)
		if c[0] == '-':
			raise forms.ValidationError("Введите пожалуйста положительное число! ")
		return trumpet
		
	def clean_baguette(self):
		baguette = self.cleaned_data['baguette']
		c = str(baguette)
		if c[0] == '-':
			raise forms.ValidationError("Введите пожалуйста положительное число! ")
		return baguette	

	

