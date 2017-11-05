# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0019_auto_20170910_0133'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('recipe', models.ManyToManyField(to='menu.Recipe')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
