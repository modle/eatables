# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('menu', '0010_auto_20150913_2052'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.IntegerField(null=True)),
                ('publishDate', models.DateTimeField(default=datetime.datetime.now)),
                ('editDate', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'ordering': ('-publishDate', '-id'),
            },
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='rating',
        ),
        migrations.AddField(
            model_name='rating',
            name='recipe',
            field=models.ForeignKey(to='menu.Recipe'),
        ),
        migrations.AddField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
