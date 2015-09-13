# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_auto_20150913_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='bannerImage',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
    ]
