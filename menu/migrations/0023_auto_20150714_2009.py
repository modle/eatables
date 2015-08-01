# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0022_comments_recipe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('comment', models.TextField(null=True)),
                ('user', models.IntegerField(default=1)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('recipe', models.ForeignKey(to='menu.Recipe')),
            ],
        ),
        migrations.RemoveField(
            model_name='comments',
            name='recipe',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
