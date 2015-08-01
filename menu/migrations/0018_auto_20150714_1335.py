# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0017_auto_20150714_1232'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shoppinglist',
            options={'ordering': ('-status', 'ingredient__name', 'id')},
        ),
        migrations.AddField(
            model_name='shoppinglist',
            name='amount',
            field=models.DecimalField(decimal_places=2, blank=True, default=0.0, max_digits=5, null=True),
        ),
    ]
