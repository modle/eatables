from django import forms
from django.forms import ModelForm, Textarea
from .models import Ingredient, Recipe, Fridge, Comment, Rating


class RecipeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'Name'})
        self.fields['temperature'].widget.attrs.update({'placeholder': 'temperature'})
        self.fields['directions'].widget.attrs.update({'placeholder': 'directions'})
        self.fields['source'].widget.attrs.update({'placeholder': 'recipe URL'})
        self.fields['servings'].widget.attrs.update({'placeholder': '0'})
        self.fields['prep_time'].widget.attrs.update({'placeholder': '0'})
        self.fields['cook_time'].widget.attrs.update({'placeholder': '0'})
        self.fields['description'].widget.attrs.update({'placeholder': 'description'})
        self.fields['banner_image'].widget.attrs.update({'placeholder': 'image URL'})

    class Meta:
        model = Recipe
        fields = ('name', 'cook_method', 'temperature', 'directions', 'source', 'servings', 'prep_time', 'cook_time', 'published', 'description', 'banner_image', 'dish_type', )
        widgets = {
            'directions': Textarea(attrs={'cols': 80, 'rows': 20}),
            'description': Textarea(attrs={'cols': 80, 'rows': 5}),
        }

class DocumentForm(forms.Form):
    docfile = forms.FileField(label='Select file')


class ArchivedRecipesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ArchivedRecipesForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['readonly'] = True
        self.fields['name'].widget.attrs.update({'id': 'formfieldastext'})

    class Meta:
        model = Recipe
        fields = ('published', 'name',)
        labels = {
            'published': '',
            'name': '',
        }


class FridgeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FridgeForm, self).__init__(*args, **kwargs)
        self.queryset = Fridge.objects.all()
        self.fields['item'].widget.attrs.update({'id': 'formfieldastextshort'})
        self.fields['expires'].widget.attrs.update({'class': 'datepicker'})
        self.fields['fridgedate'].widget.attrs.update({'class': 'datepicker'})
        # self.fields['fridgedate'].widget.attrs.update({'id': 'formfieldastextshort'})
        # self.fields['expires'].widget.attrs.update({'id': 'formfieldastextshort'})

    class Meta:
        model = Fridge
        # fields = '__all__'
        fields = ('item', 'fridgedate', 'expires',)
        labels = {
            'item': '',
            'fridgedate': 'fridged on',
            'expires': 'expires',
        }

class CommentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['comment'].widget.attrs.update({'placeholder': 'Comment'})

    class Meta:
        model = Comment
        fields = ('comment',)
        labels = {
            'comment': '',
        }
        widgets = {
            'comment': Textarea(attrs={'cols': 10, 'rows': 6}),
        }

class RatingForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RatingForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Rating
        fields = ('rating', )

class IngredientForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(IngredientForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'Name'})
        self.fields['amount'].widget.attrs.update({'placeholder': 0})
        self.fields['unit'].widget.attrs.update({'placeholder': 'Unit of Measurement'})
        self.fields['comment'].widget.attrs.update({'placeholder': 'Other Details'})

    class Meta:
        model = Ingredient
        fields = ('name', 'comment', 'amount', 'unit', )
        labels = {
            'name': 'Ingredient Name'
        }

class SearchForm(forms.Form):
    search_term = forms.CharField(label='Search', max_length=100)
