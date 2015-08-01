# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('amount', models.IntegerField()),
                ('unit', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('prepMethod', models.CharField(max_length=200)),
                ('directions', models.TextField()),
                ('url', models.CharField(max_length=200)),
                ('servings', models.IntegerField()),
                ('prepTime', models.IntegerField()),
                ('cookTime', models.IntegerField()),
            ],
            options={
                'ordering': ('name', 'prepMethod'),
            },
        ),
        migrations.AddField(
            model_name='ingredient',
            name='recipe',
            field=models.ForeignKey(to='menu.Recipe'),
        ),
    ]
