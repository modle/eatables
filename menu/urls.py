from django.conf.urls import url

from . import views


urlpatterns = [
    # index and base
    url(r'^$', views.basetemplate, name='basetemplate'),
    url(r'^menu/$', views.index, name='index'),

    # recipe
    url(r'^(?P<recipe_id>[0-9]+)/$', views.recipedetails, name='recipedetails'),
    url(r'^archivedrecipes/$', views.archivedrecipes, name='archivedrecipes'),
    url(r'^addrecipe/$', views.addrecipe, name='addrecipe'),
    url(r'^(?P<recipeId>[0-9]+)/editrecipe/$', views.editrecipe, name='editrecipe'),
    url(r'^(?P<recipeId>[0-9]+)/deleterecipeforever/$', views.deleterecipeforever, name='deleterecipeforever'),
    url(r'^uploadrecipe/$', views.uploadrecipe, name='uploadrecipe'),

    # non-generic ingredient views
    url(r'^(?P<recipeId>[0-9]+)/updateingredient/$', views.updateingredient, name='updateingredient'),
    url(r'^(?P<recipeId>[0-9]+)/addingredient/$', views.addingredient, name='addingredient'),
    url(r'^(?P<ingredient_id>[0-9]+)/edit_ingredient/$', views.edit_ingredient, name='edit_ingredient'),
    url(r'^(?P<ingredient_id>[0-9]+)/delete_ingredient/$', views.delete_ingredient, name='delete_ingredient'),
    url(r'^uploadingredients/$', views.uploadingredients, name='uploadingredients'),

    # shopping list
    url(r'^(?P<ingredient_id>[0-9]+)/add_toshopping_list/$', views.add_to_shoppinglist, name='add_to_shoppinglist'),
    url(r'^shopping_list/$', views.shopping_list, name='shopping_list'),
    url(r'^(?P<shopping_list_id>[0-9]+)/shopping_list_check_off/$', views.shopping_list_check_off, name='shopping_list_check_off'),

    # url(r'^update_rating', views.update_rating, name='update_rating'),

    # comments
    url(r'^(?P<commentId>[0-9]+)/commentdelete/$', views.commentdelete, name='commentdelete'),

    # fridge
    url(r'^fridge/$', views.fridge, name='fridge'),

    # profile
    url(r'^profile/(?P<slug>[^\.]+)/$', views.profile, name='profile'),

    # categories and dish types
    url(r'^menu/category/(?P<slug>[^\.]+)', views.view_category, name='view_category'),
    url(r'^menu/dishtype/(?P<slug>[^\.]+)', views.view_dish_type, name='view_dish_type'),
]
