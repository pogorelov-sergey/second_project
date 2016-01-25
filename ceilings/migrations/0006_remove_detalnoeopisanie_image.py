# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ceilings', '0005_auto_20160119_1751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detalnoeopisanie',
            name='image',
        ),
    ]
