# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0030_auto_20150718_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to=b'media'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(unique=True, max_length=80),
        ),
    ]
