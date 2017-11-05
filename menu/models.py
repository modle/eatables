from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from menu.choices import *


class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80, unique=True)
    cook_method = models.IntegerField(choices=COOK_METHOD_CHOICES, default=0)
    temperature = models.CharField(max_length=10, null=True, blank=True)
    directions = models.TextField(null=True)
    source = models.CharField(max_length=1000, null=True, blank=True)
    servings = models.IntegerField(default=0)
    prep_time = models.IntegerField(default=0)
    cook_time = models.IntegerField(default=0)
    user = models.ForeignKey(User, null=True, blank=True)
    publish_date = models.DateTimeField(default=timezone.now)
    edit_date = models.DateTimeField(default=timezone.now)
    pinned = models.BooleanField(default=False)
    banner_image = models.CharField(max_length=1000, null=True, blank=True)
    dish_type = models.IntegerField(choices=DISH_TYPE_CHOICES, default=0)
    description = models.TextField(null=True, blank=True)

    # rating = RatingField(range=5)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )


class Ingredient(models.Model):
    id = models.AutoField(primary_key=True)
    recipe = models.ForeignKey(Recipe)
    name = models.CharField(max_length=80, null=False)
    comment = models.CharField(max_length=80, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=3, default=0.0)
    unit = models.CharField(max_length=30, null=True, blank=True)
    sorting = models.IntegerField("Ordering", blank=False, null=False, help_text="A number.")

    def __str__(self):
        return str(self.unit) + " " + str(self.name)

    class Meta:
        ordering = ('recipe_id', 'sorting', 'id', )
        unique_together = ('name', 'recipe', 'amount', 'unit',)
        select_on_save = True


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    recipe = models.ManyToManyField(Recipe)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class ShoppingList(models.Model):
    shoppingListId = models.AutoField(primary_key=True)
    ingredient = models.ForeignKey(Ingredient, blank=False)
    name = models.CharField(max_length=80, null=False)
    amount = models.IntegerField(default=0, null=True, blank=True)
    completed = models.BooleanField(default=False) # change to completed

    def __str__(self):
        return str(self.ingredient_id) + " " + str(self.status) + " " + str(self.amount)

    class Meta:
        ordering = ('completed', 'name', 'shoppingListId')


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
    comment = models.TextField(null=False)
    rating = models.IntegerField(null=True)
    user = models.ForeignKey(User, null=True, blank=True)
    publishDate = models.DateTimeField(default=timezone.now)
    editDate = models.DateTimeField(default=timezone.now)

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
    store = models.CharField(max_length=30)
    lastPurchaseDate = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.id) + str(self.purchaseAmount) + str(self.price/self.purchaseAmount)

    class Meta:
        ordering = ('ingredient__name', 'id')


class Fridge(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.CharField(max_length=80, unique=True, null=False)
    fridgedate = models.DateField(default=timezone.now)
    expires = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.recipe) + " " + str(self.fridgedate)

    class Meta:
        ordering = ('fridgedate', 'id')


class Rating(models.Model):
    recipe = models.ForeignKey(Recipe)
    rating = models.IntegerField(null=True)
    user = models.ForeignKey(User, null=True, blank=True)
    publishDate = models.DateTimeField(default=timezone.now)
    editDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.id) + str(self.comment)

    class Meta:
        ordering = ('-publishDate', '-id')
        unique_together = ('recipe', 'user', )
