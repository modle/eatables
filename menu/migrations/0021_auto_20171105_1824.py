# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0020_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='recipe',
        ),
        migrations.AddField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(to='menu.Tag'),
        ),
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(default='deleteme', unique=True, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tag',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
        ),
    ]
