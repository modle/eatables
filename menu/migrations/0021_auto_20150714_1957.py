# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0020_auto_20150714_1342'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('comment', models.TextField(null=True)),
                ('user', models.IntegerField(default=1)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='url',
        ),
        migrations.AddField(
            model_name='recipe',
            name='source',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cookTime',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='directions',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='prepMethod',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='prepTime',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='servings',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='temperature',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
