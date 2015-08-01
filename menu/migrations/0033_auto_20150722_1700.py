# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0032_auto_20150720_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to='media'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='amount',
            field=models.DecimalField(default=0.0, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(default='', max_length=80),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(blank=True, null=True, max_length=30),
        ),
    ]
