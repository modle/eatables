# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0016_auto_20150713_2235'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredient',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='ingredientmaster',
            options={'ordering': ('name', 'id')},
        ),
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='shoppinglist',
            options={'ordering': ('status', 'ingredient__name', 'id')},
        ),
    ]
