# -*- coding: utf-8 -*-
from django import forms
from home.models import Feedback


class FeedbackForm(forms.ModelForm):
	class Meta:
		model = Feedback
		
	def clean_phone(self):
		phone = self.cleaned_data['phone']
		if phone.isalpha():
			raise forms.ValidationError("Введите пожалуйста правильный номер")
		elif len(phone) < 6:
			raise forms.ValidationError("Введите пожалуйста правильный номер")
		return phone
		
	def clean_name(self):
		name = self.cleaned_data['name']
		if name.isdigit():
			raise forms.ValidationError("Введите пожалуйста ваше имя")
		elif len(name) < 2:
			raise forms.ValidationError("Введите пожалуйста ваше имя")
		return name
		
		

