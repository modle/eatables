# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0016_auto_20151121_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='category',
        ),
        migrations.AddField(
            model_name='recipe',
            name='cook_method',
            field=models.IntegerField(default=0, choices=[(0, b''), (1, b'Grill'), (2, b'Oven'), (3, b'Slow Cooker'), (4, b'Stovetop')]),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='dish_type',
            field=models.IntegerField(default=0, choices=[(0, b''), (1, b'Dessert'), (2, b'Main'), (3, b'Pie'), (4, b'Salad'), (5, b'Side'), (6, b'Soup')]),
        ),
        migrations.DeleteModel(
            name='CookMethod',
        ),
        migrations.DeleteModel(
            name='DishType',
        ),
    ]
