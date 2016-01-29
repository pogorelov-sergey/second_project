# -*- coding: utf-8 -*-
from django.db import models


class Calculator(models.Model):
	title = models.CharField(blank=True, max_length=100)
	name = models.CharField(blank=True, max_length=100, verbose_name='Название')
	phone = models.CharField(blank=True, max_length=15, verbose_name='Номер телефона')
	content = models.TextField(blank=True)
	order = models.CharField(max_length=50)
	
	def __unicode__(self):
		return self.name
