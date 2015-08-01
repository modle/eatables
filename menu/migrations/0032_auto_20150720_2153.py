# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0031_auto_20150719_2151'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='ingredient',
            unique_together=set([('name', 'recipe', 'amount', 'unit')]),
        ),
    ]
