# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0012_auto_20150917_2219'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shoppinglist',
            options={'ordering': ('completed', 'name', 'shoppingListId')},
        ),
        migrations.RenameField(
            model_name='shoppinglist',
            old_name='status',
            new_name='completed',
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='comment',
            field=models.CharField(max_length=80, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]
