from django.conf.urls import url

from . import views


urlpatterns = [
    # index and base
    url(r'^$', views.base_template, name='base_template'),
    url(r'^menu/$', views.index, name='index'),

    # recipe
    url(r'^(?P<recipe_id>[0-9]+)/$', views.recipe_details, name='recipe_details'),
    url(r'^add_recipe/$', views.add_recipe, name='add_recipe'),
    url(r'^(?P<recipe_id>[0-9]+)/edit_recipe/$', views.edit_recipe, name='edit_recipe'),
    url(r'^(?P<recipe_id>[0-9]+)/delete_recipe_forever/$', views.delete_recipe_forever, name='delete_recipe_forever'),

    # ingredients
    url(r'^(?P<ingredient_id>[0-9]+)/edit_ingredient/$', views.edit_ingredient, name='edit_ingredient'),
    url(r'^(?P<ingredient_id>[0-9]+)/delete_ingredient/$', views.delete_ingredient, name='delete_ingredient'),
    url(r'^(?P<ingredient_id>[0-9]+)/move_ingredient_up/$', views.move_ingredient_up, name='move_ingredient_up'),
    url(r'^(?P<ingredient_id>[0-9]+)/move_ingredient_down/$', views.move_ingredient_down, name='move_ingredient_down'),


    # shopping list
    url(r'^(?P<ingredient_id>[0-9]+)/add_to_shopping_list/$', views.add_to_shopping_list, name='add_to_shopping_list'),
    url(r'^shopping_list/$', views.shopping_list, name='shopping_list'),
    url(r'^(?P<shopping_list_id>[0-9]+)/shopping_list_check_off/$', views.shopping_list_check_off, name='shopping_list_check_off'),

    # url(r'^update_rating', views.update_rating, name='update_rating'),

    # comments
    url(r'^(?P<commentId>[0-9]+)/comment_delete/$', views.comment_delete, name='comment_delete'),

    # fridge
    url(r'^fridge/$', views.fridge, name='fridge'),

    # profile
    url(r'^profile/(?P<slug>[^\.]+)/$', views.profile, name='profile'),

    url(r'^clear_recipe_filter/$', views.clear_recipe_filter, name='clear_recipe_filter'),
]
