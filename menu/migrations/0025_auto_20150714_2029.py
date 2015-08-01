# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0024_auto_20150714_2016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='comment',
            name='publishDate',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 15, 1, 29, 11, 230653, tzinfo=utc), verbose_name=b'date published'),
        ),
    ]
