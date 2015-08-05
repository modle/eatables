# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_auto_20150804_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fridge',
            name='expires',
            field=models.DateField(default=datetime.datetime(2015, 8, 18, 20, 58, 53, 496007)),
        ),
        migrations.AlterField(
            model_name='fridge',
            name='fridgedate',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
