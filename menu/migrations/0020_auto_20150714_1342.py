# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0019_auto_20150714_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppinglist',
            name='amount',
            field=models.DecimalField(max_digits=10, default=0.0, null=True, decimal_places=2, blank=True),
        ),
    ]
