# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0013_ingredient_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='comment',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
