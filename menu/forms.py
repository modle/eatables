from django import forms
from .models import ShoppingList, Ingredient, Recipe


class DocumentForm(forms.Form):
    docfile = forms.FileField(label='Select file')


class ShoppingListForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ShoppingListForm, self).__init__(*args, **kwargs)
        self.queryset = ShoppingList.objects.all()
        self.fields['ingredient'].queryset = Ingredient.objects.filter(
            id__exact=self.instance.ingredient_id)
        self.fields['ingredient'].empty_label = None
        self.fields['ingredient'].widget.choices = self.fields['ingredient'].choices
        self.fields['ingredient'].widget.attrs['readonly'] = True
        self.fields['amount'].widget.attrs.update({'id': 'listform'})

    class Meta:
        model = ShoppingList
        # fields = '__all__'
        fields = ('status', 'amount', 'ingredient',)
        labels = {
            'status': '',
            'amount': '',
            'ingredient': '',
        }


class RetiredRecipesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RetiredRecipesForm, self).__init__(*args, **kwargs)
        self.queryset = Recipe.objects.filter(enabled=False)
        self.fields['name'].widget.attrs['readonly'] = True
        self.fields['name'].widget.attrs.update({'id': 'retiredrecipesform'})

    class Meta:
        model = Recipe
        fields = ('enabled', 'name',)
        labels = {
            'enabled': '',
            'name': '',
        }
