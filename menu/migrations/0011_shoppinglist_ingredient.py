# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0010_remove_shoppinglist_ingredient'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppinglist',
            name='ingredient',
            field=models.ForeignKey(default=0, to='menu.Ingredient'),
            preserve_default=False,
        ),
    ]
