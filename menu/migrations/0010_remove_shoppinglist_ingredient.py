# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0009_auto_20150712_2335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppinglist',
            name='ingredient',
        ),
    ]
