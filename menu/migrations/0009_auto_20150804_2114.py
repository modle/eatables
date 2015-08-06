# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0008_auto_20150804_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fridge',
            name='expires',
            field=models.DateField(default=datetime.datetime(2015, 8, 18, 21, 14, 30, 119252)),
        ),
    ]
