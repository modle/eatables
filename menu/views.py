from django.shortcuts import get_object_or_404, render_to_response, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
import csv
from datetime import datetime
from django.forms.models import modelformset_factory
import logging
import json
import sys
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required, user_passes_test

from menu.forms import *
from .models import Recipe, Ingredient, ShoppingList, Fridge, Comment


def base_template(request):
    return render(request, 'base.html', )


def index(request):

    search_form = SearchForm()
    top10recipes = Recipe.objects.filter(published='True')

    if request.method == 'POST':
        search_form = SearchForm(request.POST)

        if search_form.is_valid():
            search_term = search_form.cleaned_data['search_term']

            recipes = Recipe.objects.filter(name__icontains=search_term)
        else:
            recipes = Recipe.objects.filter(published='True')
    else:
        recipes = Recipe.objects.filter(published='True')

    return render_to_response('menu/index.html', {
        'recipes': recipes,
        'top10recipes': top10recipes,
        'search_form': search_form,
        },
        context_instance=RequestContext(request)
    )


@user_passes_test(lambda u: u.is_superuser, login_url='not_authorized')
def add_to_shopping_list(request, ingredient_id):

    ingredient = Ingredient.objects.get(id=ingredient_id)
    list_item, created = ShoppingList.objects.get_or_create(ingredient_id=ingredient_id)

    list_item.amount = ingredient.amount
    list_item.name = ingredient.name
    list_item.ingredient = ingredient
    list_item.completed = False
    list_item.save()

    return HttpResponseRedirect(reverse('menu:recipe_details', args=(ingredient.recipe_id,)))


@user_passes_test(lambda u: u.is_superuser, login_url='not_authorized')
def shopping_list(request):

    shopping_list_entries = ShoppingList.objects.filter(completed=False)
    complete_shopping_list_entries = ShoppingList.objects.filter(completed=True)

    return render_to_response(
        'menu/shopping_list.html',
        {'shopping_list_entries': shopping_list_entries,
         'complete_shopping_list_entries': complete_shopping_list_entries, },
        context_instance=RequestContext(request))


@user_passes_test(lambda u: u.is_superuser, login_url='not_authorized')
def shopping_list_check_off(request, shopping_list_id):

    shopping_list_entry = ShoppingList.objects.get(shoppingListId=shopping_list_id)
    shopping_list_entry.completed = True
    shopping_list_entry.save()

    return HttpResponseRedirect(reverse('menu:shopping_list'))


@user_passes_test(lambda u: u.is_superuser, login_url='not_authorized')
def fridge(request):
    logger = logging.getLogger(__name__)

    FridgeFormSet = modelformset_factory(Fridge, form=FridgeForm, extra=0)

    if request.method == 'POST':
        formset = FridgeFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            logger.debug('Formset saved')
        else:
            logger.debug('Formset invalid')

    else:
        formset = FridgeFormSet()

    logger.debug('POST DATA:\n %s', json.dumps(request.POST, indent=4, sort_keys=True))
    logger.debug('LOCALS:\n %s', locals())

    return render_to_response(
        'menu/fridge.html',
        {'formset': formset},
        context_instance=RequestContext(request))


def update_rating(request, recipe_id, csrfmiddlewaretoken):
    recipe = Recipe.objects.get(pk=recipe_id)
    user = request.user

    rating_entry, created = Rating.objects.get_or_create(recipe=recipe, user=user)

    rating_entry.rating = 'rating'
    rating_entry.save()


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
            return HttpResponseRedirect(reverse('menu:recipe_details', args=(recipe_id,)))

    else:
        form = RecipeForm()

    return render_to_response('menu/edit_recipe.html', {'form': form},
                              context_instance=RequestContext(request))


