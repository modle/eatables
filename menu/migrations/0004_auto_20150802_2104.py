# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_delete_document'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredient',
            options={'ordering': ('sorting', 'id')},
        ),
        migrations.AddField(
            model_name='ingredient',
            name='sorting',
            field=models.IntegerField(help_text=b'A number.', null=True, verbose_name=b'Ordering', blank=True),
        ),
    ]
