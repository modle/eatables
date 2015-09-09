from django.shortcuts import get_object_or_404, render_to_response, render
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
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator

from menu.forms import *
from .models import Recipe, Ingredient, ShoppingList, Fridge, Comment


def basetemplate(request):
    return render(request, 'base.html', )

class Index(generic.ListView):
    model = Recipe
    template_name = 'menu/index.html'

    def get_queryset(self):
        return Recipe.objects.filter(enabled=1)

@user_passes_test(lambda u: u.is_superuser, login_url='notauthorized')
def addtoshoppinglist(request, recipeId):
    for key in request.POST:
        if key != 'csrfmiddlewaretoken':
            value = (request.POST[key])

            listItem, created = ShoppingList.objects.get_or_create(ingredient_id=key)
            i = Ingredient.objects.get(id=key)
            entry = get_object_or_404(ShoppingList, ingredient_id=key)
            # this math needs work; alternate is to store as decimal, then math.ceil when model is read
            if created:
                entry.amount = math.ceil(float(value))
            else:
                entry.amount = math.ceil(float(entry.amount) + float(value))
                # entry.amount = entry.amount + Decimal(float(value))
            entry.name = i.name
            entry.save()

    return HttpResponseRedirect(reverse('menu:recipedetails', args=(recipeId,)))

@user_passes_test(lambda u: u.is_superuser, login_url='notauthorized')
def shoppinglist(request):
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
        formset = ShoppingListFormSet(queryset=ShoppingList.objects.filter(status=False))

    logger.debug('POST DATA:\n %s', json.dumps(request.POST, indent=4, sort_keys=True))
    logger.debug('LOCALS:\n %s', locals())

    return render_to_response(
        'menu/shoppinglist.html',
        {'formset': formset, },
        context_instance=RequestContext(request))

@user_passes_test(lambda u: u.is_superuser, login_url='notauthorized')
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


class ArchiveList(generic.ListView):
    model = ShoppingList
    template_name = 'menu/shoppinglisthistory.html'

    def get_queryset(self):
        return ShoppingList.objects.all()


class RecipeDetail(generic.DetailView):
    model = Recipe
    template_name = 'menu/recipedetails.html'

    def get_queryset(self):
        return Recipe.objects.all()


def recipedetails(request, recipeId):

    recipe = Recipe.objects.get(pk=recipeId)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            formpost = form.save(commit=False)
            formpost.user_id = request.user_id
            formpost.editDate = datetime.now()
            formpost.save()

    else:
        form = CommentForm()

    return render_to_response('menu/recipedetails.html', {'form': form, 'recipe': recipe, },
                              context_instance=RequestContext(request))



@user_passes_test(lambda u: u.is_superuser, login_url='notauthorized')
def archivedrecipes(request):
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
        formset = ArchivedRecipesFormSet(queryset=Recipe.objects.filter(enabled=False))

    logger.debug('POST DATA:\n %s', json.dumps(request.POST, indent=4, sort_keys=True))
    logger.debug('LOCALS:\n %s', locals())

    return render_to_response(
        'menu/archivedrecipes.html',
        {'formset': formset},
        context_instance=RequestContext(request))


@user_passes_test(lambda u: u.is_superuser, login_url='notauthorized')
def addrecipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)

        if form.is_valid():
            formpost = form.save(commit=False)
            formpost.user = request.user
            formpost.edited = datetime.now()
            formpost.save()
            recipeId = formpost.id
            return HttpResponseRedirect(reverse('menu:recipedetails', args=(recipeId,)))

    else:
        form = RecipeForm()

    return render_to_response('menu/editrecipe_form.html', {'form': form},
                              context_instance=RequestContext(request))


@user_passes_test(lambda u: u.is_superuser, login_url='notauthorized')
def deleterecipeforever(request, recipeId):
    Recipe.objects.filter(pk=recipeId).delete()
    return HttpResponseRedirect(reverse('menu:index'))


@user_passes_test(lambda u: u.is_superuser, login_url='notauthorized')
def editrecipe(request, recipeId):
    if request.method == 'POST':

        form = RecipeForm(request.POST, instance=Recipe.objects.get(id=recipeId))

        if form.is_valid():
            formpost = form.save(commit=False)
            formpost.user = request.user
            formpost.edited = datetime.now()
            formpost.save()
            recipeId = formpost.id
        return HttpResponseRedirect(reverse('menu:recipedetails', args=(recipeId,)))

    else:
        recipe = Recipe.objects.get(id=recipeId)
        form = RecipeForm(instance=recipe)

    return render_to_response('menu/editrecipe_form.html', {'form': form},
                              context_instance=RequestContext(request))


class EditIngredients(generic.DetailView):
    model = Recipe
    template_name = 'menu/editingredients.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='notauthorized'))
    def dispatch(self, *args, **kwargs):
        return super(EditIngredients, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return Recipe.objects.all()


@user_passes_test(lambda u: u.is_superuser, login_url='notauthorized')
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


@user_passes_test(lambda u: u.is_superuser, login_url='notauthorized')
def deleteingredient(request, ingredientId):
    i = Ingredient.objects.get(pk=ingredientId)
    Ingredient.objects.filter(pk=ingredientId).delete()
    return HttpResponseRedirect(reverse('menu:editingredients', args=(i.recipe_id,)) + '#ingredients')


@user_passes_test(lambda u: u.is_superuser, login_url='notauthorized')
def addingredient(request, recipeId):
    r = Recipe.objects.get(pk=recipeId)

    now = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f'))
    r.ingredient_set.create(name="_Update Me_" + now, amount="0.0", unit="unit")
    return HttpResponseRedirect(reverse('menu:editingredients', args=(recipeId,)) + '#ingredients')


@login_required()
def addcomment(request, recipeId):
    r = Recipe.objects.get(pk=recipeId)
    r.comment_set.create(comment=request.POST['comment'])
    return HttpResponseRedirect(reverse('menu:recipedetails', args=(recipeId,)) + '#comments')


@login_required()
def commentdelete(request, commentId):
    c = Comment.objects.get(pk=commentId)
    Comment.objects.filter(pk=commentId).delete()
    return HttpResponseRedirect(reverse('menu:recipedetails', args=(c.recipe_id,)) + '#comments')


@user_passes_test(lambda u: u.is_superuser, login_url='notauthorized')
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


@user_passes_test(lambda u: u.is_superuser, login_url='notauthorized')
def uploadingredients(request):
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
        'menu/uploadrecipe.html',
        {'form': form},
        context_instance=RequestContext(request)
    )
    # return HttpResponseRedirect(reverse('menu:showdocuments'))


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


def notauthorized(request):
    return render_to_response(
        'registration/not_authorized.html',
        context_instance=RequestContext(request)
    )


def loggedout(request):
    return render_to_response(
        'registration/loggedout.html',
        context_instance=RequestContext(request)
    )
