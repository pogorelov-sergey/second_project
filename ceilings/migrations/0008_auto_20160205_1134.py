# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ceilings', '0007_detalnoeopisanie_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='ceiling',
            name='slug',
            field=models.SlugField(default='', max_length=100, verbose_name='URL \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='detalnoeopisanie',
            name='image',
            field=models.ImageField(upload_to=b'images/', verbose_name=b'\xd0\xa1\xd1\x81\xd1\x8b\xd0\xbb\xd0\xba\xd0\xb0 \xd0\xba\xd0\xb0\xd1\x80\xd1\x82\xd0\xb8\xd0\xbd\xd0\xba\xd0\xb8', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='detalnoeopisanie',
            name='short_description',
            field=models.TextField(null=True, verbose_name='\u041a\u0440\u0430\u0442\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
            preserve_default=True,
        ),
    ]
