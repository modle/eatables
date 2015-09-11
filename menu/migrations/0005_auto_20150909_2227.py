# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_recipe_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]
