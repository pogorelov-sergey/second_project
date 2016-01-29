# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0002_auto_20160129_1437'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FieldsPrice',
        ),
    ]
