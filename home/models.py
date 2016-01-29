# -*- coding: utf-8 -*-
from django.db import models
import datetime


class Home(models.Model):
	title = models.TextField()
	
	def __unicode__(self):
		return self.title
	
		
class Slider(models.Model):
	home = models.ForeignKey(Home)
	image = models.ImageField(blank=True, upload_to='slider/', verbose_name='Картинка для слайдера. Max 5 picture.')
	
	
class Feedback(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    phone = models.CharField(max_length=15, verbose_name='Номер телефона')
    message = models.TextField(blank=True, verbose_name='Сообщение')
    create_date = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.name
