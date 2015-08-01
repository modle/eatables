# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_auto_20150711_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='amount',
            field=models.DecimalField(default=0.0, max_digits=5, decimal_places=2),
        ),
    ]
