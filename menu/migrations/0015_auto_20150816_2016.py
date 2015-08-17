# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0014_auto_20150809_2057'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shoppinglist',
            options={'ordering': ('status', 'name', 'shoppingListId')},
        ),
        migrations.AlterField(
            model_name='fridge',
            name='expires',
            field=models.DateField(default=datetime.datetime(2015, 8, 30, 20, 16, 36, 918086)),
        ),
    ]
