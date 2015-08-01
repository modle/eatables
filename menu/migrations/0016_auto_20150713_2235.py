# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0015_ingredientmaster'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='enabled',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='amount',
            field=models.DecimalField(default=0.0, null=True, max_digits=5, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
