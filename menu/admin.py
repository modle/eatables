from django.contrib import admin

# Register your models here.
from .models import Recipe, Ingredient, ShoppingList, IngredientMaster, Comment


admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(ShoppingList)
admin.site.register(IngredientMaster)
admin.site.register(Comment)