def recipe_details(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    user = request.user

    if user.is_authenticated():

        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            try:
                rating_form = RatingForm(request.POST, instance=Rating.objects.get(recipe=recipe, user=user))
            except Rating.DoesNotExist:
                rating_form = RatingForm(request.POST)
            ingredient_form = IngredientForm(request.POST)

            if comment_form.is_valid():
                comment_save = comment_form.save(commit=False)
                comment_save.user = user
                comment_save.editDate = datetime.now()
                comment_save.recipe = recipe
                comment_save.save()

            if rating_form.is_valid():
                rating_save = rating_form.save(commit=False)
                rating_save.user = user
                rating_save.editDate = datetime.now()
                rating_save.recipe = recipe
                rating_save.save()

            if ingredient_form.is_valid():
                max_ingredient_sorting = Ingredient.objects.filter(recipe_id=recipe).order_by('-sorting')[0]

                ingredient_save = ingredient_form.save(commit=False)
                ingredient_save.recipe = recipe
                ingredient_save.sorting = max_ingredient_sorting.sorting + 10
                ingredient_save.save()

            return HttpResponseRedirect(reverse('menu:recipe_details', args=(recipe_id,)))

        else:
            comment_form = CommentForm()

            try:
                rating_entry = Rating.objects.get(recipe=recipe, user=user)
                rating_form = RatingForm(instance=rating_entry)
            except Rating.DoesNotExist:
                rating_form = RatingForm()

            ingredient_form = IngredientForm()

    else:
        comment_form = CommentForm()
        rating_form = RatingForm()
        ingredient_form = IngredientForm()

    return render_to_response('menu/recipe_details.html',
                              {'comment_form': comment_form,
                               'rating_form': rating_form,
                               'ingredient_form': ingredient_form,
                               'recipe': recipe, },
                              context_instance=RequestContext(request))


@user_passes_test(lambda u: u.is_superuser, login_url='not_authorized')
def archived_recipes(request):
    logger = logging.getLogger(__name__)

    ArchivedRecipesFormSet = modelformset_factory(Recipe, form=ArchivedRecipesForm, extra=0)

    if request.method == 'POST':
        formset = ArchivedRecipesFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            logger.debug('Formset saved')
        else:
            logger.debug('Formset invalid')
        return HttpResponseRedirect(reverse('menu:index'))
    else:
        formset = ArchivedRecipesFormSet(queryset=Recipe.objects.filter(published=False))

    logger.debug('POST DATA:\n %s', json.dumps(request.POST, indent=4, sort_keys=True))
    logger.debug('LOCALS:\n %s', locals())

    return render_to_response(
        'menu/archived_recipes.html',
        {'formset': formset},
        context_instance=RequestContext(request))


@user_passes_test(lambda u: u.is_superuser, login_url='not_authorized')
def delete_recipe_forever(request, recipe_id):
    Recipe.objects.filter(pk=recipe_id).delete()
    return HttpResponseRedirect(reverse('menu:index'))


@user_passes_test(lambda u: u.is_superuser, login_url='not_authorized')
def edit_recipe(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)

    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=Recipe.objects.get(id=recipe_id))

        if form.is_valid():
            formpost = form.save(commit=False)
            formpost.user = request.user
            formpost.edited = datetime.now()
            formpost.save()
            recipe_id = formpost.id
        return HttpResponseRedirect(reverse('menu:recipe_details', args=(recipe_id,)))

    else:
        form = RecipeForm(instance=recipe)

    return render_to_response('menu/edit_recipe.html', {
        'form': form,
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
            return HttpResponseRedirect(reverse('menu:edit_recipe', args=(recipe.id,)))

    else:
        ingredient_form = IngredientForm(instance=ingredient)

        return render_to_response('menu/edit_ingredient.html', {'ingredient_form': ingredient_form,
                                                                'recipe': recipe,
                                                                'ingredient': ingredient},
                                  context_instance=RequestContext(request))


@user_passes_test(lambda u: u.is_superuser, login_url='not_authorized')
def delete_ingredient(request, ingredient_id):
    i = Ingredient.objects.get(pk=ingredient_id)
    Ingredient.objects.filter(pk=ingredient_id).delete()
    return HttpResponseRedirect(reverse('menu:recipe_details', args=(i.recipe_id,)) + '#ingredients')


@login_required()
def comment_delete(request, comment_id):
    c = Comment.objects.get(pk=comment_id)
    Comment.objects.filter(pk=comment_id).delete()
    return HttpResponseRedirect(reverse('menu:recipe_details', args=(c.recipe_id,)) + '#comments')


@user_passes_test(lambda u: u.is_superuser, login_url='not_authorized')
def upload_recipe(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            reader = csv.reader(form.cleaned_data['docfile'])
            for row in reader:
                _, created = Recipe.objects.get_or_create(
                    name=row[0],
                )
                entry = get_object_or_404(Recipe, name=row[0])
                if created:
                    entry.category = row[1]
                    entry.temperature = row[2]
                    entry.directions = row[3]
                    entry.source = row[4]
                    if row[5] == '':
                        entry.servings = 0
                    else:
                        entry.servings = row[5]
                    if row[6] == '':
                        entry.prep_time = 0
                    else:
                        entry.prep_time = row[6]
                    if row[7] == '':
                        entry.cook_time = 0
                    else:
                        entry.cook_time = row[7]
                    entry.save()

        return HttpResponseRedirect(reverse('menu:index'))

    else:
        form = DocumentForm()  # An empty, unbound form
        # Load documents for the list page

    return render_to_response(
        'menu/upload_recipe.html',
        {'form': form},
        context_instance=RequestContext(request)
    )


@user_passes_test(lambda u: u.is_superuser, login_url='not_authorized')
def upload_ingredients(request):
    # Handle file upload #update for ingredient additions

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            reader = csv.reader(form.cleaned_data['docfile'])
            for row in reader:
                recipe = get_object_or_404(Recipe, name=row[0])
                _, created = Ingredient.objects.get_or_create(
                    # name=row[1], defaults={"recipe_id": recipe.id, "amount": row[2], "unit": row[3], })
                    name=row[1], recipe_id=recipe.id, amount=row[2], unit=row[3])
                # entry = get_object_or_404(Ingredient, name=row[1], recipe_id=recipe.id, amount=row[2], unit=row[3],)

                entry = get_object_or_404(Ingredient.objects.filter(), name=row[1],
                                          recipe_id=recipe.id,
                                          amount=row[2],
                                          unit=row[3], )
                if created:
                    entry.comment = row[4]
                    entry.save()

        return HttpResponseRedirect(reverse('menu:index'))

    else:
        form = DocumentForm()  # An empty, unbound form
        # Load documents for the list page

    return render_to_response(
        'menu/upload_recipe.html',
        {'form': form},
        context_instance=RequestContext(request)
    )


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


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/accounts/register/complete')

    else:
        form = UserCreationForm()

    token = {}
    token.update(csrf(request))
    token['form'] = form

    return render_to_response(
        'registration/registration_form.html',
        token,
        context_instance=RequestContext(request)
    )


def registration_complete(request):
    return render_to_response(
        'registration/registration_complete.html',
        context_instance=RequestContext(request)
    )


def loggedin(request):
    return render_to_response(
        'registration/loggedin.html',
        context_instance=RequestContext(request)
    )


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
def profile(request, slug):

    user = request.user

    recipes = Recipe.objects.filter(user_id=user.id)
    comments = Comment.objects.filter(user_id=user.id)
    recipe_form = RecipeForm()

    return render_to_response('menu/profile.html', {
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

    return HttpResponseRedirect(reverse('menu:edit_recipe', args=(ingredient.recipe_id,)))


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

    return HttpResponseRedirect(reverse('menu:edit_recipe', args=(ingredient.recipe_id,)))


@login_required()
def clear_recipe_filter(request):

    return HttpResponseRedirect(reverse('menu:index'))
