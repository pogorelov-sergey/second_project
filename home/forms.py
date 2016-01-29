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
		
		

