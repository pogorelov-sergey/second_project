# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='calculator',
            name='order',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='calculator',
            name='content',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='calculator',
            name='name',
            field=models.CharField(max_length=100, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='calculator',
            name='phone',
            field=models.CharField(max_length=15, verbose_name=b'\xd0\x9d\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd1\x82\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd\xd0\xb0', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='calculator',
            name='title',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
