# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0034_auto_20150722_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppinglist',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
