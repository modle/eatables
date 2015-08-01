# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0011_shoppinglist_ingredient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppinglist',
            name='user',
        ),
        migrations.AddField(
            model_name='shoppinglist',
            name='status',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
