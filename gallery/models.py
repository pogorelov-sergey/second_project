# -*- coding: utf-8 -*-
from django.db import models


class Gallery(models.Model):
	name = models.CharField(verbose_name='Название раздела галереи.', max_length=255)
	title = models.TextField()
	image = models.ImageField(blank=True, upload_to='gallery/', help_text='Картинка которая в галерее.', verbose_name='Ссылка картинки')
	slug = models.SlugField(max_length=100, verbose_name=u'URL категории', unique=True, help_text='Введите URL без "/" и пробелов.')
	
	def __unicode__(self):
		return self.name
		
		
class Picture(models.Model):
	image = models.ImageField(blank=True, upload_to='gallery/pictures/', verbose_name='Размер картинки 780x560px')
	gallery = models.ForeignKey(Gallery)
	order = models.PositiveIntegerField(null=True)
	

