# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0015_auto_20151017_2330'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='CookMethod',
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='sorting',
            field=models.IntegerField(default=0, help_text=b'A number.', verbose_name=b'Ordering'),
            preserve_default=False,
        ),
    ]
