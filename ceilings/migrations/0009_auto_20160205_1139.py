# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ceilings', '0008_auto_20160205_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ceiling',
            name='slug',
            field=models.SlugField(unique=True, max_length=100, verbose_name='URL \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438'),
            preserve_default=True,
        ),
    ]
