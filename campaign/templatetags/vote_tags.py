from django.template import Library

register = Library()


@register.simple_tag()
def multiply(lhs, rhs):
    return lhs * rhs