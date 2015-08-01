# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_auto_20150712_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cookTime',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='directions',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='prepMethod',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='prepTime',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='servings',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='temperature',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='url',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
    ]
