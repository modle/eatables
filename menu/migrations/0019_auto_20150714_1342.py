# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0018_auto_20150714_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='amount',
            field=models.DecimalField(decimal_places=2, null=True, blank=True, default=0.0, max_digits=10),
        ),
    ]
