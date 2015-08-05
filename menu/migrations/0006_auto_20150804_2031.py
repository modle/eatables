# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_recipe_pinned'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fridge',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('recipe', models.CharField(unique=True, max_length=80)),
                ('fridgedate', models.DateTimeField(default=datetime.datetime.now)),
                ('expires', models.DateTimeField(default=datetime.datetime(2015, 8, 18, 20, 31, 18, 326829))),
            ],
            options={
                'ordering': ('fridgedate', 'id'),
            },
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='pinned',
        ),
    ]
