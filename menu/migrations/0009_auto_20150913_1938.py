# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0008_auto_20150913_1119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='bannerImage',
            new_name='banner_image',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='cookTime',
            new_name='cook_time',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='dishType',
            new_name='dish_type',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='editDate',
            new_name='edit_date',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='prepTime',
            new_name='prep_time',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='publishDate',
            new_name='publish_date',
        ),
    ]
