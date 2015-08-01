# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0027_auto_20150714_2205'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseHistory',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('purchaseAmount', models.DecimalField(default=0.0, null=True, max_digits=10, decimal_places=2, blank=True)),
                ('purchaseUnit', models.CharField(max_length=30, null=True)),
                ('price', models.DecimalField(default=0.0, null=True, max_digits=10, decimal_places=2, blank=True)),
                ('store', models.CharField(max_length=30)),
                ('lastPurchaseDate', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'ordering': ('ingredient__name', 'id'),
            },
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='comment',
            field=models.CharField(max_length=80, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=80, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='ingredientmaster',
            name='name',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='prepMethod',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='source',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='temperature',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='purchasehistory',
            name='ingredient',
            field=models.ForeignKey(to='menu.Ingredient'),
        ),
    ]
