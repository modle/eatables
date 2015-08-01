# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0012_auto_20150713_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='comment',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
