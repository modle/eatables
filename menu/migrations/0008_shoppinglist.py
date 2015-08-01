# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_auto_20150712_2305'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingList',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('amount', models.DecimalField(default=0.0, max_digits=5, decimal_places=2)),
                ('unit', models.CharField(default=None, max_length=200, null=True)),
                ('user', models.IntegerField(default=None, null=True)),
            ],
        ),
    ]
