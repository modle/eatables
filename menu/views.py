from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from fractions import Fraction
from django.template import RequestContext
import csv
from datetime import datetime
from django.forms.models import modelformset_factory
import logging
import json
import sys
import math


from menu.forms import *
from .models import Recipe, Ingredient, ShoppingList


class Index(generic.ListView):
    model = Recipe
    template_name = 'menu/index.html'

    def get_queryset(self):
        return Recipe.objects.filter(enabled=1)


def addtoshoppinglist(request, recipeId):
    for key in request.POST:
        if key != 'csrfmiddlewaretoken':
            value = (request.POST[key])

            listItem, created = ShoppingList.objects.get_or_create(ingredient_id=key)
            entry = get_object_or_404(ShoppingList, ingredient_id=key)
            #this math needs work; alternate is to store as decimal, then math.ceil when model is read
            if created:
                entry.amount = math.ceil(float(value))
            else:
                entry.amount = math.ceil(float(entry.amount) + float(value))
                # entry.amount = entry.amount + Decimal(float(value))

            entry.save()

    return HttpResponseRedirect(reverse('menu:recipedetails', args=(recipeId,)))


def manageshoppinglist(request):
    logger = logging.getLogger(__name__)

    ShoppingListFormSet = modelformset_factory(ShoppingList, form=ShoppingListForm, extra=0)

    if request.method == 'POST':
        formset = ShoppingListFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            logger.debug('Formset saved')
        else:
            logger.debug('Formset invalid')

    else:
        formset = ShoppingListFormSet()

    logger.debug('POST DATA:\n %s', json.dumps(request.POST, indent=4, sort_keys=True))
    logger.debug('LOCALS:\n %s', locals())

    return render_to_response(
        'menu/manageshoppinglist.html',
        {'formset': formset},
        context_instance=RequestContext(request))

class ArchiveList(generic.ListView):
    model = ShoppingList
    template_name = 'menu/archivelist.html'

    def get_queryset(self):
        return ShoppingList.objects.all()


class RecipeDetail(generic.DetailView):
    model = Recipe
    template_name = 'menu/recipedetails.html'

    def get_queryset(self):
        return Recipe.objects.all()

def retiredrecipes(request):
    logger = logging.getLogger(__name__)

    RetiredRecipesFormSet = modelformset_factory(Recipe, form=RetiredRecipesForm, extra=0)

    if request.method == 'POST':
        formset = RetiredRecipesFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            logger.debug('Formset saved')
        else:
            logger.debug('Formset invalid')
        return HttpResponseRedirect(reverse('menu:index'))
    else:
        formset = RetiredRecipesFormSet()

    logger.debug('POST DATA:\n %s', json.dumps(request.POST, indent=4, sort_keys=True))
    logger.debug('LOCALS:\n %s', locals())

    return render_to_response(
        'menu/retiredrecipes.html',
        {'formset': formset},
        context_instance=RequestContext(request))


def addrecipe(request):
    r = Recipe(name="_Update Me_" + str(datetime.now()))
    r.save()
    return HttpResponseRedirect(reverse('menu:editrecipe', args=(r.id,)))


def disablerecipe(request, recipeId):
    r = get_object_or_404(Recipe, pk=recipeId)
    r.enabled = 0
    r.save()
    return HttpResponseRedirect(reverse('menu:index'))


def deleterecipeforever(request, recipeId):
    Recipe.objects.filter(pk=recipeId).delete()
    return HttpResponseRedirect(reverse('menu:index'))


class EditRecipe(generic.DetailView):
    model = Recipe
    template_name = 'menu/editrecipe.html'

    def get_queryset(self):
        return Recipe.objects.all()


def updaterecipe(request, recipeId):
    r = get_object_or_404(Recipe, id=recipeId)
    r.name = request.POST['name']
    r.prepMethod = request.POST['method']
    r.temperature = request.POST['temp']
    r.prepTime = request.POST['prep']
    r.cookTime = request.POST['cook']
    r.servings = request.POST['serves']
    r.directions = request.POST['directions']
    r.source = request.POST['source']
    r.save()
    return HttpResponseRedirect(reverse('menu:recipedetails', args=(r.id,)))


