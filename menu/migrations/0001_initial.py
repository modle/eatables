# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('comment', models.TextField(null=True)),
                ('rating', models.IntegerField(null=True)),
                ('user', models.IntegerField(default=1)),
                ('publishDate', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'ordering': ('-publishDate', '-id'),
            },
        ),
        migrations.CreateModel(
            name='Fridge',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('item', models.CharField(unique=True, max_length=80)),
                ('fridgedate', models.DateField(default=datetime.datetime.now)),
                ('expires', models.DateField(default=datetime.datetime(2015, 9, 22, 20, 13, 54, 752469))),
            ],
            options={
                'ordering': ('fridgedate', 'id'),
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=80)),
                ('comment', models.CharField(max_length=80, null=True)),
                ('amount', models.DecimalField(default=0.0, max_digits=10, decimal_places=2)),
                ('unit', models.CharField(max_length=30, null=True)),
                ('sorting', models.IntegerField(help_text=b'A number.', null=True, verbose_name=b'Ordering', blank=True)),
            ],
            options={
                'ordering': ('sorting', 'id'),
                'select_on_save': True,
            },
        ),
        migrations.CreateModel(
            name='IngredientMaster',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'ordering': ('name', 'id'),
            },
        ),
        migrations.CreateModel(
            name='PurchaseHistory',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('purchaseAmount', models.DecimalField(default=0.0, null=True, max_digits=10, decimal_places=2, blank=True)),
                ('price', models.DecimalField(default=0.0, null=True, max_digits=10, decimal_places=2, blank=True)),
                ('purchaseUnit', models.CharField(max_length=30, null=True)),
                ('store', models.CharField(max_length=30)),
                ('lastPurchaseDate', models.DateTimeField(null=True, blank=True)),
                ('ingredient', models.ForeignKey(to='menu.Ingredient')),
            ],
            options={
                'ordering': ('ingredient__name', 'id'),
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=80)),
                ('prepMethod', models.CharField(max_length=30, null=True, blank=True)),
                ('temperature', models.CharField(max_length=10, null=True, blank=True)),
                ('directions', models.TextField(null=True)),
                ('source', models.CharField(max_length=1000, null=True, blank=True)),
                ('servings', models.IntegerField(default=0)),
                ('prepTime', models.IntegerField(default=0)),
                ('cookTime', models.IntegerField(default=0)),
                ('enabled', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ShoppingList',
            fields=[
                ('shoppingListId', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=80)),
                ('amount', models.IntegerField(default=0, null=True, blank=True)),
                ('status', models.BooleanField(default=False)),
                ('ingredient', models.ForeignKey(to='menu.Ingredient')),
            ],
            options={
                'ordering': ('status', 'name', 'shoppingListId'),
            },
        ),
        migrations.AddField(
            model_name='ingredient',
            name='recipe',
            field=models.ForeignKey(to='menu.Recipe'),
        ),
        migrations.AddField(
            model_name='comment',
            name='recipe',
            field=models.ForeignKey(to='menu.Recipe'),
        ),
        migrations.AlterUniqueTogether(
            name='ingredient',
            unique_together=set([('name', 'recipe', 'amount', 'unit')]),
        ),
    ]
