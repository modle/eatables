# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20150703_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cookTime',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='directions',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='prepMethod',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='prepTime',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='servings',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='temperature',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='url',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
