# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20150802_1634'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Document',
        ),
    ]
