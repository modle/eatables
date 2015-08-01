# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_recipe_temperature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='amount',
            field=models.DecimalField(max_digits=5, decimal_places=2),
        ),
    ]
