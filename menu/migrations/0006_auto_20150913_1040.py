# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_auto_20150909_2227'),
    ]

    operations = [
        migrations.CreateModel(
            name='DishType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, db_index=True)),
                ('slug', models.SlugField(unique=True, max_length=100)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.AddField(
            model_name='recipe',
            name='bannerImage',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='dishType',
            field=models.ForeignKey(default=1, to='menu.DishType'),
            preserve_default=False,
        ),
    ]
