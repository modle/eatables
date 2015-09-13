# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_auto_20150913_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='dishType',
            field=models.ForeignKey(default=1, to='menu.DishType'),
            preserve_default=False,
        ),
    ]
