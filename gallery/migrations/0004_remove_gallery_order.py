# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20160120_1528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='order',
        ),
    ]
