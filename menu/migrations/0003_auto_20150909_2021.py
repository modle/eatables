# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('menu', '0002_auto_20150908_2017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, db_index=True)),
                ('slug', models.SlugField(unique=True, max_length=100)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='enabled',
            new_name='published',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='prepMethod',
        ),
        migrations.AddField(
            model_name='recipe',
            name='editDate',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='recipe',
            name='pinned',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='recipe',
            name='publishDate',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='recipe',
            name='rating',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
