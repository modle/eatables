# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0008_shoppinglist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppinglist',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='shoppinglist',
            name='name',
        ),
        migrations.RemoveField(
            model_name='shoppinglist',
            name='unit',
        ),
        migrations.AddField(
            model_name='shoppinglist',
            name='ingredient',
            field=models.ForeignKey(default=0, to='menu.Ingredient'),
            preserve_default=False,
        ),
    ]
