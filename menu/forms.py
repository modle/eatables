from django import forms
from django.forms import ModelForm, Textarea
from .models import Recipe, Ingredient, Tag, Fridge, Comment, Rating


class RecipeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'Name'})
        self.fields['name'].widget.attrs.update({'class': 'form-field'})
        self.fields['temperature'].widget.attrs.update({'placeholder': 'temperature'})
        self.fields['temperature'].widget.attrs.update({'class': 'form-field'})
        self.fields['directions'].widget.attrs.update({'placeholder': 'directions'})
        self.fields['directions'].widget.attrs.update({'class': 'form-field'})
        self.fields['source'].widget.attrs.update({'placeholder': 'recipe URL'})
        self.fields['source'].widget.attrs.update({'class': 'form-field'})
        self.fields['servings'].widget.attrs.update({'placeholder': '0'})
        self.fields['servings'].widget.attrs.update({'class': 'form-field'})
        self.fields['prep_time'].widget.attrs.update({'placeholder': '0'})
        self.fields['prep_time'].widget.attrs.update({'class': 'form-field'})
        self.fields['cook_time'].widget.attrs.update({'placeholder': '0'})
        self.fields['cook_time'].widget.attrs.update({'class': 'form-field'})
        self.fields['description'].widget.attrs.update({'placeholder': 'description'})
        self.fields['description'].widget.attrs.update({'class': 'form-field'})
        self.fields['cook_method'].widget.attrs.update({'class': 'form-select'})
        self.fields['dish_type'].widget.attrs.update({'class': 'form-select'})

    class Meta:
        model = Recipe
        fields = ('name', 'cook_method', 'temperature', 'directions', 'source', 'servings', 'prep_time', 'cook_time',
                  'description', 'dish_type', )
        labels = {
            'name': 'Ingredient Name',
            'cook_method': 'Cook Method',
            'temperature': 'Temperature',
            'comment': 'Other Details',
            'directions': 'Directions',
            'source': 'URL',
            'servings': 'Servings',
            'prep_time': 'Prep Time (minutes)',
            'cook_time': 'Cook Time (minutes)',
            'description': 'Description',
            'dish_type': 'Dish Type',
        }


class FridgeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FridgeForm, self).__init__(*args, **kwargs)
        self.queryset = Fridge.objects.all()
        self.fields['item'].widget.attrs.update({'id': 'formfieldastextshort'})
        self.fields['expires'].widget.attrs.update({'class': 'datepicker'})
        self.fields['fridgedate'].widget.attrs.update({'class': 'datepicker'})

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
        self.fields['comment'].widget.attrs.update({'placeholder': 'Note'})
        self.fields['comment'].widget.attrs.update({'class': 'form-field'})
        self.fields['comment'].widget.attrs.update({'id': 'comment_field'})

    class Meta:
        model = Comment
        fields = ('comment',)
        labels = {
            'comment': '',
        }


class TagForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(TagForm, self).__init__(*args, **kwargs)
        self.fields['tag'].widget.attrs.update({'placeholder': 'tag'})
        self.fields['tag'].widget.attrs.update({'class': 'form-field'})
        self.fields['tag'].widget.attrs.update({'id': 'tag_field'})

    class Meta:
        model = Tag
        fields = ('name',)
        labels = {
            'name': '',
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
        self.fields['name'].widget.attrs.update({'class': 'form-field'})
        self.fields['name'].widget.attrs.update({'autofocus': 'autofocus'})
        self.fields['name'].widget.attrs.update({'id': 'ingredient_name'})
        self.fields['amount'].widget.attrs.update({'placeholder': 0})
        self.fields['amount'].widget.attrs.update({'class': 'form-field'})
        self.fields['amount'].widget.attrs.update({'id': 'ingredient_amount'})
        self.fields['unit'].widget.attrs.update({'placeholder': 'Unit of Measurement'})
        self.fields['unit'].widget.attrs.update({'class': 'form-field'})
        self.fields['unit'].widget.attrs.update({'id': 'ingredient_unit'})
        self.fields['comment'].widget.attrs.update({'placeholder': 'Other Details'})
        self.fields['comment'].widget.attrs.update({'class': 'form-field'})
        self.fields['comment'].widget.attrs.update({'id': 'ingredient_comment'})

    class Meta:
        model = Ingredient
        fields = ('name', 'comment', 'amount', 'unit', )
        labels = {
            'name': 'Ingredient Name',
            'amount': 'Amount',
            'unit': 'Unit',
            'comment': 'Other Details',
        }


class SearchForm(forms.Form):
    search_term = forms.CharField(label='', max_length=100)

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['search_term'].widget.attrs.update({'placeholder': 'Filter'})
        self.fields['search_term'].widget.attrs.update({'type': 'text'})
        self.fields['search_term'].widget.attrs.update({'class': 'search'})
