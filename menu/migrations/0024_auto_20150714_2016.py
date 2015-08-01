# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0023_auto_20150714_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 15, 1, 16, 32, 976807, tzinfo=utc), verbose_name=b'date published'),
        ),
    ]
