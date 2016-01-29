# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(help_text=b'\xd0\xa0\xd0\xb0\xd0\xb7\xd0\xbc\xd0\xb5\xd1\x80 \xd0\xba\xd0\xb0\xd1\x80\xd1\x82\xd0\xb8\xd0\xbd\xd0\xba\xd0\xb8 920x330px. Max 5 picture.', upload_to=b'slider/', verbose_name=b'\xd0\x94\xd0\xbb\xd1\x8f \xd0\xa1\xd0\xbb\xd0\xb0\xd0\xb9\xd0\xb4\xd0\xb5\xd1\x80\xd0\xb0', blank=True)),
                ('home', models.ForeignKey(to='home.Home')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='home',
            name='slider',
        ),
    ]
