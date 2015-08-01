# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0014_auto_20150713_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='IngredientMaster',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
