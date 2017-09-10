from django import template
from fractions import Fraction

register = template.Library()

# filters
@register.filter(name='minutes_to_hours')
def minutestohours(value):
    return value / 60.0

@register.filter(name='hours_to_minutes')
def hourstominutes(value):
    return value * 60

@register.filter(name='strip_zeros')
def stripzeroes(value):
    result = str(value).rstrip('.00')
    return result

@register.filter(name='convert_to_float')
def converttofloat(value):
    value_float = float(value)
    return value_float

@register.filter(name='show_fraction')
def show_fraction(value):
    value_split = str(value).split('.')
    decimal = '.' + value_split[1]
    if value_split[1] == '00' or float(decimal) < 0.1:
        fraction = str('')
    else:
        fraction = str(Fraction(decimal).limit_denominator(10))
    return fraction

@register.filter(name='show_integer')
def show_integer(value):
    value_split = str(value).split('.')
    if value_split[0] == '0':
        decimal = ''
    else:
        decimal = value_split[0] + ' '
    return decimal

@register.filter(name='generate_img_path')
def generate_img_path(value):
    value = 'menu/img/' + value + '.png'
    return value
