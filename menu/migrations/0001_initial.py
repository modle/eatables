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
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('docfile', models.FileField(upload_to=b'media')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=80)),
                ('comment', models.CharField(max_length=80, null=True, blank=True)),
                ('amount', models.DecimalField(default=0.0, max_digits=10, decimal_places=2)),
                ('unit', models.CharField(max_length=30, null=True, blank=True)),
            ],
            options={
                'ordering': ('id',),
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
                ('purchaseUnit', models.CharField(max_length=30, null=True)),
                ('price', models.DecimalField(default=0.0, null=True, max_digits=10, decimal_places=2, blank=True)),
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
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('amount', models.IntegerField(default=0, null=True, blank=True)),
                ('status', models.BooleanField(default=False)),
                ('ingredient', models.ForeignKey(to='menu.Ingredient')),
            ],
            options={
                'ordering': ('status', 'ingredient__name', 'id'),
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
