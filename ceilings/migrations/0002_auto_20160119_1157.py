# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ceilings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ceiling',
            name='title',
            field=models.CharField(max_length=400, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ceiling',
            name='name',
            field=models.CharField(max_length=255, verbose_name='\u041e \u043f\u043e\u0442\u043e\u043b\u043a\u0430\u0445'),
            preserve_default=True,
        ),
    ]
