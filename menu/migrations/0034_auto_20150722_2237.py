# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0033_auto_20150722_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppinglist',
            name='status',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
