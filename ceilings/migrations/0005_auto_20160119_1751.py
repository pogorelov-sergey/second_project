# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ceilings', '0004_auto_20160119_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalnoeopisanie',
            name='image',
            field=models.ImageField(help_text=b'150x150px', upload_to=b'images/', verbose_name=b'\xd0\xa1\xd1\x81\xd1\x8b\xd0\xbb\xd0\xba\xd0\xb0 \xd0\xba\xd0\xb0\xd1\x80\xd1\x82\xd0\xb8\xd0\xbd\xd0\xba\xd0\xb8', blank=True),
            preserve_default=True,
        ),
    ]
