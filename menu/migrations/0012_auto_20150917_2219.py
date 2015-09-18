# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0011_auto_20150913_2106'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ('name',)},
        ),
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together=set([('recipe', 'user')]),
        ),
    ]
