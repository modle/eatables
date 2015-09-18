from django.conf.urls import url

from . import views


urlpatterns = [
    # index and base
    url(r'^$', views.basetemplate, name='basetemplate'),

    # generic views
    # url(r'^(?P<pk>[0-9]+)/$', views.RecipeDetail.as_view(), name='recipedetails'),
    url(r'^menu/$', views.index, name='index'),
    # url(r'^menu/$', views.Index.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/editingredients$', views.EditIngredients.as_view(), name='editingredients'),
    url(r'^archivelist/$', views.ArchiveList.as_view(), name='archivelist'),

    # non-generic recipe views
    url(r'^(?P<recipeId>[0-9]+)/$', views.recipedetails, name='recipedetails'),
    url(r'^archivedrecipes/$', views.archivedrecipes, name='archivedrecipes'),
    url(r'^addrecipe/$', views.addrecipe, name='addrecipe'),
    url(r'^(?P<recipeId>[0-9]+)/editrecipe/$', views.editrecipe, name='editrecipe'),
    url(r'^(?P<recipeId>[0-9]+)/deleterecipeforever/$', views.deleterecipeforever, name='deleterecipeforever'),
    url(r'^uploadrecipe/$', views.uploadrecipe, name='uploadrecipe'),

    # non-generic ingredient views
    url(r'^(?P<recipeId>[0-9]+)/updateingredient/$', views.updateingredient, name='updateingredient'),
    url(r'^(?P<recipeId>[0-9]+)/addingredient/$', views.addingredient, name='addingredient'),
    url(r'^(?P<ingredientId>[0-9]+)/deleteingredient/$', views.deleteingredient, name='deleteingredient'),
    url(r'^uploadingredients/$', views.uploadingredients, name='uploadingredients'),

    # shopping list
    url(r'^(?P<recipeId>[0-9]+)/addtoshoppinglist/$', views.addtoshoppinglist, name='addtoshoppinglist'),
    url(r'^shoppinglist/$', views.shoppinglist, name='shoppinglist'),


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
