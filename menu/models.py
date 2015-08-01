from django.db import models
from datetime import datetime
from django import forms
import os
from eatables import settings

# Create your models here.
class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80, unique=True)
    prepMethod = models.CharField(max_length=30, null=True, blank=True)
    temperature = models.CharField(max_length=10, null=True, blank=True)
    directions = models.TextField(null=True)
    source = models.CharField(max_length=1000, null=True, blank=True)
    servings = models.IntegerField(default=0)
    prepTime = models.IntegerField(default=0)
    cookTime = models.IntegerField(default=0)
    enabled = models.BooleanField(default=True)
    def __str__(self):
        return self.name + "; " + self.prepMethod + "; " + str(self.id)

    class Meta:
        ordering = ('name', )

class Ingredient(models.Model):
    id = models.AutoField(primary_key=True)
    recipe = models.ForeignKey(Recipe)
    name = models.CharField(max_length=80, null=False)
    comment = models.CharField(max_length=80, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    unit = models.CharField(max_length=30, null=True, blank=True)
    def __str__(self):
        return str(self.unit) + " " + str(self.name)

    class Meta:
        ordering = ('id', )
        unique_together = ('name', 'recipe', 'amount', 'unit',)

class ShoppingList(models.Model):
    id = models.AutoField(primary_key=True)
    ingredient = models.ForeignKey(Ingredient, blank=False)
    amount = models.IntegerField(default=0, null=True, blank=True)
    status = models.BooleanField(default=False,)
    def __str__(self):
        return str(self.id) + " " + str(self.ingredient_id) + " " + str(self.status) + " " + str(self.amount)

    class Meta:
        ordering = ('status', 'ingredient__name', 'id')

class IngredientMaster(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    def __str__(self):
        return str(self.id) + str(self.name)

    class Meta:
        ordering = ('name', 'id')

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    recipe = models.ForeignKey(Recipe)
    comment = models.TextField(null=True)
    rating = models.IntegerField(null=True)
    user = models.IntegerField(default=1)
    publishDate = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return str(self.id) + str(self.comment)

    class Meta:
        ordering = ('-publishDate', '-id')

class PurchaseHistory(models.Model):
    id = models.AutoField(primary_key=True)
    ingredient = models.ForeignKey(Ingredient)
    purchaseAmount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, null=True, blank=True)
    purchaseUnit = models.CharField(max_length=30, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, null=True, blank=True)
    store = models.CharField(max_length=30)
    lastPurchaseDate = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.id) + str(self.purchaseAmount) + str(self.price/self.purchaseAmount)

    class Meta:
        ordering = ('ingredient__name', 'id')

class Document(models.Model):
    docfile = models.FileField(upload_to='media')

    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.docfile.name))
        super(Document, self).delete(*args, **kwargs)
