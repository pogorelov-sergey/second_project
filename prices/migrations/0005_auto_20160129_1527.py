# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0004_fieldsprice'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriceTable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x82\xd0\xb0\xd0\xb1\xd0\xbb\xd0\xb8\xd1\x86\xd1\x8b', blank=True)),
                ('first_field', models.CharField(max_length=100, verbose_name=b'\xd0\x9f\xd0\xb5\xd1\x80\xd0\xb2\xd0\xbe\xd0\xb5 \xd0\xbf\xd0\xbe\xd0\xbb\xd0\xb5 \xd1\x82\xd0\xb0\xd0\xb1\xd0\xbb\xd0\xb8\xd1\x86\xd1\x8b', blank=True)),
                ('second_field', models.CharField(max_length=100, verbose_name=b'\xd0\x92\xd1\x82\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb5 \xd0\xbf\xd0\xbe\xd0\xbb\xd0\xb5 \xd1\x82\xd0\xb0\xd0\xb1\xd0\xbb\xd0\xb8\xd1\x86\xd1\x8b', blank=True)),
                ('third_field', models.CharField(max_length=100, verbose_name=b'\xd0\xa2\xd1\x80\xd0\xb5\xd1\x82\xd1\x8c\xd0\xb5 \xd0\xbf\xd0\xbe\xd0\xbb\xd0\xb5 \xd1\x82\xd0\xb0\xd0\xb1\xd0\xbb\xd0\xb8\xd1\x86\xd1\x8b', blank=True)),
                ('fourth_field', models.CharField(max_length=100, verbose_name=b'\xd0\xa7\xd0\xb5\xd1\x82\xd0\xb2\xd0\xb5\xd1\x80\xd1\x82\xd0\xbe\xd0\xb5 \xd0\xbf\xd0\xbe\xd0\xbb\xd0\xb5 \xd1\x82\xd0\xb0\xd0\xb1\xd0\xbb\xd0\xb8\xd1\x86\xd1\x8b', blank=True)),
                ('fifth_field', models.CharField(max_length=100, verbose_name=b'\xd0\x9f\xd1\x8f\xd1\x82\xd0\xbe\xd0\xb5 \xd0\xbf\xd0\xbe\xd0\xbb\xd0\xb5 \xd1\x82\xd0\xb0\xd0\xb1\xd0\xbb\xd0\xb8\xd1\x86\xd1\x8b', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SecondPriceTable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x82\xd0\xb0\xd0\xb1\xd0\xbb\xd0\xb8\xd1\x86\xd1\x8b', blank=True)),
                ('first_field', models.CharField(max_length=100, verbose_name=b'\xd0\x9f\xd0\xb5\xd1\x80\xd0\xb2\xd0\xbe\xd0\xb5 \xd0\xbf\xd0\xbe\xd0\xbb\xd0\xb5 \xd1\x82\xd0\xb0\xd0\xb1\xd0\xbb\xd0\xb8\xd1\x86\xd1\x8b', blank=True)),
                ('second_field', models.CharField(max_length=100, verbose_name=b'\xd0\x92\xd1\x82\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb5 \xd0\xbf\xd0\xbe\xd0\xbb\xd0\xb5 \xd1\x82\xd0\xb0\xd0\xb1\xd0\xbb\xd0\xb8\xd1\x86\xd1\x8b', blank=True)),
                ('third_field', models.CharField(max_length=100, verbose_name=b'\xd0\xa2\xd1\x80\xd0\xb5\xd1\x82\xd1\x8c\xd0\xb5 \xd0\xbf\xd0\xbe\xd0\xbb\xd0\xb5 \xd1\x82\xd0\xb0\xd0\xb1\xd0\xbb\xd0\xb8\xd1\x86\xd1\x8b', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='fieldsprice',
            name='price',
        ),
        migrations.DeleteModel(
            name='FieldsPrice',
        ),
        migrations.DeleteModel(
            name='Price',
        ),
    ]
