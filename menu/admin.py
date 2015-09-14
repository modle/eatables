from django.contrib import admin

# Register your models here.
from .models import Recipe, Ingredient, ShoppingList, IngredientMaster, Comment, Category, Fridge, DishType, Rating


admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(ShoppingList)
admin.site.register(IngredientMaster)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Fridge)
admin.site.register(DishType)
admin.site.register(Rating)
