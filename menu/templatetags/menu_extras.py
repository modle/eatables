from django import template
from fractions import Fraction

register = template.Library()

#filters
@register.filter(name='minutestohours')
def minutestohours(value):
    return value / 60.0

@register.filter(name='hourstominutes')
def hourstominutes(value):
    return value * 60

@register.filter(name='stripzeros')
def stripzeroes(value):
    result = str(value).rstrip('.00')
    return result

@register.filter(name='converttofloat')
def converttofloat(value):
    value_float = float(value)
    return value_float

@register.filter(name='showfraction')
def showfraction(value):
    value_split = str(value).split('.')
    decimal = '.' + value_split[1]
    if value_split[1] == '00' or float(decimal) < 0.1:
        fraction = str('')
    else:
        fraction = str(Fraction(decimal).limit_denominator(10))
    return fraction

@register.filter(name='showinteger')
def showinteger(value):
    value_split = str(value).split('.')
    if value_split[0] == '0':
        decimal = ''
    else:
        decimal = value_split[0] + ' '
    return decimal

