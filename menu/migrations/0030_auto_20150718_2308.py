# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0029_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cookTime',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='prepTime',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='servings',
            field=models.IntegerField(default=0),
        ),
    ]
