# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0002_auto_20160129_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculator',
            name='order',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
