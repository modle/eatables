# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0021_auto_20150714_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='recipe',
            field=models.ForeignKey(default=0, to='menu.Recipe'),
            preserve_default=False,
        ),
    ]
