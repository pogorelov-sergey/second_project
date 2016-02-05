# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_remove_gallery_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='slug',
            field=models.SlugField(default='', max_length=100, verbose_name='URL \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(help_text=b'\xd0\x9a\xd0\xb0\xd1\x80\xd1\x82\xd0\xb8\xd0\xbd\xd0\xba\xd0\xb0 \xd0\xba\xd0\xbe\xd1\x82\xd0\xbe\xd1\x80\xd0\xb0\xd1\x8f \xd0\xb2 \xd0\xb3\xd0\xb0\xd0\xbb\xd0\xb5\xd1\x80\xd0\xb5\xd0\xb5.', upload_to=b'gallery/', verbose_name=b'\xd0\xa1\xd1\x81\xd1\x8b\xd0\xbb\xd0\xba\xd0\xb0 \xd0\xba\xd0\xb0\xd1\x80\xd1\x82\xd0\xb8\xd0\xbd\xd0\xba\xd0\xb8', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='gallery',
            name='name',
            field=models.CharField(max_length=255, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x80\xd0\xb0\xd0\xb7\xd0\xb4\xd0\xb5\xd0\xbb\xd0\xb0 \xd0\xb3\xd0\xb0\xd0\xbb\xd0\xb5\xd1\x80\xd0\xb5\xd0\xb8.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.ImageField(upload_to=b'gallery/pictures/', verbose_name=b'\xd0\xa0\xd0\xb0\xd0\xb7\xd0\xbc\xd0\xb5\xd1\x80 \xd0\xba\xd0\xb0\xd1\x80\xd1\x82\xd0\xb8\xd0\xbd\xd0\xba\xd0\xb8 780x560px', blank=True),
            preserve_default=True,
        ),
    ]
