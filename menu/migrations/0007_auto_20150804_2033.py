# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_auto_20150804_2031'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fridge',
            old_name='recipe',
            new_name='item',
        ),
        migrations.AlterField(
            model_name='fridge',
            name='expires',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 18, 20, 33, 21, 219440)),
        ),
    ]
