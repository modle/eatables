# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0026_auto_20150714_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='publishDate',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
