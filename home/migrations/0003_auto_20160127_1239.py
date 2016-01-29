# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20160126_1336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=15)),
                ('message', models.TextField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(upload_to=b'slider/', verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x80\xd1\x82\xd0\xb8\xd0\xbd\xd0\xba\xd0\xb0 \xd0\xb4\xd0\xbb\xd1\x8f \xd1\x81\xd0\xbb\xd0\xb0\xd0\xb9\xd0\xb4\xd0\xb5\xd1\x80\xd0\xb0. Max 5 picture.', blank=True),
            preserve_default=True,
        ),
    ]
