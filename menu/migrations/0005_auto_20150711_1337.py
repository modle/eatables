# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20150711_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='amount',
            field=models.DecimalField(default=None, max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
