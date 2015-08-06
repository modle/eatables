# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0010_auto_20150804_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppinglist',
            name='name',
            field=models.CharField(default='', max_length=80),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fridge',
            name='expires',
            field=models.DateField(default=datetime.datetime(2015, 8, 19, 21, 15, 28, 642179)),
        ),
    ]
