from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.RecipeDetail.as_view(), name='recipedetails'),
    url(r'^$', views.basetemplate, name='basetemplate'),
    url(r'^menu/$', views.Index.as_view(), name='index'),
    url(r'^retiredrecipes/$', views.retiredrecipes, name='retiredrecipes'),
    url(r'^(?P<pk>[0-9]+)/editrecipe$', views.EditRecipe.as_view(), name='editrecipe'),
    url(r'^addrecipe/$', views.addrecipe, name='addrecipe'),
    url(r'^(?P<recipeId>[0-9]+)/disablerecipe/$', views.disablerecipe, name='disablerecipe'),
    url(r'^(?P<recipeId>[0-9]+)/deleterecipeforever/$', views.deleterecipeforever, name='deleterecipeforever'),
    url(r'^(?P<recipeId>[0-9]+)/updaterecipe/$', views.updaterecipe, name='updaterecipe'),
    url(r'^(?P<recipeId>[0-9]+)/updateingredient/$', views.updateingredient, name='updateingredient'),
    url(r'^(?P<recipeId>[0-9]+)/addingredient/$', views.addingredient, name='addingredient'),
    url(r'^(?P<ingredientId>[0-9]+)/deleteingredient/$', views.deleteingredient, name='deleteingredient'),
    url(r'^(?P<recipeId>[0-9]+)/addtoshoppinglist/$', views.addtoshoppinglist, name='addtoshoppinglist'),
    url(r'^manageshoppinglist/$', views.manageshoppinglist, name='manageshoppinglist'),
    url(r'^archivelist/$', views.ArchiveList.as_view(), name='archivelist'),
    url(r'^(?P<recipeId>[0-9]+)/addcomment/$', views.addcomment, name='addcomment'),
    url(r'^uploadrecipe/$', views.uploadrecipe, name='uploadrecipe'),
    url(r'^uploadingredients/$', views.uploadingredients, name='uploadingredients'),
    url(r'^fridge/$', views.fridge, name='fridge'),
]
