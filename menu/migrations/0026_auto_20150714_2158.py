# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0025_auto_20150714_2029'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-publishDate', '-id')},
        ),
        migrations.AlterModelOptions(
            name='shoppinglist',
            options={'ordering': ('status', 'ingredient__name', 'id')},
        ),
        migrations.AddField(
            model_name='comment',
            name='rating',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='publishDate',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 15, 2, 58, 17, 63834, tzinfo=utc), verbose_name=b'date published'),
        ),
    ]
