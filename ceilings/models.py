# -*- coding: utf-8 -*-
from django.db import models


class Ceiling(models.Model):
	name = models.CharField(u'О потолках', max_length=255)
	title = models.TextField(null=True)
	
	def __unicode__(self):
		return self.name
		
		
class DetalnoeOpisanie(models.Model):
	name = models.CharField(u'Название', max_length=255, blank=True, null=True)
	short_description = models.CharField(u'Краткое описание', max_length=500, blank=True, null=True)
	description = models.TextField(u'Полное описание', blank=True, null=True)
	image = models.ImageField(blank=True, upload_to='images/', verbose_name='Ссылка картинки')
	ceiling = models.ForeignKey(Ceiling)
	
	def __unicode__(self):
		return self.name
		
