
from django.conf.urls import include, url
from django.contrib import admin

from menu import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^accounts/loggedin/$', 'menu.views.loggedin', name='loggedin'),
    url(r'^accounts/not_authorized/$', 'menu.views.not_authorized', name='not_authorized'),
    url(r'^loggedout/$', 'menu.views.loggedout', name='loggedout'),

    # default view
    url(r'^$', views.profile, name='profile'),

    # all recipes
    url(r'^clear_recipe_filter/$', views.clear_recipe_filter, name='clear_recipe_filter'),
    url(r'^discover/$', views.discover, name='discover'),

    # recipe
    url(r'^(?P<recipe_id>[0-9]+)/recipe_details/$', views.recipe_details, name='recipe_details'),
    url(r'^add_recipe/$', views.add_recipe, name='add_recipe'),
    url(r'^(?P<recipe_id>[0-9]+)/edit_recipe/$', views.edit_recipe, name='edit_recipe'),
    url(r'^(?P<recipe_id>[0-9]+)/delete_recipe_forever/$', views.delete_recipe_forever, name='delete_recipe_forever'),

    # ingredients
    url(r'^(?P<ingredient_id>[0-9]+)/edit_ingredient/$', views.edit_ingredient, name='edit_ingredient'),
    url(r'^(?P<ingredient_id>[0-9]+)/delete_ingredient/$', views.delete_ingredient, name='delete_ingredient'),
    url(r'^(?P<ingredient_id>[0-9]+)/move_ingredient_up/$', views.move_ingredient_up, name='move_ingredient_up'),
    url(r'^(?P<ingredient_id>[0-9]+)/move_ingredient_down/$', views.move_ingredient_down, name='move_ingredient_down'),

    # shopping list
    url(r'^add_to_shopping_list/$', views.add_to_shopping_list, name='add_to_shopping_list'),
    url(r'^shopping_list/$', views.shopping_list, name='shopping_list'),
    url(r'^(?P<shopping_list_id>[0-9]+)/shopping_list_check_off/$', views.shopping_list_check_off, name='shopping_list_check_off'),
    url(r'^(?P<shopping_list_id>[0-9]+)/shopping_list_delete/$', views.shopping_list_delete, name='shopping_list_delete'),

    # comments
    url(r'^(?P<comment_id>[0-9]+)/comment_delete/$', views.comment_delete, name='comment_delete'),

    # fridge
    url(r'^fridge/$', views.fridge, name='fridge'),
]
