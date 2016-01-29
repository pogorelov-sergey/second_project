# -*- coding: utf-8 -*-
from django.db import models


class PriceTable(models.Model):
	name = models.CharField(blank=True, verbose_name='Название таблицы', max_length=100)
	first_field = models.CharField(blank=True, verbose_name='Первое поле таблицы', max_length=100)
	second_field = models.CharField(blank=True, verbose_name='Второе поле таблицы', max_length=100)
	third_field = models.CharField(blank=True, verbose_name='Третье поле таблицы', max_length=100)
	fourth_field = models.CharField(blank=True, verbose_name='Четвертое поле таблицы', max_length=100)
	fifth_field = models.CharField(blank=True, verbose_name='Пятое поле таблицы', max_length=100)
	
	
class SecondPriceTable(models.Model):
	name = models.CharField(blank=True, verbose_name='Название таблицы', max_length=100)
	first_field = models.CharField(blank=True, verbose_name='Первое поле таблицы', max_length=100)
	second_field = models.CharField(blank=True, verbose_name='Второе поле таблицы', max_length=100)
	third_field = models.CharField(blank=True, verbose_name='Третье поле таблицы', max_length=100)


