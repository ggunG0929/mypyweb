from django import template

register = template.Library()   # import django

@register.filter
def sub(value, arg):
    return value - arg  # 원래값 - 매개값 -> 원래값|sub:arg(매개값)