def updateingredient(request, recipeId):
    # loop through post form
    for key in request.POST:
        key_split = key.split(',')
        ingredient_id = key_split[0]

        # Awkwardly avoid the middlewaretoken that is being submitted
        if ingredient_id != 'csrfmiddlewaretoken':
            ingredient_field = key_split[1]
            ingredient = Ingredient.objects.get(pk=ingredient_id)
            value = (request.POST[key])

            # If the user entered a fraction, convert it to a float!
            if ingredient_field == 'amount':
                if '/' in value:
                    value = float(Fraction(value))
                elif value == "":
                    value = 0.0

            # Update the field on the ingredient from this line
            setattr(ingredient, ingredient_field, value)
            ingredient.save()

    return HttpResponseRedirect(reverse('menu:recipedetails', args=(recipeId,)))


def deleteingredient(request, ingredientId):
    i = Ingredient.objects.get(pk=ingredientId)
    Ingredient.objects.filter(pk=ingredientId).delete()
    return HttpResponseRedirect(reverse('menu:editrecipe', args=(i.recipe_id,)) + '#ingredients')


def addingredient(request, recipeId):
    r = Recipe.objects.get(pk=recipeId)

    now = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f'))
    r.ingredient_set.create(name="_Update Me_" + now, amount="0.0", unit="unit")
    return HttpResponseRedirect(reverse('menu:editrecipe', args=(recipeId,)) + '#ingredients')


def addcomment(request, recipeId):
    r = Recipe.objects.get(pk=recipeId)
    r.comment_set.create(comment=request.POST['comment'])
    return HttpResponseRedirect(reverse('menu:recipedetails', args=(recipeId,)) + '#comments')


def uploadrecipe(request):
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
                        entry.prepMethod = row[1]
                        entry.temperature = row[2]
                        entry.directions = row[3]
                        entry.source = row[4]
                        if row[5] == '':
                            entry.servings = 0
                        else:
                            entry.servings = row[5]
                        if row[6] == '':
                            entry.prepTime = 0
                        else:
                            entry.prepTime = row[6]
                        if row[7] == '':
                            entry.cookTime = 0
                        else:
                            entry.cookTime = row[7]
                        entry.save()

        return HttpResponseRedirect(reverse('menu:index'))

    else:
        form = DocumentForm()  # An empty, unbound form
        # Load documents for the list page

    return render_to_response(
        'menu/uploadrecipe.html',
        {'form': form},
        context_instance=RequestContext(request)
    )
    # return HttpResponseRedirect(reverse('menu:showdocuments'))


def uploadingredients(request):
    # Handle file upload #update for ingredient additions

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            reader = csv.reader(form.cleaned_data['docfile'])
            for row in reader:
                recipe = get_object_or_404(Recipe, name=row[0])
                _, created = Ingredient.objects.get_or_create(
                    name=row[1],
                    recipe_id=recipe.id,
                    amount=row[2],
                    unit=row[3],
                    comment=row[4],
                )
        return HttpResponseRedirect(reverse('menu:index'))

    else:
        form = DocumentForm()  # An empty, unbound form
        # Load documents for the list page

    return render_to_response(
        'menu/uploadrecipe.html',
        {'form': form},
        context_instance=RequestContext(request)
    )
    # return HttpResponseRedirect(reverse('menu:showdocuments'))


class TestListView(generic.ListView):
    model = Recipe
    template_name = 'menu/test.html'

    def get_queryset(self):
        return Recipe.objects.all()


class FauxTb(object):
    def __init__(self, tb_frame, tb_lineno, tb_next):
        self.tb_frame = tb_frame
        self.tb_lineno = tb_lineno
        self.tb_next = tb_next

def current_stack(skip=0):
    try: 1/0
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
