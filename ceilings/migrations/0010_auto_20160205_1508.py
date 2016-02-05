# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ceilings', '0009_auto_20160205_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ceiling',
            name='slug',
            field=models.SlugField(help_text=b'\xd0\x92\xd0\xb2\xd0\xb5\xd0\xb4\xd0\xb8\xd1\x82\xd0\xb5 URL \xd0\xb1\xd0\xb5\xd0\xb7 "/" \xd0\xb8 \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb1\xd0\xb5\xd0\xbb\xd0\xbe\xd0\xb2.', unique=True, max_length=100, verbose_name='URL \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438'),
            preserve_default=True,
        ),
    ]
