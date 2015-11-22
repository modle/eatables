# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0017_auto_20151121_1645'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='published',
        ),
    ]
