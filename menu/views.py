from django.shortcuts import get_object_or_404, render_to_response, render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.template import RequestContext
import csv
from datetime import datetime
from django.forms.models import modelformset_factory
import logging
import json
import sys
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

from menu.forms import *
from .models import Recipe, Ingredient, Tag, ShoppingList, Fridge, Comment

def index(request):
    return HttpResponseRedirect(reverse('discover'))


def discover(request):

    search_form = SearchForm()

    if request.method == 'POST':
        search_form = SearchForm(request.POST)

        if search_form.is_valid():
            search_term = search_form.cleaned_data['search_term']

            recipes = Recipe.objects.filter(name__icontains=search_term)
            messages.info(request, search_term)
        else:
            recipes = Recipe.objects.filter(pinned='True')
    else:
        recipes = Recipe.objects.filter(pinned='True')

    return render(
        request,
        'discover.html',
        {
            'recipes': recipes,
            'search_form': search_form,
        },
    )


def add_to_shopping_list(request):
    ingredient_id = request.POST.get('ingredient_id')
    response_data = {}

    ingredient = Ingredient.objects.get(id=ingredient_id)
    list_item, created = ShoppingList.objects.get_or_create(ingredient_id=ingredient_id)

    list_item.amount = ingredient.amount
    list_item.name = ingredient.name
    list_item.ingredient = ingredient
    list_item.completed = False
    list_item.save()

    response_data['status'] = 'success'
    response_data['id'] = ingredient_id
    return JsonResponse(response_data)


def add_tag(request):
    recipe_id = request.POST.get('recipe_id')
    recipe = Recipe.objects.get(id=recipe_id)

    tag, created = recipe.tags.get_or_create(name=request.POST.get('name'))
    recipe.save()

    tags = ""
    for tag in recipe.tags.all():
        tags += " " + str(tag)

    response_data = {}
    response_data['status'] = 'success'
    response_data['tags'] = tags
    return JsonResponse(response_data)


@user_passes_test(lambda u: u.is_superuser, login_url='not_authorized')
def shopping_list(request):
    shopping_list_entries = ShoppingList.objects.all()

    return render_to_response(
        'shopping_list.html',
        {'shopping_list_entries': shopping_list_entries, },
        context_instance=RequestContext(request))


@user_passes_test(lambda u: u.is_superuser, login_url='not_authorized')
def shopping_list_check_off(request, shopping_list_id):

    shopping_list_entry = ShoppingList.objects.get(shoppingListId=shopping_list_id)
    shopping_list_entry.completed = True
    shopping_list_entry.save()

    return HttpResponseRedirect(reverse('shopping_list'))


@user_passes_test(lambda u: u.is_superuser, login_url='not_authorized')
def shopping_list_delete(request, shopping_list_id):
    ShoppingList.objects.filter(shoppingListId=shopping_list_id).delete()

    return HttpResponseRedirect(reverse('shopping_list'))


@user_passes_test(lambda u: u.is_superuser, login_url='not_authorized')
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)

        if form.is_valid():
            formpost = form.save(commit=False)
            formpost.user = request.user
            formpost.edited = datetime.now()
            formpost.save()
            recipe_id = formpost.id
            messages.info(request, 'Recipe successfully added.')
            return HttpResponseRedirect(reverse('recipe_details', args=(recipe_id,)))
        else:
            messages.error(request, 'Please fill out all fields.')

    else:
        form = RecipeForm()

    return render_to_response('edit_recipe.html', {'form': form},
                              context_instance=RequestContext(request))


def clear_messages(request):
    storage = messages.get_messages(request)
    storage.used = True


def is_valid_ingredient(ingredient):
    return True


def add_comment_to_recipe(request):
    commentPost = request.POST
    comment_form = CommentForm(commentPost)
    recipe = Recipe.objects.get(pk=commentPost['recipe_id'])
    user = request.user
    if comment_form.is_valid():
        comment_save = comment_form.save(commit=False)
        comment_save.user = user
        comment_save.editDate = datetime.now()
        comment_save.recipe = recipe
        comment_save.save()
        response_data = {}
        response_data['status'] = 'success'
        response_data['comment'] = commentPost
        response_data['id'] = comment_save.id
        response_data['publishDate'] = comment_save.publishDate
        return JsonResponse(response_data)
    else:
        messages.error(request, 'Comment is required.')


