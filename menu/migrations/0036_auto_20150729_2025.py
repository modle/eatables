# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0035_auto_20150727_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppinglist',
            name='amount',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
    ]
