# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0036_auto_20150729_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
    ]
