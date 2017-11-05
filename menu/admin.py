from django.contrib import admin

# Register your models here.
from .models import Recipe, Ingredient, Tag, ShoppingList, IngredientMaster, Comment, Fridge, Rating


admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Tag)
admin.site.register(ShoppingList)
admin.site.register(IngredientMaster)
admin.site.register(Comment)
admin.site.register(Fridge)
admin.site.register(Rating)
