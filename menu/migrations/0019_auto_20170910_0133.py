# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0018_remove_recipe_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(default='deleteme'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='amount',
            field=models.DecimalField(default=0.0, max_digits=10, decimal_places=3),
        ),
    ]
