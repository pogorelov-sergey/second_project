# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0003_delete_fieldsprice'),
    ]

    operations = [
        migrations.CreateModel(
            name='FieldsPrice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_field', models.CharField(max_length=100, verbose_name=b'\xd0\x9f\xd0\xb5\xd1\x80\xd0\xb2\xd0\xbe\xd0\xb5 \xd0\xbf\xd0\xbe\xd0\xbb\xd0\xb5 \xd1\x82\xd0\xb0\xd0\xb1\xd0\xbb\xd0\xb8\xd1\x86\xd1\x8b', blank=True)),
                ('second_field', models.CharField(max_length=100, verbose_name=b'\xd0\x92\xd1\x82\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb5 \xd0\xbf\xd0\xbe\xd0\xbb\xd0\xb5 \xd1\x82\xd0\xb0\xd0\xb1\xd0\xbb\xd0\xb8\xd1\x86\xd1\x8b', blank=True)),
                ('third_field', models.CharField(max_length=100, verbose_name=b'\xd0\xa2\xd1\x80\xd0\xb5\xd1\x82\xd1\x8c\xd0\xb5 \xd0\xbf\xd0\xbe\xd0\xbb\xd0\xb5 \xd1\x82\xd0\xb0\xd0\xb1\xd0\xbb\xd0\xb8\xd1\x86\xd1\x8b', blank=True)),
                ('fourth_field', models.CharField(max_length=100, verbose_name=b'\xd0\xa7\xd0\xb5\xd1\x82\xd0\xb2\xd0\xb5\xd1\x80\xd1\x82\xd0\xbe\xd0\xb5 \xd0\xbf\xd0\xbe\xd0\xbb\xd0\xb5 \xd1\x82\xd0\xb0\xd0\xb1\xd0\xbb\xd0\xb8\xd1\x86\xd1\x8b', blank=True)),
                ('fifth_field', models.CharField(max_length=100, verbose_name=b'\xd0\x9f\xd1\x8f\xd1\x82\xd0\xbe\xd0\xb5 \xd0\xbf\xd0\xbe\xd0\xbb\xd0\xb5 \xd1\x82\xd0\xb0\xd0\xb1\xd0\xbb\xd0\xb8\xd1\x86\xd1\x8b', blank=True)),
                ('price', models.ForeignKey(to='prices.Price')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
