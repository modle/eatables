# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0011_auto_20150805_2115'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shoppinglist',
            options={'ordering': ('status', 'name', 'shoppingListId')},
        ),
        migrations.RenameField(
            model_name='shoppinglist',
            old_name='id',
            new_name='shoppingListId',
        ),
        migrations.AlterField(
            model_name='fridge',
            name='expires',
            field=models.DateField(default=datetime.datetime(2015, 8, 19, 21, 56, 14, 555103)),
        ),
    ]