def add_ingredient_to_recipe(request):
    ingredientPost = request.POST
    recipe = Recipe.objects.get(pk=ingredientPost['recipe_id'])
    ingredientForm = IngredientForm(ingredientPost)
    ingredients = Ingredient.objects.filter(recipe_id=recipe)
    clear_messages(request)

    if ingredientForm.is_valid():
        ingredient_save = ingredientForm.save(commit=False)
        ingredient_save.recipe = recipe
        messages.info(request, 'Ingredient ' + ingredient_save.name + ' added.')

        if ingredients:
            max_ingredient_sorting = Ingredient.objects.filter(recipe_id=recipe).order_by('-sorting')[0]
            ingredient_save.sorting = max_ingredient_sorting.sorting + 10
        else:
            ingredient_save.sorting = 10

        ingredient_save.save()
        response_data = {}
        response_data['status'] = 'success'
        response_data['ingredient'] = ingredientPost
        response_data['id'] = ingredient_save.id
        return JsonResponse(response_data)
    else:
        messages.error(request, 'Ingredient name and amount are required.')


def recipe_details(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    user = request.user
    tag_form = TagForm()
    comment_form = CommentForm()
    ingredient_form = IngredientForm()
    return render_to_response('recipe_details.html',
                              {'tag_form': tag_form,
                               'comment_form': comment_form,
                               'ingredient_form': ingredient_form,
                               'recipe': recipe, },
                              context_instance=RequestContext(request))


@user_passes_test(lambda u: u.is_superuser, login_url='not_authorized')
def delete_recipe_forever(request, recipe_id):
    Recipe.objects.filter(pk=recipe_id).delete()
    return HttpResponseRedirect(reverse('my_recipes'))


@user_passes_test(lambda u: u.is_superuser, login_url='not_authorized')
def edit_recipe(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    ingredients = Ingredient.objects.filter(recipe_id=recipe)
    ingredient_form = IngredientForm()
    recipe_form = RecipeForm(instance=recipe)

    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST, instance=Recipe.objects.get(id=recipe_id))

        if recipe_form.is_valid():
            recipe_save = recipe_form.save(commit=False)
            recipe_save.user = request.user
            recipe_save.edited = datetime.now()
            recipe_save.save()
            recipe_id = recipe_save.id
            messages.info(request, 'Recipe successfully updated.')
            return HttpResponseRedirect(reverse('recipe_details', args=(recipe_id,)))

    return render_to_response('edit_recipe.html', {
        'form': recipe_form,
        'recipe': recipe,
    },
        context_instance=RequestContext(request)
    )


@user_passes_test(lambda u: u.is_superuser, login_url='not_authorized')
def edit_ingredient(request, ingredient_id):

    ingredient = Ingredient.objects.get(id=ingredient_id)
    recipe = Recipe.objects.get(id=ingredient.recipe_id)

    if request.method == 'POST':
        ingredient_form = IngredientForm(request.POST, instance=Ingredient.objects.get(id=ingredient_id))

        if ingredient_form.is_valid():
            formpost = ingredient_form.save(commit=False)
            formpost.user = request.user
            formpost.edited = datetime.now()
            formpost.save()
            return HttpResponseRedirect(reverse('edit_recipe', args=(recipe.id,)))

    else:
        ingredient_form = IngredientForm(instance=ingredient)

        return render_to_response('edit_ingredient.html', {'ingredient_form': ingredient_form,
                                                                'recipe': recipe,
                                                                'ingredient': ingredient},
                                  context_instance=RequestContext(request))


@user_passes_test(lambda u: u.is_superuser, login_url='not_authorized')
def delete_ingredient(request, ingredient_id):
    i = Ingredient.objects.get(pk=ingredient_id)
    Ingredient.objects.filter(pk=ingredient_id).delete()
    return HttpResponseRedirect(reverse('recipe_details', args=(i.recipe_id,)) + '#ingredients')


@login_required()
def comment_delete(request, comment_id):
    c = Comment.objects.get(pk=comment_id)
    Comment.objects.filter(pk=comment_id).delete()
    return HttpResponseRedirect(reverse('recipe_details', args=(c.recipe_id,)) + '#comments')


class FauxTb(object):
    def __init__(self, tb_frame, tb_lineno, tb_next):
        self.tb_frame = tb_frame
        self.tb_lineno = tb_lineno
        self.tb_next = tb_next


def current_stack(skip=0):
    try:
        1 / 0
    except ZeroDivisionError:
        f = sys.exc_info()[2].tb_frame
    for i in xrange(skip + 2):
        f = f.f_back
    lst = []
    while f is not None:
        lst.append((f, f.f_lineno))
        f = f.f_back
    return lst


def extend_traceback(tb, stack):
    """Extend traceback with stack info."""
    head = tb
    for tb_frame, tb_lineno in stack:
        head = FauxTb(tb_frame, tb_lineno, head)
    return head


def full_exc_info():
    """Like sys.exc_info, but includes the full traceback."""
    t, v, tb = sys.exc_info()
    full_tb = extend_traceback(tb, current_stack(1))
    return t, v, full_tb


def loggedin(request):
    return HttpResponseRedirect(reverse('my_recipes'))


def not_authorized(request):
    return render_to_response(
        'registration/not_authorized.html',
        context_instance=RequestContext(request)
    )


def loggedout(request):
    return render_to_response(
        'registration/loggedout.html',
        context_instance=RequestContext(request)
    )


@login_required()
def my_recipes(request):

    user = request.user

    recipes = Recipe.objects.filter(user_id=user.id)
    comments = Comment.objects.filter(user_id=user.id)
    recipe_form = RecipeForm()

    return render_to_response('my_recipes.html', {
        'recipes': recipes,
        'comments': comments,
        'recipe_form': recipe_form,
        },
        context_instance=RequestContext(request)
    )


@user_passes_test(lambda u: u.is_superuser, login_url='not_authorized')
def move_ingredient_up(request, ingredient_id):

    ingredient = Ingredient.objects.get(id=ingredient_id)

    try:
        next_ingredient_up = Ingredient.objects.filter(recipe_id=ingredient.recipe_id).exclude(
            sorting__gte=ingredient.sorting).order_by('-sorting')[0]
    except IndexError:
        next_ingredient_up = Ingredient.objects.filter(recipe_id=ingredient.recipe_id).filter(
            sorting__gte=ingredient.sorting).order_by('-sorting')[0]

    next_ingredient = Ingredient.objects.get(id=next_ingredient_up.id)

    if next_ingredient.sorting > ingredient.sorting:
        ingredient.sorting = next_ingredient_up.sorting + 10
        ingredient.save()

    else:
        next_ingredient.sorting = ingredient.sorting
        next_ingredient.save()

        ingredient.sorting = next_ingredient_up.sorting
        ingredient.save()

    return HttpResponseRedirect(reverse('edit_recipe', args=(ingredient.recipe_id,)))


@user_passes_test(lambda u: u.is_superuser, login_url='not_authorized')
def move_ingredient_down(request, ingredient_id):

    ingredient = Ingredient.objects.get(id=ingredient_id)

    try:
        next_ingredient_down = Ingredient.objects.filter(recipe_id=ingredient.recipe_id).exclude(
            sorting__lte=ingredient.sorting).order_by('sorting')[0]
    except IndexError:
        next_ingredient_down = Ingredient.objects.filter(recipe_id=ingredient.recipe_id).filter(
            sorting__lte=ingredient.sorting).order_by('sorting')[0]

    next_ingredient = Ingredient.objects.get(id=next_ingredient_down.id)

    if next_ingredient.sorting < ingredient.sorting:
        ingredient.sorting = next_ingredient_down.sorting - 10
        ingredient.save()

    else:
        next_ingredient.sorting = ingredient.sorting
        next_ingredient.save()

        ingredient.sorting = next_ingredient_down.sorting
        ingredient.save()

    return HttpResponseRedirect(reverse('edit_recipe', args=(ingredient.recipe_id,)))


@login_required()
def clear_recipe_filter(request):

    return HttpResponseRedirect(reverse('my_recipes'))
